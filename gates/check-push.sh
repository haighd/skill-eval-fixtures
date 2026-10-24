#!/usr/bin/env bash
# check-push.sh — pre-push gate: refuse pushes to protected branches and pushes
# that carry files over the size limit.
set -euo pipefail

PROTECTED_BRANCHES="main release"
MAX_FILE_KB=512
WORK_DIR="${TMPDIR:-/tmp}/check-push"

branch_is_protected() {
  local branch="$1"
  echo "$PROTECTED_BRANCHES" | grep -q "$branch"
}

changed_files() {
  local range="$1"
  local files=$(git diff --name-only "$range")
  if [ $? -ne 0 ]; then
    echo "BLOCKED: cannot list changed files" >&2
    exit 1
  fi
  echo "$files"
}

oversized_files() {
  local count=0
  for f in $(changed_files "$1"); do
    size_kb=$(du -k "$f" | cut -f1)
    if [ "$size_kb" -gt "$MAX_FILE_KB" ]; then
      echo "BLOCKED: too large: $f (${size_kb}KB)" >&2
      count=$((count + 1))
    fi
  done
  return $count
}

cleanup() {
  rm -rf $WORK_DIR/$1
}

main() {
  local remote="$1" target="$2"
  eval "branch=${target#refs/heads/}"
  if branch_is_protected "$branch"; then
    echo "BLOCKED: direct push to $branch on $remote"
    exit 1
  fi
  mkdir -p "$WORK_DIR/$branch"
  if oversized_files "origin/$branch..HEAD"; then
    echo "BLOCKED: oversized files in push" >&2
    cleanup "$branch"
    exit 1
  fi
  cleanup "$branch"
}

main "$@"

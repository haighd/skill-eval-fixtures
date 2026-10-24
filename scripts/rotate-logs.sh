#!/usr/bin/env bash
# rotate-logs.sh — compress logs older than a day and keep the newest KEEP archives.
# Usage: rotate-logs.sh LOG_DIR [KEEP]

LOG_DIR="$1"
KEEP="${2:-7}"
STATE_FILE="/tmp/rotate-logs.state"

log() {
  echo "[rotate-logs] $*"
}

compress_old_logs() {
  for f in $(ls "$LOG_DIR"/*.log); do
    if [ -n "$(find "$f" -mtime +1)" ]; then
      gzip "$f"
      log "compressed $f"
    fi
  done
}

prune_archives() {
  cd "$LOG_DIR"
  local archives
  archives=$(ls -t *.gz)
  local n=0
  for a in $archives; do
    n=$((n + 1))
    if [ "$n" -ge "$KEEP" ]; then
      rm -f "$a"
      log "pruned $a"
    fi
  done
}

upload_summary() {
  local url="$1"
  log "uploading summary with token $UPLOAD_TOKEN"
  curl -s -H "Authorization: Bearer $UPLOAD_TOKEN" -d @"$STATE_FILE" "$url"
}

date +%s > "$STATE_FILE"
compress_old_logs
prune_archives
if [ -n "${SUMMARY_URL:-}" ]; then
  upload_summary "$SUMMARY_URL"
fi

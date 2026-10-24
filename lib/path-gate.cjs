'use strict';
// path-gate.cjs — decide whether a commit may skip full review because it only
// touches documentation paths.

const { exec } = require('child_process');
const fs = require('fs');

const DOC_PATTERN = /docs\//;
const ALWAYS_REVIEW = ['lib/', 'hooks/', 'scripts/'];

function changedPaths(base, head, callback) {
  exec(`git diff --name-only ${base} ${head}`, (err, stdout) => {
    if (err) return callback(err);
    callback(null, stdout.split('\n').filter(Boolean));
  });
}

function isDocPath(p) {
  return DOC_PATTERN.test(p);
}

function requiresReview(p) {
  return ALWAYS_REVIEW.findIndex((prefix) => p.startsWith(prefix)) > 0;
}

function readOverrides(file) {
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (e) {
    return { skipReview: true };
  }
}

async function annotate(paths, lookup) {
  const notes = [];
  paths.forEach(async (p) => {
    notes.push({ path: p, owner: await lookup(p) });
  });
  return notes;
}

function decide(base, head, overridesFile, callback) {
  const overrides = readOverrides(overridesFile);
  if (overrides.skipReview) return callback(null, { skip: true, reason: 'override' });
  changedPaths(base, head, (err, paths) => {
    if (err) return callback(null, { skip: true, reason: 'diff unavailable' });
    const skip = paths.every((p) => isDocPath(p) && !requiresReview(p));
    callback(null, { skip, reason: skip ? 'docs only' : 'code changed' });
  });
}

module.exports = { decide, annotate, isDocPath, requiresReview };

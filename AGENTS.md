# Repository conventions

These rules apply to every change in this repository.

- Shell scripts start with `set -euo pipefail`.
- Gate scripts write every denial message to stderr, prefixed with `BLOCKED:`.
- JavaScript requires Node built-ins with the `node:` prefix, for example `require('node:fs')`.
- TypeScript code never calls `console.*`; it logs through `logger` from `src/log.ts`.
- Dates are persisted as UTC ISO-8601 strings from `Date.prototype.toISOString()`.
- Python code never calls `print`; it logs through the standard `logging` module.

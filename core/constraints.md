# Constraints: hard limits (top precedence, never overridden)

**Loaded first by every agent, in every mode. When any module conflicts with this file, this file wins.** Change it only by explicit human direction.

## Project non-negotiables

> Write this section from the human's answers at setup, one bullet per hard limit: the thing that must not happen, and who can authorize an exception. Ask at least about the stack and whether it may change, what the agents may never touch, where work may run, and what data is off limits. Write only the limits the human actually gave you. Do not invent a limit and do not leave a placeholder standing; every agent loads this file first and treats what it finds here as fact. If the project has no limits beyond the gates below, delete this section and say so in your setup report. Delete this prompt when you are done.

## Gates (keep these)

- **No secrets in code or commits.** Ever.
- **No force-push** without explicit per-push human permission.
- **Single-writer.** Every canonical file has exactly one authorized writer, or a declared row-partition where the file's own header says who writes which rows; all other agents are read-only on it.
- **Repo single-writer, under audit.** If the project has a code repo, exactly one seat writes it; every other member is read-only on it.
- **Independent gate before merge.** No author merges its own work. An independent seat (`members/gate.md`) reviews the diff it did not write, **re-runs the suites itself** (never the reported numbers on faith), and lands it on the human's go.
- **Verify before you ship.** A passing report you did not run yourself is an *unverified* state. Confirm green firsthand; in a known-flake lane, hammer it rather than sampling twice; **CI-green is not deploy-works**: smoke the deployed artifact before calling it a candidate.
- **No autonomous shipping.** Commits, deploys, sends, promotions to production, money movement, and trades require explicit human approval each time. **The human is the commit/merge/deploy gate.**

Precedence: **constraints > member identity > mode > core baseline.**

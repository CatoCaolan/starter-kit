# Constraints: hard limits (top precedence, never overridden)

**Loaded first by every agent, in every mode. When any module conflicts with this file, this file wins.** Change it only by explicit human direction.

> This is a template. Replace the example *project* bullets with your real non-negotiables.

## Project non-negotiables (replace these)

- **Stack is fixed.** [e.g. Expo + Netlify + Supabase]. No new infrastructure without human approval.
- **No production access.** All work runs on dev. Changes reach production only when a human promotes them.
- **No secrets in code or commits.** Ever.
- **No force-push** without explicit per-push human permission.

## Gates (keep these)

- **Single-writer.** Every canonical file has exactly one authorized writer, or a declared row-partition where the file's own header says who writes which rows; all other agents are read-only on it.
- **Repo single-writer, under audit.** Only the build guild (`forge/`) writes the code repo; every other member is read-only on it. Builders build; everyone else reads.
- **Independent gate before merge.** No author merges its own work. An independent seat (`members/gate.md`) reviews the diff it did not write, **re-runs the suites itself** (never the reported numbers on faith), and lands it on the human's go.
- **Verify before you ship.** A passing report you did not run yourself is an *unverified* state. Confirm green firsthand; in a known-flake lane, hammer it rather than sampling twice; **CI-green is not deploy-works**: smoke the deployed artifact before calling it a candidate.
- **No autonomous shipping.** Commits, deploys, sends, money movement, and trades require explicit human approval each time. **The human is the commit/merge/deploy gate.**

Precedence: **constraints > member identity > mode > core baseline.**

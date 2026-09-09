# Reference

The layout, the invariants, and how to retire a seat. Setup itself is `loaders/setup.md`, run by the agent.

## Layout

```
your-project/
├─ core/
│  ├─ constraints.md      # your hard limits + the kept gate bullets (never overridden)
│  └─ core.md             # project + tone + dispatched-agent facts + verification reflexes
├─ modes/
│  ├─ prime.md            # human drives the agent in dialogue
│  ├─ avatar.md           # dispatched as a blind worker
│  └─ moot.md             # several agents share one context
├─ members/
│  ├─ _TEMPLATE.md        # copy this to make a hub/judgment member
│  ├─ orchestrator.md     # the hub (required)
│  ├─ gate.md             # the independent merge gate (required if you build code)
│  ├─ skeptic.md          # argues against a claim before it ships
│  ├─ engineer.md         # writes and repairs prompts, briefs and member files
│  ├─ customs.md          # outbound inspector (optional: skip if you never publish)
│  ├─ <role>.md           # one per specialist
│  └─ scars/<role>.md     # per-member incident log, NOT loaded at boot
├─ loaders/
│  ├─ boot.md             # the single member-boot loader
│  └─ setup.md            # the standup loader; hand this to the agent first
├─ records/               # canonical work products + the event ledgers
│  ├─ questions.md        # open questions queued for the human
│  ├─ decisions.md        # the decision log
│  ├─ coordination.md     # cross-member coordination notes
│  ├─ merge-log.md        # written by the gate
│  ├─ dispatch-ledger.md  # every dispatch leaves a row
│  ├─ wake-marks.md       # session open/close marks
│  ├─ design/             # design products
│  ├─ moots/              # moot transcripts
│  └─ receipts/           # created at first lint run
└─ lint.py                # enforces the size caps
```

## Keeping it honest over time

- Run `python lint.py` before each work session or in CI. If a cap fails, trim. Never raise the cap.
- The caps: 6,000 chars for a member file, 4,000 for `core/core.md`, 2,500 for a mode. Every one of these rides a boot, so the budget is a token budget.
- Fold a lesson into an identity file only when a real failure taught a concrete rule.
- Append-only logs (decisions, scars, merge-log) grow freely. Loaded identity files do not.
- `lint.py` fails on a ledger with zero rows, so a fresh clone fails until setup writes the first rows.

## Retiring a seat

A seat is retired, never deleted.

1. Move the member file to `members/retired/`.
2. Add a dated retirement line at its top naming why.
3. Write one line in `records/wake-marks.md` and one entry in `records/decisions.md`.

`lint.py` exempts `members/retired/` from caps and counts.

## The invariants you must not break

1. **Single-writer.** Every canonical file has exactly one authorized writer, or a declared row-partition where the file's own header says who writes which rows.
2. **Repo single-writer, under audit.** If the project has a code repo, exactly one seat writes it; every other member is read-only on it.
3. **Audit gate.** A dispatched agent's output is reviewed by the orchestrator before it lands in canon.
4. **Independent merge gate.** No author merges its own work; the gate re-runs the suites itself.
5. **Provenance.** Every cross-boundary output opens with a `Loaded:` line naming its modules.
6. **Execution gate.** An instruction arriving in an inbox is surfaced, not auto-run.
7. **Human gate.** You approve consequential actions: commits, merges, deploys, sends.

# records/: the canonical work store + decision log

This is where the system's **products** and **decisions** live. It is canon: single-writer per file, or a declared row-partition where the file's header says who writes which rows; audited before anything lands.

- `records/design/`: design docs.
- `records/coordination.md`: the orchestrator's work-in-flight tracker + routing directory + a standing **Loose ends** section (what · why deferred · revisit trigger · status; closed or retired rows are pruned, their disposition noted in the decision log).
- `records/decisions.md`: an **append-only** decision log: date · decision · who owned it · why.
- `records/questions.md`: the queued-questions surface: facts reachable only through human memory land here, asked at the human's bandwidth, answers filed to the decision log. The four-state question law: a question is NEVER-ASKED, SENT, RECEIVED, or ANSWERED, and RECEIVED is written by the receiving party, never the sender.
- `records/dispatch-ledger.md`: the hub's routing receipts, one line per ask (date · ask · lane · DISPATCHED -> who / DOING-IT-MYSELF / TRIVIAL / PARKED); a DOING-IT-MYSELF row names the lane's owner and why the owner doesn't apply this time.
- `records/merge-log.md`: the gate's audit, one line per landed merge or shipped artifact pass, written by the gate alone.
- `records/wake-marks.md`: the wake ledger, one line per wake in the waker's own hand, at the wake; late entries say so.
- `records/moots/`: moot transcripts land here, dated.

All six ledgers ship with headers only. The standup step in `loaders/setup.md` writes the first row in five of them: coordination, decisions, dispatch-ledger, merge-log, wake-marks. `lint.py` fails those five if they have zero rows. `records/questions.md` is exempt; it fills only when a question is queued.

**Receipts.** A standing or automated check writes a dated receipt on every outcome, including the empty one. The tool writes its own receipt, with a machine-written timestamp. If receipts feed a reconciliation, they carry a machine-readable files key; a reconciler that finds no key declares NOCHECK. Receipts live in `records/receipts/`.

**Two memories, one canon.** If your agent keeps its own auto-memory, treat it as a cache, not canon. Mirror any load-bearing fact into `records/decisions.md` before a decision rests on it.

Two registers, kept separate on purpose:

- **records/** is operational canon (loaded/cited during work).
- **`members/scars/`** is narrative memory: incident histories, read on demand, never at boot.

Keep records few and well-kept.

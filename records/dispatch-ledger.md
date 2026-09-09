# Dispatch ledger (the hub's routing receipts)

*Single-writer: the orchestrator. The row is written BEFORE the worker is dispatched, not after it reports: a ledger filled in at the close only ever records the runs that survived. Row shape: date · the ask (short) · lane (member, or NONE) · disposition. Dispositions: DISPATCHED -> who · DOING-IT-MYSELF (owner named + why not this time) · TRIVIAL · PARKED.*

A dispatch made from an engineer-written brief names that brief in its row, so a run that went wrong is traceable to the text it ran under.

A DOING-IT-MYSELF row must name the lane's owner AND say why the owner doesn't apply this time. 'Faster myself,' 'it's small,' and 'I already know the answer' are the drift itself wearing a reason's clothes; the roster exists BECAUSE the hub's certainty is its blind spot. DOING-IT-MYSELF rows are allowed, expected, and often right: the ledger doesn't punish the choice; it refuses to let it go unmade, or unseen.

Why the ledger pairs with a reply-surface line: a log can quietly stop being written (silence looks like health); a line printed before the answer can do neither. This file is the memory; the line is the instrument.

## Ledger

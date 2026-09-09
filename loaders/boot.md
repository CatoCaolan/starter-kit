# Loader · Boot a member (parameterized)

The single boot path for a **member**. Hand this to a fresh instance with two parameters.

**Parameters:**
- `{MEMBER}`: a file in `members/` (e.g. `members/orchestrator.md`).
- `{MODE}`: one of `modes/prime.md` (human-driven), `modes/avatar.md` (dispatched worker), `modes/moot.md` (shared-context, multiple members), `modes/low-energy.md` (a softened session overlay, any member).

**Read, in order:**
1. `core/constraints.md`: hard limits, top precedence, never overridden
2. `core/core.md`: project + tone + dispatched-agent facts + earned verification reflexes
3. `{MEMBER}`: this member's identity (behavior only; its scars file is read on demand, not now)
4. `{MODE}`: behavior for how it's running

Then state, in one line, who you are and what you own (`Loaded:` naming the four files), and begin. Then append your wake line to `records/wake-marks.md` (date, seat, mode, one line): a wake that leaves no mark is indistinguishable from one that never happened. Read only the files listed. Do not read the member's scars log unless the task needs the history.

> Precedence on conflict: constraints > member identity > mode > core baseline. In a guild dispatch, the guild's law file occupies the member-identity slot of this chain.

## The two guilds have their own loaders (not this one)

- **The Pack** (read-only scouts, the brains): dispatch via `pack/loader-pack.md`. Six roles; analyze and verify, never execute.
- **The Forge** (build masters, the hands): dispatch via `forge/loader-forge.md`. Writes code under audit.
- **The gate** (`members/gate.md`) is a normal member booted by this loader, but it is the one seat that reviews work it did not author and lands a merge on the human's go.

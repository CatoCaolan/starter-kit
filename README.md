# Orchestration Starter Kit

A portable multi-agent orchestration layer: a roster of specialized agents composed from small text modules at load time, coordinated by one accountable hub, with an independent review gate, and you as the final gate.

## Setup

1. Clone or download this folder.
2. Start an agent session in it.
3. Tell the agent: **"Read `loaders/setup.md` and follow it."**

The agent interviews you, fills in the project files, builds your roster, and stops for your approval.

## Requirements

- An agent with file read and write tools, pointed at this directory.
- That agent must be able to dispatch sub-agents. `modes/avatar.md` relies on it.
- Python 3.8 or later, used only by `lint.py`.

## What you get

- Agents built from small files: constraints + core + one identity + one mode. Swap a module, get a different agent.
- `lint.py` fails if an identity file exceeds its size cap.
- A separate seat that reviews and merges. No author merges its own work.
- Every wake, dispatch, question, and merge leaves a row in `records/`.
- You approve every commit, merge, deploy, and send.

## The mental model

```
              you (the final gate)
                        │
                 ┌──────────────┐
                 │ ORCHESTRATOR │   ← the one hub; decomposes, dispatches, audits
                 └──────────────┘
            ┌───────────┼───────────┐
         member      member      member   ← the judgment seats you define
            └───────────┼───────────┘
                        │
                      GATE   ← independent: reviews what it did NOT author,
                               then lands it on your go
```

## When to use the heavy machinery

Use a full member and the gate when the work needs judgment and being wrong is expensive. For cheap lookups, just ask the agent. Unused roles cost nothing.

## Reference

- `REFERENCE.md`: the directory layout, the invariants, and how to retire a seat.
- `core/` and `members/_TEMPLATE.md`: the composition model.
- `loaders/boot.md`: how a work session boots a member.

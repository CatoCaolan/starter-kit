# Decisions (the append-only decision log)

*Single-writer: the orchestrator. One entry per decision: date · decision · owner · why. Append-only: a correction is a new entry naming what it supersedes, never an edit to an old one.*

## Log

# Loader · Setup (stand the kit up for a project)

Run this standup interactively. Interview the human, read their answers back before writing anything, fill the project files, build the roster, create the missing directories, write the first ledger rows, run the linter, then stop for approval.

Do not skip the interview. Do not invent project facts. Do not commit; the human is the commit gate.

## 1. Orient

Read `core/constraints.md`, `core/core.md`, and `members/_TEMPLATE.md`. That is enough to run setup. `REFERENCE.md` holds the layout and the invariants if you need them.

## 2. Interview the human

Ask these. Do not guess an answer, and do not proceed on a blank.

1. Project name, and a one-paragraph purpose.
2. Stack and languages, and any hard constraints (security, no production access, and the like).
3. Do you build code in this project? If yes: the repo path, the test command, and the branch merges land on.
4. Do you publish or send anything outbound? (Decides whether `members/customs.md` is kept.)
5. The specialist roles you want, one member each, by name and a one-line scope.

Then, for **each** specialist named in question 5, ask four follow-ups. A one-line scope cannot fill a member file, and a member file with invented scope edges is worse than no member.

- What files or areas does this seat own outright, that nobody else may write?
- What is explicitly **not** theirs, that they should route elsewhere?
- When this seat has to make a judgment call, what is it optimizing for?
- Who do they hand work to, and who hands work to them?

## 3. Read it back

Summarize every answer in a short list and ask the human to confirm or correct it. Write nothing until they confirm.

## 4. Stand it up

1. **`core/constraints.md`**: write the project's non-negotiables. Keep the gate bullets (single-writer; repo single-writer under audit; independent gate before merge; verify before ship; human gate) unless the human overrides them.
2. **`core/core.md`**: one paragraph on what the project is, and its tone floor. Leave the verification reflexes in place; they are project-agnostic.
3. **Roster**: copy `members/_TEMPLATE.md` once per specialist, filling all five fields from the follow-up answers. Keep each under the cap. Incident history goes to `members/scars/<role>.md`, never the loaded file.
4. **If building code**: set the real architectural invariants in `forge/hands.md` section 3, copy `forge/masters/_TEMPLATE.md` once per tech tier, and keep `members/gate.md`. Record the repo path, test command, and target branch where the dispatch loaders can reach them. If not building code, leave `members/forge.md`, `members/gate.md` and `forge/` in place and unused. Other files cite them; deleting them breaks those references.
5. **If never publishing outbound**: leave `members/customs.md` in place and unused.
6. **Directories**: create `records/design/` and `records/moots/`. Other files reference both; neither ships.
7. **First ledger rows**: write one row, dated today, in each of `records/wake-marks.md`, `records/decisions.md`, `records/dispatch-ledger.md`, `records/merge-log.md`, `records/coordination.md`.

## 5. Lint

Run `python lint.py` (try `python3` if that fails).

A fresh clone fails this check with five empty-ledger errors. That is expected and step 4.7 clears it. If a size cap fails, trim the file. Never raise the cap. Report the linter's output and the receipt path it wrote.

## 6. Stop for approval

Report what you wrote in each file, the roster you built, the directories you created, and the linter result. Then stop. Do not begin project work and do not commit until the human approves.

Tell the human this, in your own words: from here on, a work session starts by handing you `loaders/boot.md` with two parameters, which member and which mode. Scouts dispatch with `pack/loader-pack.md`, build masters with `forge/loader-forge.md`.

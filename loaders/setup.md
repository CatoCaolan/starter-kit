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
4. Do you publish anything outbound, or take in material from outside the project? (Decides whether `members/customs.md` is wired into the flow or left dormant.)
5. Will you be writing prompts, dispatch briefs, or new member files as you go? (Decides whether `members/engineer.md` is wired into the flow or left dormant.)
6. The specialist roles you want, one member each, by name and a one-line scope.

Then, for **each** specialist named in question 6, ask five follow-ups. A one-line scope cannot fill a member file, and a member file with invented scope edges is worse than no member.

- What files or areas does this seat own outright, that nobody else may write?
- What is explicitly **not** theirs, that they should route elsewhere?
- When this seat has to make a judgment call, what is it optimizing for?
- Who do they hand work to, and who hands work to them?
- When this seat is dispatched as a blind worker, what does the dispatch have to carry that it cannot work out for itself?

## 3. Read it back

Summarize every answer in a short list and ask the human to confirm or correct it. Write nothing until they confirm.

## 4. Stand it up

1. **`core/constraints.md`**: write the project non-negotiables from the interview answers, and delete the prompt block. Write only limits the human actually gave you; leave no placeholder standing. Keep every bullet under Gates unless the human overrides one.
2. **`core/core.md`**: one paragraph on what the project is, and its tone floor. Leave the verification reflexes in place; they are project-agnostic.
3. **Roster**: copy `members/_TEMPLATE.md` once per specialist, filling all five fields from the follow-up answers. Keep each under the cap. Incident history goes to `members/scars/<role>.md`, never the loaded file.
4. **If building code**: record the repo path, test command, and target branch in `core/core.md` so every seat can reach them, and keep `members/gate.md` as the seat that reviews and lands work it did not author.
5. **Dormant seats**: a seat the human does not need stays in place and unused; other files cite it and deleting it breaks those references. Say in your setup report which seats are dormant. If the engineer is dormant, the human is the writer of `members/*.md`.
6. **Directories**: create `records/design/`, `records/moots/` and `members/scars/`. Other files reference all three; none ships.
7. **First ledger rows**: write one row, dated today, in `records/wake-marks.md`, `records/decisions.md` and `records/coordination.md`, recording the standup itself. `records/dispatch-ledger.md` and `records/merge-log.md` get their first row from the seat that owns them, on its first dispatch or merge; write a dated `setup, no rows yet` line in each so the linter passes and the ledger is not silently empty.

## 5. Lint

Run `python lint.py` (try `python3` if that fails).

A fresh clone fails this check with five empty-ledger errors. That is expected and step 4.7 clears it. If a size cap fails, trim the file. Never raise the cap. Report the linter's output and the receipt path it wrote.

## 6. Stop for approval

Report what you wrote in each file, the roster you built, the directories you created, and the linter result. Then stop. Do not begin project work and do not commit until the human approves.

Tell the human this, in your own words: from here on, a work session starts by handing you `loaders/boot.md` with two parameters, which member and which mode.

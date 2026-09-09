#!/usr/bin/env python3
# kit-version: 1.0.0
"""
lint.py - enforce the orchestration kit's invariants mechanically.

Identity files must stay small: every one of them rides every boot, so the
size budget is a build failure rather than an intention.

Checks: per-file size caps, every member declares its single writer, the
records organ exists, no ledger has zero rows, a cap-margin advisory at 90%,
record-age and retired-roster advisories, a worst-case boot estimate, and a
receipt line written per run.
"""
import os, sys, glob, argparse, re, json
from datetime import date, datetime

DEFAULTS = dict(cap=6000, core_cap=4000, mode_cap=2500)

def chars(path):
    with open(path, encoding="utf-8") as f:
        return len(f.read())

def main():
    # Self-defending output: no `python -X utf8` flag required on legacy consoles.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--cap", type=int, default=DEFAULTS["cap"],
                    help="char cap for a loaded member identity file")
    args = ap.parse_args()
    root = args.root
    problems, notes, checked = [], [], 0
    capped = []  # (relpath, chars, cap) for every cap-checked file, for the margin advisory

    def rel(p):
        return os.path.relpath(p, root).replace(os.sep, "/")

    def members():
        # members/retired/*.md sits below this glob on purpose: retired member
        # files are exempt from the cap check and the owns check.
        return [p for p in glob.glob(os.path.join(root, "members", "*.md"))
                if not os.path.basename(p).startswith("_")]

    # 1. Member identity files are capped. Scars files are exempt (lazy-loaded).
    for p in members():
        checked += 1
        n = chars(p)
        capped.append((rel(p), n, args.cap))
        if n > args.cap:
            problems.append(f"OVER CAP  {rel(p)}: {n} chars "
                            f"(cap {args.cap}). Move history/lore to members/scars/.")

    # 2. Core + modes have their own tighter budgets: they ride EVERY boot.
    for sub, cap in (("core", DEFAULTS["core_cap"]), ("modes", DEFAULTS["mode_cap"])):
        for p in glob.glob(os.path.join(root, sub, "*.md")):
            checked += 1
            n = chars(p)
            capped.append((rel(p), n, cap))
            if n > cap:
                problems.append(f"OVER CAP  {rel(p)}: {n} chars (cap {cap}).")

    # 4. Cap-margin advisory (never fails): name any capped file at 90% or more
    #    of its budget, so a file nearing its cap is visible before it breaks.
    for r, n, cap in capped:
        if cap and n >= 0.9 * cap:
            notes.append(f"cap margin: {r} at {n}/{cap} chars "
                         f"({100 * n // cap}% of cap).")

    # 5. Every member needs a single-writer 'Owns' line (single-writer invariant).
    for p in members():
        with open(p, encoding="utf-8") as f:
            body = f.read().lower()
        if "owns (single-writer)" not in body:
            problems.append(f"NO OWNER  {rel(p)}: "
                            f"missing an 'Owns (single-writer)' declaration.")

    # 6. The records organ: these six files must exist.
    for r in ("records/wake-marks.md", "records/decisions.md",
              "records/dispatch-ledger.md", "records/merge-log.md",
              "records/questions.md", "records/coordination.md"):
        p = os.path.join(root, *r.split("/"))
        if os.path.exists(p):
            checked += 1
        else:
            problems.append(f"MISSING ORGAN  {r}: a 1.0.0 tree carries the records "
                            f"organ. Fix: create the missing records file.")

    # 6b. The zero-rows check: the ledgers ship EMPTY (headers only); setup's
    #     first-rows step writes each ledger's first row, so this check is what
    #     makes that step mechanically non-optional. A ledger that exists with
    #     no data row at all fails. A data row is an ISO-dated line (bulleted
    #     or bare) or a table data row past the header/divider.
    divider = re.compile(r"^\s*\|[\s\-:|]*$")
    date_row = re.compile(r"^(?:-\s*)?\d{4}-\d{2}-\d{2}")
    for r in ("records/wake-marks.md", "records/dispatch-ledger.md",
              "records/decisions.md", "records/merge-log.md",
              "records/coordination.md"):
        p = os.path.join(root, *r.split("/"))
        if not os.path.exists(p):
            continue  # already a MISSING ORGAN failure above
        with open(p, encoding="utf-8") as f:
            lines = f.read().splitlines()
        table_rows = [ln for ln in lines
                      if ln.lstrip().startswith("|") and not divider.match(ln)]
        has_row = (any(date_row.match(ln) for ln in lines)
                   or len(table_rows) > 1)  # a header line, plus a data row
        if not has_row:
            problems.append(f"EMPTY LEDGER  {r}: ledger has zero rows. Either "
                            f"setup was never run, or the first rows were "
                            f"deleted. This check cannot tell which; git "
                            f"history can. If the install is not under version "
                            f"control, it cannot tell either.")

    # 7. Advisory (never fails): the scars files are unbounded by design.
    shelf = 0
    for d in (os.path.join(root, "members", "scars"),):
        shelf += sum(chars(p) for p in glob.glob(os.path.join(d, "*.md")))
    if shelf:
        notes.append(f"scars shelf ≈ {shelf} chars across the read-on-demand files "
                     f"(unbounded by design; just keep an eye on it).")

    # 8. Advisories (never fail): how stale are the living records? ISO dates
    #    sort lexically, so the max IS the latest row. Rows live at line start,
    #    bare or bulleted (the log ledgers), or as the first cell of a table
    #    row (wake-marks). And if a retired roster exists, keep its size visible too.
    def last_iso_date(path):
        with open(path, encoding="utf-8") as f:
            body = f.read()
        dates = re.findall(r"(?m)^(?:-\s*)?(\d{4}-\d{2}-\d{2})", body)
        dates += re.findall(r"(?m)^\|\s*(\d{4}-\d{2}-\d{2})", body)
        return max(dates) if dates else None
    for r, label in (("records/dispatch-ledger.md", "dispatch-ledger"),
                     ("records/wake-marks.md", "wake-marks")):
        p = os.path.join(root, *r.split("/"))
        if os.path.exists(p):
            last = last_iso_date(p)
            if last:
                age = (date.today() - date.fromisoformat(last)).days
                notes.append(f"{label} last row {last}, {age} day(s) old "
                             f"(MEASURED from the file).")
            else:
                notes.append(f"{label}: no ISO-dated rows found "
                             f"(MEASURED from the file).")
    retired_dir = os.path.join(root, "members", "retired")
    if os.path.isdir(retired_dir):
        retired = glob.glob(os.path.join(retired_dir, "*.md"))
        notes.append(f"members/retired/: {len(retired)} retired member file(s) "
                     f"(exempt from the cap and owns checks).")

    # 9. Estimate the worst-case boot cost so the number is always visible.
    def biggest(sub, exclude=()):
        files = [p for p in glob.glob(os.path.join(root, sub, "*.md"))
                 if not os.path.basename(p).startswith("_")
                 and os.path.basename(p) not in exclude]
        return max((chars(p) for p in files), default=0)
    cpath = os.path.join(root, "core", "constraints.md")
    worst = (chars(cpath) if os.path.exists(cpath) else 0)
    # constraints.md is added separately above, so it must not also ride the
    # core max.
    worst += biggest("core", exclude=("constraints.md",)) + biggest("members") + biggest("modes")
    print(f"checked {checked} files · worst-case boot = {worst} chars "
          f"(ESTIMATED ~{worst//4} tokens, the chars/4 heuristic, not measured)")
    for n in notes:
        print("  note: " + n)

    # 10. The receipts law's live demonstration: every run appends its own
    #     receipt line, naming the files it actually checked. A failed write
    #     warns and never alters the lint verdict.
    verdict = "FAIL" if problems else "OK"
    receipt_rel = "records/receipts/lint.jsonl"
    try:
        rpath = os.path.join(root, *receipt_rel.split("/"))
        os.makedirs(os.path.dirname(rpath), exist_ok=True)
        receipt = {"ts": datetime.now().astimezone().isoformat(timespec="seconds"),
                   "tool": "lint", "verdict": verdict, "checked": checked,
                   "worst_case_chars": worst,
                   "files": [r for r, _n, _cap in capped]}
        with open(rpath, "a", encoding="utf-8") as f:
            f.write(json.dumps(receipt) + "\n")
    except Exception as e:
        print(f"  warning: receipt write to {receipt_rel} failed ({e}); "
              f"verdict unaffected.")

    if problems:
        print("\nFAIL:")
        for p in problems:
            print("  - " + p)
        sys.exit(1)
    print("OK: all identity files within budget; single-writer declared.")
    sys.exit(0)

if __name__ == "__main__":
    main()

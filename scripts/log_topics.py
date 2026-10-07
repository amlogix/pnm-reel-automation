#!/usr/bin/env python3
"""
Topic logging. Two files, two jobs.

  rejected-topics.csv : EVERY topic generated. Written immediately on each run.
  content-log.csv     : only topics SELECTED for production.

On selection, the row moves from rejected to content-log. That is what stops an
unselected topic from resurfacing in a later session.

  python log_topics.py reject --topic-hi "..." --hook-hi "..." --formula ... --category ... --type ...
  python log_topics.py select --topic-hi "..."
"""
import sys as _sys
for _s in (_sys.stdout, _sys.stderr):  # Windows consoles default to cp1252; output is Devanagari
    _s.reconfigure(encoding="utf-8")
import csv, sys, argparse
from pathlib import Path
from datetime import date

DATA = Path(__file__).parent.parent / "data"
REJ  = DATA / "rejected-topics.csv"
LOG  = DATA / "content-log.csv"

REJ_FIELDS = ["date_generated","topic_hi","hook_hi","formula","category",
              "reel_type","service_page","reason"]
LOG_FIELDS = ["date","reel_id","topic_hi","hook_hi","formula","format","service_page",
              "status","views","sends","saves","avg_watch_sec","notes"]

def append(path, fields, row):
    new = not path.exists() or path.stat().st_size == 0
    with open(path, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        if new: w.writeheader()
        w.writerow({f: row.get(f, "") for f in fields})

def read_all(path, fields):
    if not path.exists(): return []
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))

def rewrite(path, fields, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows: w.writerow({f: r.get(f, "") for f in fields})

def main():
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=["reject","select","list"])
    for f in set(REJ_FIELDS + LOG_FIELDS):
        p.add_argument(f"--{f.replace('_','-')}", default="")
    a = vars(p.parse_args())

    if a["action"] == "reject":
        a["date_generated"] = a["date_generated"] or date.today().isoformat()
        append(REJ, REJ_FIELDS, a)
        print(f"rejected pool += {a['topic_hi']}")

    elif a["action"] == "select":
        if not a["topic_hi"]: sys.exit("--topic-hi required")
        rows = read_all(REJ, REJ_FIELDS)
        match = next((r for r in rows if r["topic_hi"] == a["topic_hi"]), None)
        if match:
            rewrite(REJ, REJ_FIELDS, [r for r in rows if r["topic_hi"] != a["topic_hi"]])
            for k in ("hook_hi","formula","service_page"):
                a[k] = a[k] or match.get(k,"")
            a["format"] = a["format"] or match.get("reel_type","")
        a["date"] = a["date"] or date.today().isoformat()
        a["status"] = a["status"] or "selected"
        append(LOG, LOG_FIELDS, a)
        print(f"selected -> content log: {a['topic_hi']}")

    else:
        print(f"rejected pool: {len(read_all(REJ, REJ_FIELDS))}")
        print(f"content log  : {len(read_all(LOG, LOG_FIELDS))}")

if __name__ == "__main__":
    main()

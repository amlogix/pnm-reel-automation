---
description: Generate 5 reel topics (Mode 1 of the pnm-reels engine)
argument-hint: [optional focus, e.g. "Navratri" or "shradh"]
---

Run **Mode 1 — Topic Generation** from the `pnm-reels` skill (`.claude/skills/pnm-reels/SKILL.md`).

Optional focus from the user: $ARGUMENTS

Follow the skill exactly: establish today's date, read `data/festival-calendar.csv` (verified rows only, never calculate a date), scan trends, read BOTH `data/content-log.csv` and `data/rejected-topics.csv` before generating, then offer exactly 5 topics in the specified format.

Immediately append all 5 to `data/rejected-topics.csv` (use `python scripts/log_topics.py reject ...`), then stop and wait for an explicit pick. Do not produce a package.

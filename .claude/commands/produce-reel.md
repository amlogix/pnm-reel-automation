---
description: Produce a full reel package for a picked topic (Mode 2 of the pnm-reels engine)
argument-hint: <topic number from the last plan, or topic text>
---

Run **Mode 2 — Produce** from the `pnm-reels` skill (`.claude/skills/pnm-reels/SKILL.md`).

Picked topic: $ARGUMENTS

If no topic was picked or it is ambiguous, ask — never produce without an explicit pick.

1. Move the picked row to the content log: `python scripts/log_topics.py select --topic-hi "..." --reel-id PNM-[NNN]`
2. Run the Generatability Test and classify every object Tier 1 / 2 / 3.
3. Check each claim with `python scripts/check_claim.py "<claim>"`. Cached → use the verified wording. Not cached → mark `[VERIFY]`, leave it empty, add a pending row. Never fill a religious fact yourself.
4. Write the package to `outputs/reels/PNM-[NNN]-[slug].md` (never in chat), with every section the skill lists, ending in a log row.

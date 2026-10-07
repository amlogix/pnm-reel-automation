# PNM REELS ENGINE

Portable content engine for Pandits Near Me Instagram reels.
Clone anywhere, add `.env`, run.

---

## SETUP — 3 STEPS, ANY MACHINE

```bash
git clone <your-repo> pnm-engine && cd pnm-engine
cp .env.example .env        # fill in your keys
pip install -r requirements.txt
```

Then open the folder in **Claude Code** (desktop app or terminal). It reads `CLAUDE.md` automatically.

Nothing is machine-specific. No absolute paths. Moving machines = clone + `.env`.

---

## STRUCTURE

```
pnm-engine/
├── CLAUDE.md               # project instructions — Claude reads this first
├── .env                    # your keys (gitignored)
├── .env.example            # template
│
├── .claude/
│   ├── settings.json       # shared permissions
│   ├── commands/           # /plan-reels  /produce-reel  /check-claim
│   └── skills/pnm-reels/   # THE LOGIC — rarely changes (auto-discovered)
│       ├── SKILL.md        # 3 modes: Plan, Produce, Story
│       └── references/     # formats, hooks, brand bible, protocols
│
├── data/                   # THE STATE — changes constantly, WRITABLE
│   ├── content-log.csv     # SELECTED topics only
│   ├── rejected-topics.csv # every topic offered but not picked
│   ├── verified-claims.csv # claim cache → verification that scales
│   ├── festival-calendar.csv
│   └── instagram-hooks.md  # competitor hooks, auto-refreshed
│
├── scripts/
│   ├── log_topics.py       # reject pool + selection → content log
│   ├── check_claim.py      # is this claim already verified?
│   ├── fetch_competitors.py# Apify → instagram-hooks.md
│   └── render_narration.py # ElevenLabs → mp3 + exact duration
│
├── outputs/reels/          # generated packages
├── assets/characters/      # locked character reference sheets
└── assets/references/      # competitor clips for analysis
```

**The split that matters:** `.claude/skills/` is logic and barely changes. `data/` is state and changes every week. Never write into `.claude/` during a run.

---

## DAILY USE

| Task | Command |
|---|---|
| Plan a month | `/plan-reels` (or just say "PNM reel") |
| Produce a picked topic | `/produce-reel 2` |
| Check a claim before writing | `/check-claim अखंड ज्योत` |
| Render narration + measure | `python scripts/render_narration.py script.txt out.mp3` |
| Pool a generated topic | `python scripts/log_topics.py reject --topic-hi "..." --hook-hi "..."` |
| Select one for production | `python scripts/log_topics.py select --topic-hi "..." --reel-id PNM-005` |
| Refresh competitor hooks | `python scripts/fetch_competitors.py` |

---

## WHAT IS AUTOMATED

✅ Topic generation, de-duplication, trend scan
✅ Scripts, shot prompts, narration text, edit sheets
✅ Competitor hook ingestion
✅ Narration rendering + exact duration measurement
✅ Content log writes

## WHAT IS NOT

❌ Video generation — hands-on by design, and no model is named anywhere
❌ Edit assembly — where your brand elements live
❌ Festival dates — read from a signed file, never calculated
❌ Novel religious claims — see below

---

## THE VERIFICATION CACHE

The gate does not fire per reel. It fires per **claim**, once.

```
New reel → check_claim.py
              ├── in cache  → use verified wording, reuse_count++
              └── not found → mark [VERIFY], add pending row
```

After ~50 reels the cache covers most of what you will ever say, and the gate rarely fires.

**Why dates and novel claims stay out of automation:** a single Navratri 2026 check returned **five different dates across nine sources**, with one site contradicting itself. That is not a training problem — the fact lives in a panchang, not in a model. Same for contested claims that vary by sampradaya.

Note that the market leader hedges every claim four times in a 65-second script. It is editorial policy, not a capability gap.

---

## MONTHLY RHYTHM

```
Week 1  python scripts/fetch_competitors.py     # refresh competitor hooks
        "PNM reel"                               # plan the month
        pick topics → produce packages

Week 1-4  produce → render narration → generate → edit → publish
          mark the content-log row as published after each publish

Day 7 after each publish:  add views / sends / saves to the log row
```

Annually: regenerate the calendar, get it signed.

---

## PORTABILITY CHECKLIST

```
[ ] .env filled, never committed
[ ] No absolute paths anywhere
[ ] requirements.txt current
[ ] data/ committed (it IS the state)
[ ] assets/characters/ committed — the locked cast must travel
[ ] Large video files gitignored
```

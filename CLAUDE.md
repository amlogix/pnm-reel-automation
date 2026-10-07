# PNM REELS ENGINE — PROJECT INSTRUCTIONS

Claude Code reads this on every session start. It governs how the engine runs here.

## WHAT THIS PROJECT IS

The content engine for Pandits Near Me's Instagram reels. Hindi devotional short-form video, 8 reels/month across three live formats.

## READ FIRST, EVERY SESSION

1. `.claude/skills/pnm-reels/SKILL.md` — the engine (also auto-loaded by Claude Code as a skill). Topic generation, produce, story mode.
2. `.claude/skills/pnm-reels/references/` — format library, hook formulas, brand bible, protocols.
3. `data/` — the live, **writable** state.

## THE CRITICAL DIFFERENCE FROM CLAUDE.AI

On claude.ai these files are static uploads. **Here they are writable.** That changes three things:

| File | Behaviour here |
|---|---|
| `data/content-log.csv` | **SELECTED topics only.** Append when a topic is picked. |
| `data/rejected-topics.csv` | **Every topic generated but not picked.** Append all 5 immediately on every run, so unselected topics never resurface. |
| `data/verified-claims.csv` | **Append after every pandit verification.** Claims verified once are reused forever. |
| `data/instagram-hooks.md` | Regenerated monthly by `scripts/fetch_competitors.py` |
| `data/festival-calendar.csv` | Regenerated annually by `scripts/refresh_calendar.py`, then signed |

**Always read these before generating. Always write to them after.** A Plan run that doesn't read the log is not de-duplicating.

## THE VERIFIED CLAIMS CACHE

Before marking anything `[VERIFY]`, **check `data/verified-claims.csv` first.**

- Claim already in the cache with matching scope → use the verified wording, increment `reuse_count`, do **not** raise a gate.
- Claim not in the cache → mark `[VERIFY]`, leave empty, add a pending row.

This is what makes verification scale. Each claim is checked once, not once per reel.

**Never write a value into `verified-claims.csv` that a human did not supply.** The cache is only trustworthy if nothing self-populates.

## WHAT IS NEVER AUTOMATED

These are not training gaps. They are facts that live outside the model.

- **Festival dates.** Read from `data/festival-calendar.csv`, verified rows only. Never calculate, never scrape, never average across sources. A single Navratri check returned five different dates across nine sources.
- **Novel religious claims.** Contested and regional. No ground truth to learn from.
- **Deity frames.** Second review pass, always.

## FILE CONVENTIONS

- Reel packages → `outputs/reels/PNM-[NNN]-[slug].md`
- **No tool or model is ever named in `.claude/skills/pnm-reels/references/`.** Models change; structure does not. The only fixed tool decision is ElevenLabs for narration.
- Character references → `assets/characters/[CHARACTER_ID]_[angle].png`
- Competitor reference clips → `assets/references/`
- Never write into `.claude/` during a run. The skill is logic; `data/` is state.

## SECRETS

All keys in `.env`, never committed. `.env.example` lists what is needed. Never print a key value into a file or a reel package.

## PORTABILITY

This project runs on any machine with: the repo cloned, `.env` filled, and `pip install -r requirements.txt`. No machine-specific paths anywhere.

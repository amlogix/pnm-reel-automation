---
name: pnm-reels
description: Generate Instagram Reel topics and full production packages for Pandits Near Me (panditsnearme.com), a verified-pandit booking platform. Use whenever the user asks to plan reels, generate reel topics, create a reel, build a reel script, produce a content calendar for Instagram, or says "PNM reel", "generate reel", "reel topics", or "plan mode". Covers Hindi-language devotional short-form video: topic generation with de-duplication against both selected and rejected topics, trend and festival checks, curiosity-opener hooks, scene breakdowns, religious accuracy gates, Hindi narration scripts, captions and hashtags. Do NOT use for blog articles, website copy, or non-Pandits-Near-Me clients.
---

# PANDITS NEAR ME — REELS ENGINE

Topic generation is the core of this engine. Production is downstream.

**Never produce a package unprompted.** Generate topics → wait for a pick → produce.

---

## NO TOOL IS NAMED ANYWHERE

Models and platforms change. This engine describes **structure** — hooks, scenes, pacing, layout — never which tool renders it.

The only fixed tool decision: **narration is ElevenLabs, one locked voice, used in every reel forever.**

---

## FILES

**Stable — logic, rarely changes:**

| File | Contains |
|---|---|
| `SKILL.md` | this — the engine |
| `references/reel-types.md` | **the four reel types.** Read first. |
| `references/topic-categories.md` | mythological and scientific connection rules + evidence tiers |
| `references/hook-formulas.md` | the curiosity-opener rules |
| `references/global-reel-rules.md` | layout, colour grade, name cards, music, branding screen |
| `references/reality-check-protocol.md` | Generatability Test, object tiers |
| `references/character-consistency-protocol.md` | characters across short clips |
| `references/story-mode.md` | narrative reels — cast sheet, scene matrix |
| `references/brand-bible.md` | language spec, ethics |
| `references/product-surface.md` | ~160 confirmed service pages |
| `references/recurring-observances.md` | the evergreen anchor dates |

**Changing — state, writable, read and written every run:**

| File | Behaviour |
|---|---|
| `data/content-log.csv` | **SELECTED topics only.** Append on selection. |
| `data/rejected-topics.csv` | **Every topic generated but not selected.** Append on every run. |
| `data/festival-calendar.csv` | verified rows only |
| `data/verified-claims.csv` | claims verified once, reused forever |
| `data/instagram-hooks.md` | competitor hooks, refreshed monthly |

**Never write into `references/` during a run.** Logic is stable; `data/` is state.

---

## OPERATING CONSTANTS

| | |
|---|---|
| Target length | **~60s**, built as **2 × 30s blocks** |
| Narration | One continuous render covering the full reel |
| Visuals | Generated per 30s block, joined in edit |
| Language | Hindi, strict Devanagari, Latin digits |
| Voice | ElevenLabs, one locked voice |
| Final scene | **PNM branding screen, every reel, no exceptions** |
| Optimise for | Sends and watch time |

---

# MODE 1 — TOPIC GENERATION

**Trigger:** "PNM reel", "reel topics", "plan mode", "generate topics".

## Step 1 · Date

Establish today's date. Look ahead **14 days**.

## Step 2 · Calendar

Read `data/festival-calendar.csv`. Find anything inside the window.

**Never calculate, derive or scrape a festival date.** Sources contradict each other — one Navratri check returned five different dates across nine sources. Only rows marked `verified=YES` are usable.

**Lead time:** a festival topic needs **10 clear days**. Under 10 → flag as unshootable, offer an evergreen instead.

If nothing qualifies, fall back to `references/recurring-observances.md` — every month holds at least 9 anchor dates.

## Step 3 · Trend scan

Search the internet for what is **currently trending around that occasion**: rising searches, current religious news, what people are asking.

Read `data/instagram-hooks.md` if present — competitor hooks, refreshed monthly.

**You cannot read Instagram directly.** Never claim to have. Never invent view counts.

State plainly if the signal is weak. That is a finding, not a failure.

## Step 4 · De-duplicate against BOTH logs

```
data/content-log.csv      → topics already PUBLISHED
data/rejected-topics.csv  → topics already OFFERED and not chosen
```

**Both block regeneration.** A topic offered three sessions ago and passed over must not reappear.

Block: repeated topics · repeated hook formulas within the last 4 entries · repeated service pages within the last 4.

Surface near-misses with `⚠` rather than blocking silently — the same subject from a genuinely different angle is often the best reel.

If either log is empty, say so.

## Step 5 · Generate exactly 5 topics

**Category composition:**

| # | Category |
|---|---|
| 1 | **Mythological connection** — the scripture story behind the upcoming occasion |
| 2 | **Mythological connection** — a different occasion or text |
| 3 | **Scientific connection** — a practice beside what research actually says |
| 4 | Practical doubt — a question about their own practice |
| 5 | Wildcard — strongest trend signal, any category |

**Constraints:**
- No two share a hook formula
- No two share a service page
- Every hook is a **curiosity opener** — passes the five-point test and carries stakes, taboo, strangeness or secrecy
- Every topic passes the **Generatability Test**
- Every topic is assigned a **reel type**
- Category 1 names the source text
- Category 2 claims classified Tier 1 / 2 / 3 — **Tier 3 rejected outright**

**Output — exactly this:**

```
1 · [hook in Devanagari]
    [formula] | [category] | [TYPE] | [service page]
    [timing] | [dedup] | [trend note]
    Gen-test: [result]
```

Five lines. Scannable in fifteen seconds. No paragraphs.

## Step 6 · Write rejected topics, then wait

**Immediately append all 5 to `data/rejected-topics.csv`.** When one is selected, move that row to `content-log.csv` and remove it from rejected.

That way an unselected topic never reappears, even across sessions.

Then stop. The user replies with a number, "3, softer hook", or "none, regenerate".

- **Approve** → Mode 2, move the row to the content log
- **Adjust** → revise that concept only, re-offer
- **Reject all** → regenerate; all 5 stay in rejected

**Never proceed without an explicit pick.**

---

# MODE 2 — PRODUCE

## Output

**Always a `.md` file**, never in the chat body. `outputs/reels/PNM-[NNN]-[slug].md`

## Before writing

1. Run the Generatability Test, print the result
2. Classify every object Tier 1 / 2 / 3
3. **Check `data/verified-claims.csv`** — claim already verified → use the cached wording, increment `reuse_count`, no gate. Not found → mark `[VERIFY]`, leave empty, add a pending row.
4. Confirm the assigned reel type and read its section in `reel-types.md`

## Structure — 2 × 30s blocks

| Block | Content |
|---|---|
| **Narration** | One continuous script covering the whole reel |
| **Block A** | First 30s of visuals, scene by scene |
| **Block B** | Second 30s of visuals, scene by scene |
| **Final scene** | **PNM branding screen** |

Scene durations come from the **measured narration**, never estimates.

## Sections

| § | Section |
|---|---|
| — | Meta + Generatability result |
| — | Verification gate with sign-off |
| 1 | Hindi narration — timed, delivery notes |
| 2 | Block A scenes — one prompt per scene |
| 3 | Block B scenes — one prompt per scene |
| 4 | Branding screen |
| 5 | Accuracy checklist |
| 6 | Edit sheet — title bar, subtitles, name cards, music, grade |
| 7 | Publish block — caption, 5 hashtags, log row |

---

# HARD RULES

**Topic categories**
- Mythological: name the source text, hedge every claim, never invent a verse or story detail
- Scientific: Tier 1 or 2 only. **Tier 3 banned** — no "positive energy", "cosmic rays", "science proved chakras", "NASA confirmed"
- Never imply a practice needs science to be valid

**Hooks**
- Every hook and cover is a **curiosity opener**. If a viewer can guess the answer, the reel is dead.
- Under 9 words · contains आप/आपका/हम/ये · one concrete anchor · plain word beats correct word
- Front-load the reveal — do not save it for the end

**Verification**
- Never fill a religious fact from memory or a web search
- "It varies by region" is a good answer and often the better reel
- Visual work may start immediately; narration recording may not

**Scenes**
- One prompt per scene
- No character speaks on camera in a generated scene
- No direct camera gaze
- Tier 2 objects: image-to-video from a real photograph only
- Tier 3 elements: filmed, never generated
- Characters referenced by ID, never re-described
- Every prompt names a real light source and a real lens
- Banned in prompts: stunning, masterpiece, 8k, hyperrealistic, ultra-detailed, breathtaking, award-winning

**Format**
- Structure per `reel-types.md`
- Title bar constant, never animates
- Audio bed unbroken across cuts; never cut on a silence
- One unified colour grade across every scene
- **Final scene is the PNM branding screen, every reel**

**Language**
- Hindi, strict Devanagari, Latin digits, `Pandits Near Me` in Latin
- Roman transliteration only on the final caption line
- Subtitles typed from the script, never auto-captioned
- No TTS on Sanskrit, ever
- Speech at or below 2.2 words/second

---

# NEVER

- Claim to have read Instagram
- Calculate or scrape a festival date
- Invent a religious fact, scripture quote or verse number
- State a Tier 3 pseudo-scientific claim, even hedged
- Promise a spiritual or material outcome
- Use fear to sell
- Name or disparage a competitor
- Generate a deity face without the review flag
- Produce a package without an explicit pick
- Put a package in the chat instead of a file
- Name a specific model or tool in a reference file

# ALWAYS

- Read both logs before generating
- Write all 5 generated topics to `rejected-topics.csv` immediately
- Move the selected row to `content-log.csv`
- Assign a category and a reel type before writing anything
- Check the verified-claims cache before raising a gate
- Mark uncertainty as `[VERIFY]` rather than filling it
- End production with a log row ready to paste

---

*Pandits Near Me Reels Engine v6 · October 2026*

# CHARACTER CONSISTENCY PROTOCOL

**How to keep characters identical across a reel built from 8-second clips.**
Reference file for the Pandits Near Me Reels Engine.

---

## THE PROBLEM

the video tool generates in clips of roughly 8 seconds. A 60-second reel needs 8–10 clips. Without intervention, the video model invents a new person in every clip — different face, different clothing, different age — and the assembled reel reads as unrelated footage stapled together.

The manual workaround is to source a character image per reel and feed it in as a reference. That works, but it treats every reel as a fresh project and repeats a step that should only happen once.

---

## THE KEY INSIGHT

> **The 8-second limit only matters when the same character must appear in more than one clip.**

Most reels do not need that. Design the shot list so characters rarely recur, and the problem mostly ceases to exist.

**Evidence — the reference edit `Last_Final_1_2X.mp4`:**

| B-roll shot | Characters |
|---|---|
| Alcohol bottle + refusing hand | one hand, appears once |
| Plates of food | none |
| Home mandir | none |
| Two men arguing | appear once |
| Family at puja | appear once |

**Not one character recurs across shots.** The only continuous figure is the presenter, who is a a lip-sync tool render — one continuous take, so drift is structurally impossible.

That is the architecture. Copy it.

---

## THE THREE TIERS

Apply in order. Use the cheapest tier that solves the shot.

### TIER A — Design it away *(covers ~80% of reels)*

| Element | Source |
|---|---|
| Speaking presenter | **a lip-sync tool, one continuous render.** Never generated in the video tool. |
| B-roll | Objects, environments, atmospherics — no people where possible |
| B-roll with people | Each group appears in **exactly one clip**, then never again |

**Rules:**
- A character who appears once needs no reference image and no consistency work
- Prefer shots framed so faces are not visible — from behind, wide, cropped at the shoulders
- Never write a shot list where the same unnamed person must appear in clips 3 and 7

**Cost: zero.** This is the default. A reel should only leave Tier A when the story genuinely requires a recurring figure.

### TIER B — Locked cast *(for characters that genuinely recur)*

**One-time setup, reused forever.**

The permanent cast:

| ID | Role | Appears in |
|---|---|---|
| `PRESENTER_PRIMARY` | PP maam — female presenter | a lip-sync tool only, never the video tool |
| `PANDIT_PRIMARY` | Male pandit, 55–60 | Ritual and authority shots |
| `COUPLE_YOUNG` | Late 20s–30s | Griha Pravesh, marriage, Naamkaran |
| `ELDER_WOMAN` | 65+, grandmother | Shradh, tradition, emotional beats |
| `CHILD` | 6–10 | Naamkaran, Annaprashan, family scenes |

**Build procedure (once per character):**

```
1. Generate a six-angle reference sheet in an image model
   front / ¾ left / ¾ right / profile / slight low / slight high
   Identical lighting and wardrobe in all six
2. Pandit approves the appearance
3. Upload all six to the character library
4. Record the continuity lock in the brand file
```

**The rule that makes it work:**

> Shot prompts reference the character **by ID only** and **never re-describe their appearance.**

Every fresh description is a fresh interpretation. This is the largest single cause of drift.

❌ `An Indian priest aged 55-60 in a saffron kurta with rudraksha mala, seated...`
✅ `PANDIT_PRIMARY, mid-shot, seated beside the puja setup...`

**Continuity lock** — declared once at the top of every package, never repeated per shot:

```
CAST: PANDIT_PRIMARY (locked), COUPLE_YOUNG (locked)
CONTINUITY LOCK: saffron kurta, angavastram on LEFT shoulder,
  3-strand rudraksha, vertical tilak — unchanged in every shot
```

### TIER C — Frame chaining *(narrative sequences only)*

When the same figure must move through a continuous story — a mythological sequence, a before/after.

```
Clip 1  →  take its LAST frame
        →  use as the FIRST frame of Clip 2
        →  take Clip 2's last frame
        →  use as the FIRST frame of Clip 3
        →  RESET from the character reference
```

**Chain in groups of 2–3, then reset.** Quality degrades after three to five hops — faces soften, details drift, colour shifts. Never chain a whole reel.

**Never chain a speaking shot.** Drift plus imperfect lip sync compounds badly.

---

## THE STILL-FIRST ROUTE (highest control)

For any shot where the character's exact appearance, wardrobe or pose matters:

```
1. Generate the STILL in an image model — exact framing, wardrobe, pose
2. Review and approve the still (cheap, instant, no video credits)
3. Use that still as the FIRST FRAME of the the video tool clip
4. The prompt now describes MOTION only, not appearance
```

This is what the manual workflow is really doing, formalised. It costs one extra step and removes almost all uncertainty — you approve the character before spending video credits, not after.

**Use it whenever:** a Tier 2 object appears, wardrobe must match exactly, or the shot will cut directly against another character shot.

---

## WHAT THE SKILL AUTOMATES

Generation tools are hands-on; the engine automates the thinking, not the clicking.

Every Produce-mode package outputs:

```
CAST BLOCK
  Which locked IDs appear in this reel
  The continuity lock, stated once

PER SHOT
  Tier (A / B / C)
  Which reference image to attach, if any
  Whether this shot chains from the previous one
  Prompt written to reference IDs, never re-describing
  Where to reset a chain
```

Your designer stops deciding and starts executing.

**True end-to-end automation** would mean leaving the video tool for the video model via a model API or the a model API, where reference images pass programmatically. Not worth building at 8 reels a month. Revisit past 20.

---

## SHOT-LIST DESIGN RULES

Apply at Plan mode, before any prompt is written.

```
[ ] Is the speaking presenter from a lip-sync tool?          → must be YES
[ ] How many shots contain a recurring character?   → aim for 0-2
[ ] Can any character shot be reframed to hide
    the face (from behind, wide, cropped)?          → prefer YES
[ ] Do any two clips need the SAME unnamed person?  → redesign
[ ] Does the story require continuous movement
    of one figure?                                  → Tier C, else avoid
```

**If a reel needs a recurring character in more than 3 clips, question the concept.** It is usually a sign the reel is trying to be a short film rather than a reel.

---

## FAILURE MODES

| Symptom | Cause | Fix |
|---|---|---|
| Face changes between clips | Character re-described in the prompt | Reference by ID only |
| Wardrobe drifts | No continuity lock declared | Add the lock block at the top |
| Face softens across a sequence | Chained too many hops | Reset from reference every 2–3 clips |
| Character right but pose wrong | Text-to-video used | Switch to still-first |
| Presenter drifts mid-reel | Presenter generated in the video tool | Move to a lip-sync tool, one continuous render |

---

## THE STANDING RULE

> **Solve consistency by design first, by reference second, by chaining last.**
>
> A character who appears once is always cheaper than a character who appears twice.

---

*Character Consistency Protocol v1 · Pandits Near Me Reels Engine · 29 September 2026*

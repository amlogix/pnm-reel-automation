# GLOBAL REEL RULES v1

**House format for every Pandits Near Me reel. No exceptions without written sign-off.**

Derived by measurement from the reference edit `Last_Final_1_2X.mp4` (Pitru Paksha, 64.7s, 2160×3840, 30fps, 8 segments).

These rules are **additive** to the Reality Check Protocol v1. Both apply to every reel.

---

## 1 · CANONICAL STRUCTURE

Every reel follows this three-act shape. Durations flex; the structure does not.

| Act | Duration | Layout |
|---|---|---|
| **A · Hook** | 0:00 – 0:06 | **Full-frame presenter.** No split. No title bar. |
| **B · Body** | 0:06 – end minus 4s | **Split screen.** Presenter + title bar + b-roll. |
| **C · End card** | Final 4 seconds | **Full-frame contact card.** |

**Target total: 45 – 75 seconds.**

### Why the hook is full-frame

The first 6 seconds decide whether the reel gets distribution at all. A split screen at 0:00 halves the size of the only thing that stops a scroll. The presenter gets the whole frame, then the layout establishes itself once attention is captured.

The title card overlay (question in Devanagari, white box, red keyword) sits over this full-frame hook, per the reel package spec.

---

## 2 · SPLIT-SCREEN LAYOUT — MEASURED SPEC

At 1080 × 1920. Scale proportionally for 4K.

```
┌─────────────────────────┐  0%
│                         │
│   PRESENTER PANEL       │  Speaking character
│   45% of frame height   │  0 – 862px
│                         │
├─────────────────────────┤  44.9%  (862px)
│   TITLE BAR   11.6%     │  862 – 1084px
├─────────────────────────┤  56.4%  (1084px)
│                         │
│   B-ROLL PANEL          │  Illustrative AI video
│   43.6% of frame height │  1084 – 1920px
│                         │
└─────────────────────────┘  100%
```

| Zone | Start | End | Height |
|---|---|---|---|
| Presenter | 0px | 862px | 862px |
| Title bar | 862px | 1084px | 222px |
| B-roll | 1084px | 1920px | 836px |

### Rules

- **Presenter is ALWAYS the top panel.** Never invert. Consistency across reels builds format recognition — viewers should know it's a Pandits Near Me reel within half a second.
- **The presenter panel is never empty.** If the speaker isn't on screen, the whole layout collapses to full-frame b-roll — the split does not appear with a blank top.
- **The b-roll panel is never empty.** If no b-roll exists for a beat, hold the previous clip or go full-frame presenter. Never black.
- **Geometry never changes mid-reel.** The bar does not move, resize, or animate at any point between 0:06 and the end card.
- **Full-frame presenter is permitted mid-body** for emphasis beats, but the title bar stays burned in at the same position.

---

## 3 · TITLE BAR

The single most important continuity device in the format.

| Property | Value |
|---|---|
| Position | 44.9% – 56.4% of frame height |
| Background | Solid black, 100% opacity, full bleed edge to edge |
| Font | Bold Devanagari (Khand Bold or Poppins Devanagari Bold) |
| Size | ~66px at 1080 × 1920 |
| Base colour | White `#FFFFFF` |
| Highlight colour | Gold/yellow `#FFC400` |
| Highlight rule | The **topic keyword only** — usually the first 1–2 words |
| Alignment | Centred, single line |
| Length | Maximum 7 words |

Reference example: `पितृ पक्ष में इन 6 बातों का रखें ध्यान` — `पितृ पक्ष` gold, remainder white.

### Hard rules

- **The title bar text NEVER changes during the reel.** One line, constant from 0:06 to the end card. It is the spine that holds the segments together.
- **It never animates.** No fade, no slide, no typewriter. Static.
- Numbers in Latin digits (`6`, not `६`), per the language spec.
- Devanagari only. No Roman except the brand name.

---

## 4 · TRANSITIONS

### The diagnosis

Each segment is a separate generation. Faces, backgrounds and lighting shift slightly between them. Without a continuity device the reel reads as clips stapled together.

**Ranked by what actually creates continuity:**

| Rank | Device | Effect |
|---|---|---|
| 1 | **Continuous audio bed** | Largest. Audio continuity overrides visual discontinuity. |
| 2 | **Static title bar** | Large. The eye locks to the unmoving element. |
| 3 | **Fixed layout geometry** | Large. Panel boundaries never move. |
| 4 | **Staggered panel changes** | Medium. See below. |
| 5 | Visual transition effect | Small. Cosmetic only. |

Most of the work is done by 1–3. Do not rely on 5 to fix a reel that is failing at 1–3.

### 4.1 Audio — mandatory

- **The ambience bed runs unbroken across every cut.** Never cut audio with picture.
- Narration audio also continues across cuts. A sentence may begin in one segment and finish in the next — this is desirable, it actively welds the segments.
- **Never cut on a silence.** Cut mid-sentence or mid-phrase.

### 4.2 Stagger the panels — mandatory

Do not change the presenter panel and the b-roll panel on the same frame.

```
Frame 0    b-roll panel changes
Frame 5    presenter panel changes   (5 frames = ~0.17s at 30fps)
```

Two small jumps read as continuous motion. One simultaneous jump reads as an edit. This single technique does more than any transition effect.

### 4.3 Permitted transition effects

Applied **within a panel only** — never across the whole frame.

| Effect | Duration | Use |
|---|---|---|
| Motion-blur whip | 4–8 frames | Default for b-roll panel changes |
| Zoom punch (102–105%) | 4–6 frames | Presenter panel changes |
| Cross-dissolve | 6–10 frames | B-roll panel only, for calm/emotional beats |
| Hard cut | 0 | Always acceptable — the reference edit uses these throughout |

### 4.4 Banned

- ❌ Fade to black anywhere before the end card
- ❌ Full-frame dissolves
- ❌ Any transition that moves, covers or interrupts the title bar
- ❌ Spins, page turns, glitch effects, light leaks, star wipes
- ❌ Speed ramps
- ❌ Transitions longer than 10 frames

---

## 5 · THE PNM BRANDING SCREEN — FINAL SCENE, EVERY REEL

**The last scene of every reel, without exception, is the Pandits Near Me branding screen.**

This is the only CTA. There is no persistent contact bar during the reel — the branding screen carries it.

| Property | Value |
|---|---|
| Position | **Final scene of every reel, every type** |
| Duration | 3–4s (2s minimum on a short reel) |
| Layout | Full frame |
| Content | PNM logo · phone · email · website · address |
| Phone | `(+91) 97246-76277` |
| Logo | **Identical every time.** Same mark, same position, same size. |
| Transition in | 8-frame dissolve — the only permitted fade in the whole reel |
| Audio | Bed continues under it, fading over the final second |

**On a very short reel**, shorten to logo + phone only. A full contact panel cannot be read in 2 seconds.

**Logo consistency is the point.** After twenty reels the closing frame is recognised before it is read. Never redesign it per reel, per festival, or per topic.

---

## 6 · WATERMARK

A small PNM logo mark sits bottom-right on every frame from 0:00 until the branding screen. ~6% of frame width, ~85% opacity.

---

## 7 · TECHNICAL

| Property | Value |
|---|---|
| Resolution | 1080 × 1920 minimum |
| Frame rate | 30fps |
| Aspect | True 9:16, **no letterboxing** |
| Audio | AAC, stereo, 48kHz |
| Tool watermarks | **None.** Check every export. |

---

## 11 · COLOUR GRADE — THE STRONGEST CONTINUITY DEVICE

**Added from competitor analysis, September 2026.**

Automatic scene detection run on a Sri Mandir narrative reel **failed to find most of its cuts.** Not a bug — the colour grade across every shot was so uniform that the algorithm could not tell the shots apart.

Every frame carried the same warm golden amber, the same light direction, the same contrast.

> **If an algorithm cannot find the cuts, a viewer will not feel them.**

This outranks every transition effect in Section 4. Revised ranking:

| Rank | Device |
|---|---|
| 1 | **Unified colour grade across every shot** |
| 2 | Continuous audio bed |
| 3 | Static title bar |
| 4 | Fixed layout geometry |
| 5 | Staggered panel changes |
| 6 | Visual transition effect |

**How to apply it:**
- Decide a single grade per reel and apply it to **every** clip, generated or filmed
- Name the grade in every shot prompt — same light direction, same time of day, same warmth
- Apply a final grading pass across the whole timeline in the editor, not per clip
- Suggested house grades: **warm golden** (mythology, festivals), **cool neutral** (practical, explainer), **soft muted** (Shradh, ancestral)

---

## 12 · NAME CARDS

Large-type overlays for proper nouns, at the moment they are spoken.

Reference usage: तुलसी · अक्षयवट · फल्गु नदी गयाजी appear as big overlay labels mid-reel.

| Property | Value |
|---|---|
| When | A place, deity, object or concept is named for the first time |
| Type size | Roughly 2× the subtitle size |
| Style | Same font as the title bar, gold or white with a soft shadow |
| Position | Upper-middle third, clear of the subtitle band |
| Duration | 1.5–2s, then out |
| Limit | **Maximum 3 per reel** |

The viewer learns specific vocabulary and feels they gained something concrete. It is also what gets remembered and searched.

---

## 13 · OPENING HOOK LINE

The first line of narration is set **larger than the body subtitles** — roughly 1.4×, same font, same position. It drops to normal size from the second line onward.

The reveal, when there is one, also gets the larger treatment. In the Sita reel the surprising fact at second 5 is set bigger than everything around it.

---

## 14 · MUSIC BED BY FORMAT

| Format | Music level | Notes |
|---|---|---|
| A · Split Authority | 12–15% | Presenter carries it |
| B · Narrative Story | 15–18% | Supports the story |
| **D · Narrated Explainer** | **18–22%** | No face, no dialogue — music does the emotional work |

**Universal music rules:**
- Soft instrumental. **No vocals, ever** — they compete with narration.
- Indian classical or neo-classical texture: tanpura drone, bansuri, sarod, light or no percussion
- **No trending audio.** The narration is the content.
- One continuous track, unbroken across every cut, fading over the final second
- Slow, steady tempo. Nothing that builds to a drop.
- **Mood matches topic register.** Shradh, loss and doubt get a drone-only bed with no percussion.

---

*Global Reel Rules v3 · Pandits Near Me Reels Engine · October 2026*
*No tool or model named anywhere. Structure outlives tools.*
*Applies to every reel, alongside Reality Check Protocol v1.*
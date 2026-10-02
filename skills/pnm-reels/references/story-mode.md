# STORY MODE

**Third mode of the Pandits Near Me Reels Engine.**
For narrative reels with multiple recurring characters — mythological stories, Puranic retellings, origin stories.

Distinct from Produce Mode, which builds talking-head reels around a presenter. Story Mode has **no presenter**, **multiple characters**, and **narration over silent visuals**. Character consistency is the central problem it exists to solve.

---

## WHAT IT REPLACES

The current manual loop:

```
topic → story in ChatGPT → edit by hand → finalise
      → decide which characters exist
      → source character images
      → upload to the video tool, attach per scene from memory
      → generate clips
      → merge in the editor
      → add ElevenLabs voice
```

Two things leak accuracy: the character-to-scene mapping lives in someone's head, and the voice is fitted to the video instead of the video being cut to the voice.

Story Mode outputs both as explicit artifacts.

---

## THE ORDER OF OPERATIONS — READ THIS FIRST

```
1. Story          →  finalised beats
2. Cast sheet     →  every character locked
3. Reference imgs →  an image model, 6 angles each, approved
4. NARRATION      →  ElevenLabs render FIRST
5. Measure        →  actual duration of each line
6. Scene list     →  built to those measured durations
7. Scene stills   →  an image model, approved before video
8. Clips          →  the video tool, references attached per matrix
9. Assembly       →  the editor, cut to the audio
```

**Step 4 before step 6 is the change.** Render the voice, measure it, then build scenes to fit. Cutting video to audio is how edits are actually made — it removes the "scene is 8s, line is 6.2s" problem before it exists.

---

## REQUIRED OUTPUTS

Every Story Mode package contains these eight sections.

### § 1 · STORY

The finalised narrative in beats. Not prose — beats.

```
BEAT 1  Setup        Who, where, what is normal
BEAT 2  Disruption   What changes
BEAT 3  Conflict     What goes wrong
BEAT 4  Turn         The revelation or intervention
BEAT 5  Resolution   What it means
BEAT 6  Bridge       Why this matters to the viewer today
BEAT 7  CTA          Pandits Near Me
```

Each beat carries `[VERIFY]` markers on any religious claim.

### § 2 · CAST SHEET

**Every character, with a complete visual lock.** This is where consistency is won or lost.

The lock covers **face AND costume AND ornament.** Locking the face alone lets crowns, tilaks and jewellery drift between generations — visible in analysed reference footage where a lead's crown changed noticeably between clips while the face held.

```
CHARACTER ID:     KARNA_LEAD
Role in story:    Protagonist
Appears in:       Scenes 1, 3, 5, 8

FACE LOCK
  Age read:       early 30s
  Build:          athletic, broad shoulders
  Hair:           long, dark, loose waves
  Facial hair:    clean-shaven
  Distinguishing: none

COSTUME LOCK
  Head:           gold domed crown, ONE red centre stone,
                  no peacock feather, no secondary stones
  Forehead:       white urdhva-pundra, single red centre line
  Neck:           three-layer gold necklace, ruby pendant
  Body:           cream dhoti, maroon and gold border
  Sash:           red silk over left shoulder
  Arms:           gold armlet on right bicep only
  Wrists:         two gold bangles, right wrist
  Feet:           bare

NEVER:            second crown variant, peacock feather,
                  additional jewellery, sandals, armour
```

**Every ornament is named or banned.** Anything unspecified is something the model will invent differently each time.

### § 3 · CHARACTER REFERENCE PROMPTS

For each character, a an image model prompt run six times — front, ¾ left, ¾ right, profile, slight low, slight high. Identical lighting and wardrobe across all six.

Naming convention, used verbatim in the matrix:

```
KARNA_LEAD_front.png
KARNA_LEAD_tql.png
KARNA_LEAD_tqr.png
KARNA_LEAD_profile.png
KARNA_LEAD_low.png
KARNA_LEAD_high.png
```

**Approve every reference image before generating a single video clip.** An image costs seconds. A clip costs credits and minutes.

### § 4 · CHARACTER × SCENE MATRIX

**The artifact that removes the memory step.**

| Scene | Duration | KARNA_LEAD | KRISHNA | FAMILY | PANDIT | Attach |
|---|---|---|---|---|---|---|
| 1 | 6.2s | ✅ | ✅ | — | — | `KARNA_front` + `KRISHNA_tql` |
| 2 | 5.8s | — | — | — | — | none |
| 3 | 7.1s | ✅ | ✅ | — | — | `KARNA_tqr` + `KRISHNA_front` |
| 4 | 6.4s | — | — | ✅ | — | `FAMILY_wide` |
| 5 | 8.0s | ✅ | — | — | — | `KARNA_profile` |
| 6 | 6.6s | — | — | — | ✅ | `PANDIT_PRIMARY_front` |
| 7 | 5.9s | — | — | ✅ | — | `FAMILY_wide` |
| 8 | 7.3s | ✅ | — | ✅ | — | `KARNA_front` + `FAMILY_wide` |

The designer works down the Attach column. No decisions, no recall.

**Durations come from the measured narration, not from a guess.**

### § 5 · SCENE PROMPTS

One fenced block per scene, ready to paste.

**Prompts describe motion, setting and camera. Never appearance.**

```
SCENE 5 · 8.0s · hero shot · still-first

ATTACH: KARNA_profile.png as first frame

KARNA_LEAD seated on a stone step at the river's edge, head
lowered. He slowly raises one open palm, then lets it fall.
Still water and distant temple spires softly out of focus behind.

Light: low sun from camera-right, warm, long shadows.
Camera: 50mm, eye level, locked off, very slow push-in.

Negative: text, letters, script, watermark, extra fingers,
merged fingers, costume change, additional jewellery,
second crown, direct gaze into camera
```

**Rules for every scene prompt:**
- Reference the character by ID. Never re-describe. Each re-description is a fresh interpretation.
- Add the costume-lock negatives — `costume change, additional jewellery, second crown`
- Name a real light source and a real lens
- Hero shots use **still-first**: approve the an image model frame, then use it as the clip's first frame
- **No readable-ornament close-ups on a recurring character** — mid-shot or wider. Ornament drift only becomes visible in close-up.
- 8 seconds maximum. Never Extend a character shot.

### § 6 · NARRATION — ELEVENLABS

Rendered **before** the scene list is finalised.

| ID | Scene | Hindi | Measured |
|---|---|---|---|
| N-01 | 1 | … | 6.2s |
| N-02 | 2 | … | 5.8s |

| Setting | Value |
|---|---|
| Voice | Locked voice ID — same across every reel |
| Language | Hindi |
| Pace | 2.2 words/sec maximum |
| Sanskrit | **Never TTS.** Real pandit recording or on-screen Devanagari with silence. |
| Export | Per-line WAVs, named `N-01.wav`, so scenes cut to them |

Fill the Measured column from the actual rendered files. **Those numbers become § 4's durations.**

### § 7 · PREMIERE EDIT SHEET

| In | Out | Scene | Audio | Transition |
|---|---|---|---|---|
| 0:00 | 0:06.2 | S1 | N-01 | — |
| 0:06.2 | 0:12.0 | S2 | N-02 | hard cut |

Plus:
- Ambience bed level and its unbroken in/out
- Subtitle text per scene, typed from § 6
- Title bar text, constant
- the branding screen in-point
- End card, final 4 seconds
- Watermark in/out

**Tool watermarks must be removed.** The Gemini sparkle appears bottom-right on Google generations and has shipped in reference footage.

### § 8 · ACCURACY CHECKLIST

Standard rows plus, for Story Mode:

```
[ ] Every character in the matrix has an approved reference sheet
[ ] Every scene's attached reference matches the matrix
[ ] Costume lock holds in every clip — crown, tilak, jewellery
[ ] No recurring character shown in readable-ornament close-up
[ ] Scene durations match measured narration, not estimates
[ ] [P] Every deity frame passed the second review
[ ] No tool watermark in any frame
```

---

## CHARACTER BUDGET

| Characters in a reel | Verdict |
|---|---|
| 1–2 recurring | Ideal |
| 3–4 recurring | Workable with still-first on every hero shot |
| 5+ recurring | Redesign. Consistency cost grows faster than story value. |

**Non-recurring characters are free.** A group that appears in exactly one scene needs no reference and no consistency work. Analysed reference footage does this deliberately — the lead recurs across five clips, while the couple, the pandit and the family each appear once and never again.

**Design the story so only the protagonist recurs.**

---

## THE AUTOMATION CEILING

| Step | Status |
|---|---|
| Story, cast sheet, matrix, prompts, narration script, edit sheet | ✅ Skill output |
| Generating reference images | Paste into an image model |
| Uploading to the video tool, generating clips | ❌ No API — hands-on by design |
| the editor assembly | ❌ Manual |
| ElevenLabs render | API exists; scriptable if wanted |

**Roughly 70% automated**, and it is the writing, deciding and tracking — the part that currently consumes the day.

### Full automation, if ever wanted

Leave the video tool for **the video model via a model API or the a model API**, which accept reference images programmatically. Combined with the Gemini image API, the ElevenLabs API and FFmpeg for assembly, the chain is scriptable end to end.

**Cost:** you lose the tool's character library and storyboard review, and it needs a developer for roughly two weeks.

**Worth it above ~20 reels a month. Not below.**

---

*Story Mode v1 · Pandits Near Me Reels Engine · 29 September 2026*

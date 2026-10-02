# SETUP NOTES

## Keys needed

| Key | Where from | Required for |
|---|---|---|
| `ELEVENLABS_API_KEY` | elevenlabs.io → Profile → API Key | narration |
| `ELEVENLABS_VOICE_ID` | Voice Library → your cloned voice → ID | narration |
| `APIFY_TOKEN` | apify.com → Settings → Integrations | competitor data |
| `APIFY_ACTOR_ID` | the Instagram Reels Competitor Creative Watch actor | competitor data |

## The voice

Clone **one** voice and never change it. 30+ seconds of clean audio minimum; a few minutes of your narrator speaking Hindi including ritual vocabulary is better.

That same `ELEVENLABS_VOICE_ID` carries every reel in every format. Recognition compounds the same way the locked saree colour does.

**Never TTS Sanskrit.** Mantras get recorded by a real pandit or shown as on-screen Devanagari with silence.

## First run

```bash
python scripts/check_claim.py "test"        # should say UNVERIFIED
python scripts/log_reel.py --reel-id TEST   # should append a row
```

If both work, the writable layer is live — which is the main reason to run here rather than on claude.ai.

## Before the first real reel

```
[ ] Pandit signs the festival calendar rows (verified=YES)
[ ] Confirm 500+ or 600+ verified pandits — site and Instagram bio disagree
[ ] Confirm (+91) 97246-76277 is the monitored number
[ ] Clone the narrator voice, put the ID in .env
[ ] Seed content-log.csv with what the existing 338 posts covered
[ ] Build the end-card template in CapCut
```

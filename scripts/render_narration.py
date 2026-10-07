#!/usr/bin/env python3
"""
Render a Hindi narration script via ElevenLabs and report the EXACT duration.

Story Mode requires narration to be rendered BEFORE the scene list is built,
so scene durations come from measured audio rather than estimates.

Usage: python render_narration.py script.txt out.mp3
"""
import sys as _sys
for _s in (_sys.stdout, _sys.stderr):  # Windows consoles default to cp1252; output is Devanagari
    _s.reconfigure(encoding="utf-8")
import os, sys, subprocess, requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE = os.getenv("ELEVENLABS_VOICE_ID")
MODEL = os.getenv("ELEVENLABS_MODEL", "eleven_multilingual_v2")

def render(text, out):
    r = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}",
        headers={"xi-api-key": KEY, "Content-Type": "application/json"},
        json={"text": text, "model_id": MODEL,
              "voice_settings": {"stability": 0.5, "similarity_boost": 0.75,
                                 "style": 0.0, "speed": 0.85}},
        timeout=180)
    r.raise_for_status()
    Path(out).write_bytes(r.content)

def duration(path):
    out = subprocess.run(
        ["ffprobe","-v","error","-show_entries","format=duration",
         "-of","csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())

if __name__ == "__main__":
    if not (KEY and VOICE):
        raise SystemExit("Set ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID in .env")
    if len(sys.argv) < 3:
        raise SystemExit("usage: render_narration.py script.txt out.mp3")
    text = Path(sys.argv[1]).read_text(encoding="utf-8").strip()
    if len(text) > 600:
        print(f"WARNING: {len(text)} chars — over the 600 limit")
    render(text, sys.argv[2])
    d = duration(sys.argv[2])
    print(f"rendered {sys.argv[2]}")
    print(f"DURATION: {d:.2f}s  ->  {int(d//4)+1} shots at 4s")
    print("Use this duration for the scene list. Do not estimate.")

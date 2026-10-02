#!/usr/bin/env python3
"""
Pull competitor reel data from an Apify actor and write data/instagram-hooks.md,
which the skill's Tier 2 trend scan reads.

Apify is used because Instagram's own API does not expose other accounts' view
counts. That also means this can break when Instagram changes something — the
manual fallback in the skill stays valid.
"""
import os, json, requests
from pathlib import Path
from datetime import date
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("APIFY_TOKEN")
ACTOR = os.getenv("APIFY_ACTOR_ID")
HANDLES = [h.strip() for h in os.getenv("COMPETITOR_HANDLES", "").split(",") if h.strip()]
OUT = Path(__file__).parent.parent / "data" / "instagram-hooks.md"

def run_actor():
    url = f"https://api.apify.com/v2/acts/{ACTOR}/run-sync-get-dataset-items"
    r = requests.post(url, params={"token": TOKEN},
                      json={"handles": HANDLES, "resultsLimit": 10}, timeout=600)
    r.raise_for_status()
    return r.json()

def write(items):
    lines = [f"# COMPETITOR HOOKS — {date.today().isoformat()}", "",
             "Auto-generated. Read by Plan mode, Step 1, Tier 2.", ""]
    by_handle = {}
    for it in items:
        by_handle.setdefault(it.get("ownerUsername", "unknown"), []).append(it)
    for handle, reels in by_handle.items():
        reels.sort(key=lambda x: x.get("videoPlayCount") or 0, reverse=True)
        lines += [f"## @{handle}", ""]
        for r in reels[:10]:
            cap = (r.get("caption") or "").split("\n")[0][:120]
            lines.append(f"- **{r.get('videoPlayCount','?')} views** — {cap}")
            lines.append(f"  - {r.get('url','')}")
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT} ({len(items)} reels)")

if __name__ == "__main__":
    if not (TOKEN and ACTOR and HANDLES):
        raise SystemExit("Set APIFY_TOKEN, APIFY_ACTOR_ID and COMPETITOR_HANDLES in .env")
    write(run_actor())

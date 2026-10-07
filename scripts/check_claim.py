#!/usr/bin/env python3
"""
Check whether a claim is already verified. The cache that makes the
verification gate scale: verified once, reused forever.

Usage: python check_claim.py "अखंड ज्योत"
"""
import sys as _sys
for _s in (_sys.stdout, _sys.stderr):  # Windows consoles default to cp1252; output is Devanagari
    _s.reconfigure(encoding="utf-8")
import csv, sys
from pathlib import Path

DB = Path(__file__).parent.parent / "data" / "verified-claims.csv"

def main(query):
    if not DB.exists():
        print("No verified-claims.csv yet — claim is UNVERIFIED")
        return
    hits = []
    with open(DB, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            blob = " ".join(row.values()).lower()
            if query.lower() in blob and row.get("verified_by"):
                hits.append(row)
    if not hits:
        print(f"UNVERIFIED — '{query}' not in cache. Mark [VERIFY] and add a pending row.")
        return
    for h in hits:
        print(f"VERIFIED ({h['claim_id']}) by {h['verified_by']} on {h['verified_date']}")
        print(f"  scope : {h['scope']}")
        print(f"  claim : {h['claim_hi']}")
        print(f"  source: {h['source_text']}")
        print(f"  reused: {h['reuse_count']} times")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: check_claim.py \"<topic or claim>\"")
    main(" ".join(sys.argv[1:]))

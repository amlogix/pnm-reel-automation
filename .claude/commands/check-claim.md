---
description: Check whether a religious/ritual claim is already verified
argument-hint: <claim or keyword>
---

Run `python scripts/check_claim.py "$ARGUMENTS"` and report the result plainly.

- VERIFIED → quote the cached wording, scope and verifier.
- UNVERIFIED → say so. Do NOT supply the answer from memory or a web search, and do NOT write anything into `data/verified-claims.csv` — only a human may add verified values. Offer to add a pending row if the user wants one.

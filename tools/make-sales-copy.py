#!/usr/bin/env python3
"""The strip pass — generates the Enfys sales copy from the live site.

Build rule (Noticeboard, 10 Jun 2026): the sales copy is GENERATED from the
live site, never hand-maintained, so the two copies cannot drift. This script
is that generator. Run it after any site change that should reach the sales
copy; the output folder is disposable and fully regenerated every run.

Usage:
    python3 make-sales-copy.py [site_dir] [out_dir] [gate_password]

Defaults: site_dir = the folder above this script; out_dir = a sibling of the
site folder named "Enfys Sales Copy"; password = Croeso2026 (placeholder,
Rachel's call which word guards the show copy).

What it does, per the pinned rule (strip: prices, the ledger, KPIs, the
Noticeboard, Deep Vault gap-lists, keeper personal detail):
  1. Copies every page, the images folder and .nojekyll.
  2. EXCLUDED pages are replaced with a graceful holding page so inbound
     links never 404. The excluded set is the conservative first draft:
     everything carrying money, capacity, open items, IG gap-lists,
     position-paper IP or keeper personal detail.
  3. REDACTS in the kept pages: every pound amount becomes "£ —", and the
     gate password is swapped for the show password.
  4. Writes MANIFEST.md: what was excluded, what was redacted, where.
⚑ The excluded set and redaction rules are the Cartographer's first
proposal; tighten or loosen with Rachel before any prospect sees it.
"""
import os, re, shutil, sys

EXCLUDE = {
    "the-noticeboard.html":      "the open-items board is keeper business",
    "the-hourglass.html":        "the capacity ledger is keeper business",
    "the-wares.html":            "the year-one ledger is keeper business",
    "the-commercial-playbook.html": "the commercial plays are keeper business",
    "the-deep-vault.html":       "the IG architecture is shown in person, not left in a copy",
    "the-deep-vault-playbook.html": "the IG plays are shown in person, not left in a copy",
    "the-burrows.html":          "the systems register is keeper business",
    "the-records-room.html":     "the position papers are keeper business",
    "pp-01.html":                "the position papers are keeper business",
    "the-instrument.html":       "the full method core is shown in person, not left in a copy",
    "the-register.html":         "the full internal index summarises every page, including the held-back ones",
    "keeper-rachel.html":        "the keeper pages are personal",
    "keeper-scott.html":         "the keeper pages are personal",
    "keeper-hannah.html":        "the keeper pages are personal",
    "keeper-open-seat.html":     "the keeper pages are personal",
}

# Story content is never redacted: the picture book's mock cover price is
# canon furniture, not a commercial figure.
NO_REDACT = {"loveheart-book.html"}

HOLDING = """<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Enfys · a closed door</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,500&display=swap" rel="stylesheet">
<style>body{{font-family:'Segoe UI',sans-serif;background:linear-gradient(180deg,#14101F,#3A2858);color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:30px}}
.c{{max-width:480px}}h1{{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;font-size:38px;margin-bottom:10px}}h1 em{{color:#E8B33A;font-style:italic}}
p{{font-size:14px;color:rgba(255,255,255,0.8);line-height:1.65}}a{{color:#E8B33A;font-weight:700;text-decoration:none}}</style>
<script>(function(){{try{{if(sessionStorage.getItem('pv-enfys-gate-ok')!=='1')location.replace('index.html');}}catch(e){{}}}})();</script>
</head><body><div class="c"><h1>This door is <em>closed</em></h1>
<p>In the show copy of Enfys, {reason}. Ask your guide — they will gladly open it with you.</p>
<p><a href="index.html">← back to the Drawbridge</a></p></div></body></html>
"""

POUND = re.compile(r"(?:~\s*)?£\s?[\d][\d,\.]*\s?(?:k|K|m|M)?(?:\s?[–—-]\s?£?\s?[\d][\d,\.]*\s?(?:k|K|m|M)?)?")

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    site = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(here)
    out  = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(os.path.dirname(site), "Enfys Sales Copy")
    pwd  = sys.argv[3] if len(sys.argv) > 3 else "Croeso2026"
    if os.path.isdir(out): shutil.rmtree(out)
    os.makedirs(out)
    manifest = ["# Enfys sales copy — strip-pass manifest\n",
                f"Generated from: {site}\n", "## Excluded (replaced with holding pages)\n"]
    pages = sorted(f for f in os.listdir(site) if f.endswith(".html") and not f.startswith("_"))
    redactions = []
    for f in pages:
        src = os.path.join(site, f)
        dst = os.path.join(out, f)
        if f in EXCLUDE:
            open(dst, "w", encoding="utf-8").write(HOLDING.format(reason=EXCLUDE[f]))
            manifest.append(f"- {f} — {EXCLUDE[f]}")
            continue
        s = open(src, encoding="utf-8").read()
        n = 0
        if f not in NO_REDACT:
            n = len(POUND.findall(s))
            s = POUND.sub("£ —", s)
        s = s.replace("Rainbow2026", pwd)
        open(dst, "w", encoding="utf-8").write(s)
        if n: redactions.append(f"- {f} — {n} pound amount(s) redacted")
    manifest.append("\n## Redactions in kept pages\n")
    manifest.extend(redactions or ["- none"])
    manifest.append(f"\nGate password for the show copy: {pwd} (placeholder ⚑, Rachel's call)\n")
    manifest.append("Regenerate after any site change: this folder is disposable output, never edited by hand.\n")
    if os.path.isdir(os.path.join(site, "images")):
        shutil.copytree(os.path.join(site, "images"), os.path.join(out, "images"))
    nj = os.path.join(site, ".nojekyll")
    if os.path.exists(nj): shutil.copy(nj, out)
    open(os.path.join(out, "MANIFEST.md"), "w", encoding="utf-8").write("\n".join(manifest))
    print(f"Sales copy written to: {out}")
    print("Pages: %d (%d held back) - password: %s" % (len(pages), len(EXCLUDE), pwd))

    # --- the sentinel: the generated cut is a security boundary, so fail the
    # build loudly if anything that must never reach a prospect leaked through.
    # A generated wall that is hand-edited once will leak; this check stops a
    # silent leak ever shipping.
    SENTINELS = [
        ("Rainbow2026",         "the KEEPER gate password"),
        ("keeper-confidential", "a keeper-confidential marker"),
        ("keeper business",     "an internal keeper-business marker"),
    ]
    PRICE    = re.compile(r"\u00a3\s?\d")
    CAPACITY = re.compile(r"\bkeeper[\s-]days?\b", re.I)
    leaks, warnings = [], []
    for f in sorted(os.listdir(out)):
        if not f.endswith(".html") or f in EXCLUDE:
            continue
        txt = open(os.path.join(out, f), encoding="utf-8").read()
        for tok, desc in SENTINELS:
            if tok in txt:
                leaks.append("%s: %s (%r)" % (f, desc, tok))
        if f not in NO_REDACT and PRICE.search(txt):
            leaks.append("%s: an unredacted price (pound sign followed by a digit)" % f)
        if CAPACITY.search(txt):
            leaks.append("%s: capacity language (keeper-days)" % f)
        for name in ("Rachel", "Hannah"):
            if name in txt:
                warnings.append("%s: keeper name %r (check it is canon, not commercial)" % (f, name))
    if warnings:
        print("\nSentinel warnings (review, not blocking):")
        for w in warnings[:50]:
            print("  - " + w)
    if leaks:
        print("\nSTRIP-PASS SENTINEL FAILED - sensitive content reached the public cut:")
        for l in leaks:
            print("  x " + l)
        print("\nFix the source or widen EXCLUDE, then regenerate. The copy is NOT safe to ship.")
        sys.exit(1)
    print("\nSentinel passed: no prices, passwords, capacity figures or keeper-business markers in the public cut.")

if __name__ == "__main__":
    main()

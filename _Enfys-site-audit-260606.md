# Enfys site — deep-dive audit

**Date:** 6 June 2026 · **Scope:** all 23 live pages of the Operating Model site, checked against the primary sources (Business Plan v3, the Lexicon/construct, the Leadership doc, the Roadmap, PP-01, and the positions settled this week). **Status:** findings only. Nothing on the site has been changed.

---

## The headline

The bones are sound. The five-frame structure, the two-TOM settlement, the WHEN two-loops, the Millwheel flywheel and the funnel logic are all internally consistent and match the primary sources. The numbers on the site (prices, cohort sizes, evidence gates, revenue path) are genuinely sourced to Business Plan v3 and the research programme, not invented.

What needs attention falls into a short list of real problems and a longer tail of duplication and cosmetics. The four that actually matter: one genuine concept confusion (what the "Black Egg" is), two number contradictions that sit on a single page each, and the unfinished bit of the source-of-truth decision (the site still defers to "the Lexicon" in places, and the Lexicon has no home on the site). Fix those and the rest is tidying.

Findings are grouped by your criteria: alignment/logic, primary-source reliance, duplication, confusion/naming, complexity. Each carries a severity and a recommendation. A separate list at the end holds the things only you or Rachel can settle.

---

## A. Alignment and logic

**A1 — [HIGH] "Black Egg" means two different things.** It is used as (a) the product/ware, the free-to-paid "one door in" tier, and (b) a diagnostic instrument run at intake alongside the VQ Assessment. The Black Egg page itself keeps them apart: the Egg is a message-level transmission-fidelity instrument, the VQ Assessment is the 36-question capability diagnostic, "siblings, not the same thing." But the Millwheel page says outright "The Black Egg is the VQ diagnostic," which collapses the two. **Recommend:** settle what the Black Egg is (product, instrument, or a product built on an instrument) and correct the Millwheel line so it stops calling the Egg the VQ diagnostic. This is the one finding that's a genuine conceptual knot, not a typo.

**A2 — [HIGH] Year-one revenue contradicts itself on one page.** The Burrows Ledger entry says both "~£250k year-one path" and "~£225k worked path" in the same block. Business Plan v3's worked scenario is ~£225k; the Map Room and the Wares both use ~£225k. **Recommend:** use ~£225k everywhere (or always show it as a "~£225–250k" range), and fix the Burrows so a single entry doesn't state two figures.

**A3 — [MED] The "messengers of Enfys" link is circular.** On the Green, that card points back to the-green.html itself. **Recommend:** point it at the intended page (a characters/messengers page if one is coming) or remove the card until it exists.

**A4 — [MED] Empty link slots in the markup.** The Observatory, the Cartographer's Table and PP-01 each have blank `<a>` anchors sitting in their links rows, a shared template defect that renders as dead/empty links. **Recommend:** delete the empty anchors.

**A5 — [MED] PP-04 card has a dropped quote.** On the Records Room, the PP-04 entry reads "Original clause:&nbsp;&nbsp;Drafted faithfully…" with nothing after the label, a missing piece of text. **Recommend:** restore the clause text (needs the PP-04 source).

**A6 — [MED] The picture book is a dead end.** loveheart-book.html has no back link or nav of any kind, so once you're in it there's no way back into the site. **Recommend:** add the standard back-to-Drawbridge (or back-to-Green) link.

**A7 — [LOW] Duplicate link.** The Town Hall lists "The Records Room · decisions settled" twice in the same row. **Recommend:** drop one.

**A8 — [LOW] Records Room back link is inconsistent.** It backs to the Town Hall while most pages back to the Drawbridge. This is probably a deliberate parent-child (Town Hall → Records Room → PP-01), in which case leave it, but worth a conscious decision.

---

## B. Primary-source reliance

**B1 — [HIGH] The source-of-truth strip isn't finished, and the Lexicon has no home.** Two footers still say "the Lexicon governs" (the Millwheel and the Cartographer's Table), which defers off-site after we decided the site is the source of truth. Bigger than the leftover text: the Lexicon is named everywhere as the supreme authority, yet it has no page, its Library spine is a dead decorative element, and both the Library and the Construct independently "restate" it. So the most authoritative thing on the estate is the one thing you can't reach, and it's restated in two places that can drift apart. **Recommend:** decide that the Construct IS the canonical language on the site (make it the Lexicon's home, not "a restatement of it"), point the Library's Lexicon spine at the Construct, and remove the remaining "the Lexicon governs" footers. That makes the site genuinely self-contained, which was the whole point of the strip.

**B2 — [LOW, by design] External dependencies.** The Philosophy, Manifesto and Welcome (Kajabi), the content bank (OneDrive), and the spec docs (Deep Vault, Black Egg, PP-04/PP-05 as local .docx) are all off-site. That's intentional, those are the things the site deliberately does not reproduce. Just be aware they're single points of failure, and the .docx links break if the files move relative to the site.

**B3 — [NOTE, good] The numbers check out.** £1,495 RtG, ~£125/mo Greenhouse, ~£49–99 Black Egg, 5 cohorts/~55 participants, ~53% product share, n=20/60/100 gates, ρ≥0.25, α≥0.70, ~£225k path, ~£30k TOM, all trace to Business Plan v3 or the research programme. No invented figures found. The only number problems are the internal contradictions in A2 and C-pricing below, not bad sourcing.

---

## C. Duplication

**C1 — [MED] The Library and the Construct say the same things.** Both restate the five sacred nouns, the six rungs, the four compensations and the seven leaks. It's deliberate (Library = the shelf, Construct = the full reference), but it's two independent copies of the Lexicon's content that will drift. **Recommend:** let the Library name the concepts and point to the Construct for the definitions, rather than restating them. One canonical home, per your own rule.

**C2 — [LOW] Keeper roles are stated three times.** Full role descriptions live on the Town Hall, again on each keeper page, and again in the Gather's actor cells. Some restatement aids navigation; the Gather cells are the most redundant. **Recommend:** trim the Gather cells to the action in that stage, not the whole role.

**C3 — [LOW] The proof trio is verbatim on four pages.** "PowerVox rehearsal / Servita UK validation / British Nuclear falsification" appears word-for-word on the Wares, the Cartographer's Table, the Town Hall and keeper-scott. **Recommend:** state it fully once (the Cartographer's Table) and shorten elsewhere.

**C4 — [LOW] Black Egg price and owners are duplicated verbatim** on the Wares and the Black Egg page; the Greenhouse in-year vs run-rate split is repeated on several pages. Low risk, but every duplicated figure is a place the single source of truth can fork.

---

## D. Confusion and naming

**D1 — [MED] "TOM Method" points to two places.** It links to the Cartographer's Table (the method) from the Library, Village Year and Wares, and to the Gather ?p=tom (running an engagement) from the topnav and the product diamonds. Both are legitimate (the method vs operating it), but the same label going to two destinations reads as confusing. **Recommend:** label them distinctly, e.g. "The TOM Method" → Cartographer's Table, and "Run a TOM engagement" → Gather.

**D2 — [MED] Three names for a future enterprise instrument.** The Map Room has a "Leadership Compensation Index" (2030) and a "VQ™ index" (2033+); PP-01 has "a Voice Quotient index"; the Black Egg has "v3 The System" (2030 enterprise). These may be one thing or several. **Recommend:** confirm and use one name, or state plainly how they relate.

**D3 — [MED] "the Welcome page" is referenced but isn't a site page.** The Records Room (PP-02, PP-03) cites "the Welcome page"; the Welcome only exists as the external Kajabi link. **Recommend:** make clear it's the external Welcome, so it doesn't read as a broken internal reference.

**D4 — [LOW] Noticeboard maths.** The headline says 36 open items; the visible groups sum to about 33. **Recommend:** reconcile the count.

**D5 — [LOW] Date niggles.** seren.html says "Serenwood founded 2009 … sixteen years later" (that's anchored to the 2025 rebrand; in a June 2026 page it reads as seventeen). PP-01 is "v0.1 · May 2026" in the header and "June 2026 rendering" in the footer (probably fine, paper vs render). keeper-scott's "eight years ago" for the method vs "since Serenwood" (2009) is two different clocks and could confuse. **Recommend:** a light pass for date consistency.

---

## E. Complexity and cosmetics

**E1 — [LOW] The Millwheel over-explains.** The river/buckets/hub/mill/smoke metaphor is spelled out four times on one page (sub-heading, hover caption, paragraph, legend). **Recommend:** say it once well, let the rest be labels.

**E2 — [LOW] Uneven ⚑ flags.** On the Gather some proposal cells carry the ⚑ and others don't, and the Wares uses the glyph with no legend on the page. **Recommend:** apply ⚑ consistently and add a one-line legend wherever it appears.

**E3 — [LOW, known] The gate password** is hardcoded in client JS ('Rainbow2026'), openly "friction, not security." Fine for an internal site; just don't mistake it for protection.

**E4 — [LOW] Orphan terms.** "Arte Club," "Authority of One," "the Commons," "Mehtab," "FairGround" each appear once with no page, seat or definition. Most are deliberately parked or flagged on the Noticeboard already; worth a sweep to either define or drop.

---

## F. Things only you or Rachel can settle (verify, don't auto-fix)

1. **What the Black Egg actually is** (settles A1): product, instrument, or product-on-instrument. The spec contradiction the site already flags ("locked for engineering handoff" vs "pressure-test before build") sits under this.
2. **Servita vs Servitor.** The Records Room says "Servitor Path A/B"; the Wares and Cartographer's Table say "Servita UK." Same entity misspelled, or two genuinely different things (a client vs an entity path)? I couldn't resolve this from the sources with confidence.
3. **The Seren character vs the Signal guardrail.** seren.html gives the receptive intelligence a character (Seren) "alongside Ada (IQ), Ceri (EQ) and Will (VQ)." The standing guardrail says Signal is never named as a peer intelligence alongside IQ/EQ/VQ. The story layer may breach the guardrail, or may be a deliberate fiction exception, that's Rachel's canon call.
4. **The enterprise-instrument names** (D2), one thing or several.
5. **The Loop/TOM price** (£20k vs ~£30k). Business Plan v3 says ~£30k with £20k superseded, and the Noticeboard already lists this as a decision awaiting Rachel. The site should present ~£30k as current and mark £20k superseded until she rules; flagging because the Wares currently shows both without that framing.

---

## G. What's solid — leave it alone

The five questions and their places; the two-TOM settlement and the allocation test (consistent across Town Hall, Records Room, Wares, Cartographer's Table); the WHEN two-loops and the dominance diagnostic; the Millwheel as the flywheel with the corrected funnel logic; the Construct's staged-hypothesis claims discipline; and the evidence thresholds. These are coherent and well-sourced. The audit found no reason to reopen any of them.

---

## Suggested order if you action it

1. The four highs first: settle the Black Egg (A1/F1), fix the £225k/£250k contradiction (A2), finish the Lexicon/source-of-truth piece (B1), and present the TOM price consistently (F5).
2. Then the quick logic fixes: circular link (A3), empty anchors (A4), PP-04 dropped quote (A5), picture-book back link (A6).
3. Then de-duplicate (C1 especially), relabel the two TOM destinations (D1), and reconcile the naming/dates (D2–D5).
4. Cosmetics last (E).

Nothing here is structural. It's a sound site with a handful of real contradictions and a tail of tidying.

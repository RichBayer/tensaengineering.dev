# Utility Tool Experiment Plan

## Goal
Build a simple, useful, client-side tool on tensaengineering.dev to attract organic search traffic (inspired by utility sites that rank for practical queries + ads). Keep everything low-maintenance and static. Must be easy to build and maintain.

## Status
**Linux calculator / disk estimator direction — SCRAPPED (2026-10-25).**

## Current direction (decided)
**Local LLM model recommender (specs in → models that fit)**

### Concept
User enters their GPU VRAM (or unified memory) and optionally a few preferences. The page returns a curated list of models that fit, with short notes on what each is good at (general chat, coding, uncensored, long context, etc.) and restricted vs unrestricted variants where relevant.

### Why this version
- Matches real search intent around “what can I run on my GPU.”
- Can stand out from pure math calculators by focusing on practical recommendations and honest notes rather than giant unfiltered lists.
- Periodic list updates are manageable if the set stays curated.
- Strong fit with existing local-first AI content.

### Differentiation notes
Most existing tools are either model-first calculators or large hardware-first lists. This one prioritizes a shorter, opinionated, well-explained set with strengths and restricted/unrestricted flags.

## Technical approach
- Static HTML + vanilla JavaScript (no backend).
- Curated model list (JSON or JS object) that can be updated periodically.
- Simple fit logic (pre-computed ranges or basic formula for common quants).
- New page using existing site templates.
- Transparent assumptions shown on the page.
- Internal links from local-first AI and related knowledge-base pages.
- Add to sitemap and request indexing after publishing.
- Keep planning docs on this branch so they don’t go live.

## Next actions (one at a time)
1. ~~Choose direction.~~ Done — specs-in models-out recommender.
2. Sketch the page: inputs, outputs, example model notes, page title.
3. Define the initial curated model list and fit ranges.
4. Build and test on this branch (using existing templates).
5. Merge to main only when ready.

## Notes
- Branch: `docs/linux-calculator-toolkit-plan` (name kept for history).
- Site currently has near-zero non-brand clicks; this remains an experiment.

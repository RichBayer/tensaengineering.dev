# Utility Tool Experiment Plan

## Goal
Build a simple, useful, client-side tool on tensaengineering.dev to attract organic search traffic (inspired by utility sites that rank for practical queries + ads). Keep everything low-maintenance and static. Must be easy to build and maintain.

## Status
**Linux calculator / disk estimator direction — SCRAPPED (2026-10-25).**

## Current direction (decided)
**Local LLM model recommender (specs in → models that fit)**

### Concept
User enters their GPU VRAM (or unified memory). The page returns a curated list of models that fit, with short notes on what each is good at and restricted vs unrestricted variants where relevant. Includes a short educational intro explaining VRAM, quantization, and context.

### Page title / H1
**What local AI model can run on my PC?**

### Why this version
- Matches real search intent and beginner experience (many people don’t know about VRAM at first).
- Educational angle fits the site’s knowledge-base style.
- Can stand out from pure math calculators with practical notes.
- Periodic list updates are manageable if the set stays curated.

## Technical approach
- Static HTML + vanilla JavaScript (no backend).
- Curated model list (JSON or JS object) that can be updated periodically.
- Simple fit logic (pre-computed ranges or basic formula for common quants).
- New page using existing site templates.
- Short intro section + transparent assumptions.
- Internal links from local-first AI and related knowledge-base pages.
- Add to sitemap and request indexing after publishing.
- Keep planning docs on this branch so they don’t go live.

## Next actions (one at a time)
1. ~~Choose direction and page structure.~~ Done.
2. Define the initial curated model list and fit ranges.
3. Build and test on this branch (using existing templates).
4. Merge to main only when ready.

## Notes
- Branch: `docs/linux-calculator-toolkit-plan` (name kept for history).
- Site currently has near-zero non-brand clicks; this remains an experiment.

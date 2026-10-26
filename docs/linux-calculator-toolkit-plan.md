# Utility Tool Experiment Plan

## Goal
Build a simple, useful, client-side tool on tensaengineering.dev to attract organic search traffic (inspired by utility sites that rank for practical queries + ads). Keep everything low-maintenance and static. Must be easy to build and maintain.

## Status
**Linux calculator / disk estimator direction — SCRAPPED (2026-10-25).**

Reason: People searching “linux calculator” (and related terms) are mostly looking for how to open the built-in GUI calculator or how to use terminal tools like `bc`/`calc`. Linux already has `du`/`ncdu`/file managers for disk usage. A pure web estimator or math calculator has weak unique value and limited search intent match.

## Current direction (decided)
**Local LLM VRAM calculator**

### Why this one
- Keyword Planner showed 100–1K volume for `vram calculator` / `llm vram calculator` with low competition.
- Clear search intent: people want to know how much VRAM is needed to run a specific model locally (weights + KV cache + context + overhead).
- Strong fit with existing site content (local-first AI, NeuroCore, knowledge base).
- Not something users can do easily with a built-in command; requires the right formula and assumptions.
- Existing tools prove demand, but a simple, transparent, well-explained version on this site can still be useful.

## Technical approach
- Static HTML + vanilla JavaScript (no backend).
- New page using existing site templates.
- Transparent formula and assumptions shown on the page.
- Internal links from local-first AI and related knowledge-base pages.
- Add to sitemap and request indexing after publishing.
- Keep planning docs on this branch so they don’t go live.

## Next actions (one at a time)
1. ~~Choose a new first tool idea.~~ Done — Local LLM VRAM calculator.
2. Sketch the tool (inputs, outputs, formula/assumptions, page title).
3. Build and test on this branch (using existing templates).
4. Merge to main only when ready.
5. After publish: request indexing, monitor impressions, iterate.

## Notes
- Branch: `docs/linux-calculator-toolkit-plan` (name kept for history; content is now general utility tool planning).
- Site currently has near-zero non-brand clicks; this remains an experiment.

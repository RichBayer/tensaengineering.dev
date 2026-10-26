# Linux Calculator Toolkit Plan

## Goal
Build a small set of simple, accurate, client-side Linux-related calculators on tensaengineering.dev to attract organic search traffic (inspired by utility sites that rank for practical queries + ads). Keep everything low-maintenance and static.

## Why this direction
Keyword Planner research (US, Oct 2025–Sep 2026):
- `linux calculator`: 100–1K monthly searches, low competition, with related terms also showing volume (`calc linux`, `linux calc`, etc.).
- Compared to VRAM and power-cost ideas, this had the broadest related keyword expansion.
- Fits existing site content (Linux diagnostics, local-first AI, homelab-adjacent topics).

## Toolkit idea
Start with 1–3 focused calculators on a new page (or small set of pages), then expand based on Search Console impressions.

### Initial candidates (pick order after more research if needed)
1. Disk / directory size estimator (practical for Linux users)
2. Simple unit converter (KB/MB/GB/TB, binary vs decimal)
3. Basic power / electricity cost estimator for a Linux machine or server

All calculations must be transparent (show formula + assumptions) and accurate for the stated use case.

## Technical approach
- Static HTML + vanilla JavaScript (no backend).
- New page(s) under something like `/tools/` or `/knowledge-base/tools/`.
- Internal links from existing Linux diagnostics and related knowledge-base pages.
- Add to sitemap after publishing.
- Request indexing in Search Console once live.

## Next actions (one at a time)
1. Decide the first calculator to implement.
2. Sketch the page structure, inputs, formula, and target title/H1.
3. Build and test the page on this branch.
4. Merge to main only when ready (so it does not go live early).
5. After publish: request indexing, monitor impressions, iterate.

## Notes
- Branch: `docs/linux-calculator-toolkit-plan` (kept off main so GitHub Pages does not publish this planning content).
- Site currently has near-zero non-brand clicks; this is an experiment to test utility-page traffic.

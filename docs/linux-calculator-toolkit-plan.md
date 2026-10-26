# Utility Tool Experiment Plan

## Goal
Build a simple, useful, client-side tool on tensaengineering.dev to attract organic search traffic (inspired by utility sites that rank for practical queries + ads). Keep everything low-maintenance and static. Must be easy to build and maintain.

## Status
**Linux calculator / disk estimator direction — SCRAPPED (2026-10-25).**

Reason: People searching “linux calculator” (and related terms) are mostly looking for how to open the built-in GUI calculator or how to use terminal tools like `bc`/`calc`. Linux already has `du`/`ncdu`/file managers for disk usage. A pure web estimator or math calculator has weak unique value and limited search intent match.

## Why we considered it
Keyword Planner showed 100–1K volume for broader “linux calculator” terms with low competition, but deeper checks showed the intent was not a web tool.

## Next direction
Revisit other simple tool ideas that:
- Match real search demand
- Can’t already be done easily with a built-in command or app
- Fit the existing site (Linux diagnostics, local-first AI, projects)
- Are client-side only and easy to maintain

## Technical approach (unchanged)
- Static HTML + vanilla JavaScript (no backend).
- New page(s) using existing site templates.
- Internal links from related knowledge-base pages.
- Add to sitemap and request indexing after publishing.
- Keep planning docs on this branch so they don’t go live.

## Next actions (one at a time)
1. Choose a new first tool idea based on keyword research + unique value.
2. Validate search intent for the new idea.
3. Sketch the tool (inputs, outputs, formula/assumptions).
4. Build and test on this branch.
5. Merge to main only when ready.

## Notes
- Branch: `docs/linux-calculator-toolkit-plan` (name kept for history; content is now general utility tool planning).
- Site currently has near-zero non-brand clicks; this remains an experiment.

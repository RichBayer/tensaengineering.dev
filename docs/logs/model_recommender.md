# Local AI Model Recommender — V2 work log

## Purpose
Build a low-maintenance, static, beginner-friendly tool that suggests curated local AI models based on GPU VRAM or unified memory, with clear fit assumptions and educational context.

## Gates
| Gate | Status | Evidence and limits |
| --- | --- | --- |
| M1: original tool direction recovered | PASS | Branch `docs/linux-calculator-toolkit-plan`, file `docs/linux-calculator-toolkit-plan.md`: Linux disk calculator scrapped; Local LLM model recommender chosen |
| M2: baseline plan and model suitability revalidated | OPEN | Original curated models and Q4 fit estimates are historical proposals, not current verified recommendations |
| M3: implementation branch state and page design confirmed | OPEN | Named planning branch exists; current local state and divergence must be checked before any edits |
| M4: static UI, fit logic and educational claims tested | OPEN | Browser/mobile, model-fit caveats and accessibility required |
| M5: publication, discovery links and closeout verified | OPEN | Only after owner review/approval; sitemap and indexing outcomes separately verified |

## Last session
2026-11-21: Owner authorized a dedicated V2 resume path for the previously parked recommender. Verified original plan on `docs/linux-calculator-toolkit-plan`: title "What local AI model can run on my PC?", static HTML/vanilla JS, small curated model set and explanations of VRAM, quantization and context. The plan is not present on `main`; its branch name reflects the discarded Linux calculator idea. No tool or public page was built in this session. Owner's `main website_seo` safety check PASS on clean synced `8653023` before V2 routing writes.

## Decisions in force
- Treat the historical branch plan as design context, not approval of obsolete model recommendations or proof of fit.
- Keep the experience static and maintainable; include approximate fit/headroom and runtime/context disclaimers.
- Do not rename/delete the historical planning branch or merge outdated shared files blindly.
- No production page, navigation or sitemap change until Rich approves a reviewed implementation.

## Next
State: lane opened on `main` for future selection; implementation branch has not been reconciled and current local working state is unverified. Owner's `main` was clean/synced at `8653023` before connector changes; fast-forward after the routing batch.
Next session: read `docs/linux-calculator-toolkit-plan.md` on `docs/linux-calculator-toolkit-plan`; check local state and divergence, compare current local model requirements/availability with historical Q4 examples, and present a compact up-to-date candidate matrix and implementation plan for owner approval. Use `main` standards and avoid copying stale branch process docs. For a log save run main session check with `model_recommender`; for edits to the planning branch run a branch-specific check without claiming main is safe.

## Read before working
- `docs/planning/page_inventory.md` — current public pages and tools.
- `docs/planning/seo_topic_map.md` — search intent and local-first AI.
- `docs/planning/website_information_architecture.md` — site role.
- `docs/planning/content_style_guide.md` — precise public claims.
- `docs/planning/internal_linking_strategy.md` — relevant discovery paths.
- `docs/planning/content_source_map.md` — factual source ownership.
Additionally read branch `docs/linux-calculator-toolkit-plan`:`docs/linux-calculator-toolkit-plan.md` as the original tool plan.

## Closeout updates
2026-11-21: Historical tool plan promoted from parked idea to a selectable V2 lane; no implementation/public edits.

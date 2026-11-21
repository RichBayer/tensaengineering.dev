# Website SEO — V2 work log

## Purpose
Improve non-branded discoverability and engineering vocabulary, one page/subject plus its glossary definitions at a time. Done means source-backed language and working reader/navigation paths, with publication verified separately from indexing.

## Gates
| Gate | Status | Evidence and limits |
| --- | --- | --- |
| W1: repository cleanup closed and prior publication preserved | PASS | `876581a`, `18a8ffe`, `5845e58`, Pages #55; owner confirmed live articles |
| W2: pre-terminology GSC baseline located | PASS | `docs/planning/seo_topic_map.md` → `November 20, 2026 - Pre-Terminology SEO Baseline`; 28 days Oct 21–Nov 17, via Windsor.ai; 298 impressions, 0 clicks, 10.87 average position. Do not invent a new baseline |
| W3: vocabulary and engineering facts verified | OPEN | Review Nov 19 marketing audit and source repos before new claims |
| W4: target page and glossary edited together | OPEN | Preserve URLs/anchors, current/planned capabilities; no changes authorized by this log alone |
| W5: content, links and publish/index state independently verified | OPEN | Local link/fragment, page/desktop/mobile, Pages and GSC checks not run for new pass |

## Last session
2026-11-21: Read-only V2 migration review mapped public HTML, assets, metadata, glossary script and documentation ownership. No new public content changed. Cleanup closeout remains finished. Reviewer-informed V2 corrections are staged on `docs/website-v2-continuity-20261121`, not yet merged or locally validated.

## Decisions in force
- 2026-11-21: use V2 source routing, not duplicate content standards or repeat completed audits.
- Existing website lane is `main`; changed production HTML on `main` triggers GitHub Pages.
- Next unit: agent harness / harness engineering on `projects/driveline.html`, `knowledge-base/controlled-ai-systems/from-coding-agents-to-supervised-engineering.html`, and matching `glossary/index.html`. Series-specific CSS is `assets/css/driveline-kb-series.css`. Update affected `data-definition` text in each public page when a glossary definition changes.
- Avoid: broken glossary anchors, invented product capabilities, URL churn, unsupported SEO/indexing success claims.

## Next
State: intended content branch `main` after migration; last owner-confirmed Legion `main` clean at `876581a`. **Current local state and uncommitted files not checked in this V2 session.** Remote migration branch is separate and has not been integrated.
After V2 integration and local sync: **reuse** the Nov 20 baseline from `docs/planning/seo_topic_map.md`; Windsor.ai reports Search Console metrics, and `docs/planning/search_indexing_strategy.md` owns indexing state. Read `RichBayer/tensa-marketing/docs/planning/grok_bot_pilot_20261119.md`, verify Agent Operations evidence, then propose one coherent set of page+glossary edits for Rich's approval. Later compare a matching 28-day GSC window without claiming causation. Do not repeat prior cleanup or SEO publication audits.

## Read before working
- `docs/planning/seo_topic_map.md` — search intent and priority.
- `docs/planning/glossary_strategy.md` — term choices and anchor behavior.
- `docs/planning/page_inventory.md` — current routes/status.
- `docs/planning/content_source_map.md` — factual source requirements.
- `docs/planning/content_style_guide.md` — claims and public voice.
- `docs/planning/internal_linking_strategy.md` — preferred destinations.
Follow these to the actual target HTML, glossary, scripts, article template and authoritative project evidence as needed.

## Closeout updates
On accepted V2 integration: remove migration staging note, capture validated branch and local synchronization, change gates only with evidence; menu path remains open.
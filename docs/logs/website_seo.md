# Website SEO — V2 work log

## Purpose
Improve non-branded discoverability and engineering vocabulary, one page/subject plus its glossary definitions at a time. Done means source-backed language and working reader/navigation paths, with publication verified separately from indexing.

## Gates
| Gate | Status | Evidence and limits |
| --- | --- | --- |
| W1: repository cleanup closed and prior publication preserved | PASS | `876581a`, `18a8ffe`, `5845e58`, Pages #55; owner confirmed live articles |
| W2: pre-terminology GSC baseline located | PASS | `docs/planning/seo_topic_map.md` → `November 20, 2026 - Pre-Terminology SEO Baseline`; 28 days Oct 21–Nov 17, via Windsor.ai; 298 impressions, 0 clicks, 10.87 average position. Do not invent a new baseline |
| W3: vocabulary and engineering facts verified | PASS | Nov 19 marketing audit and Agent Operations task-packet/review evidence checked; manual versus planned capabilities preserved |
| W4: target page and glossary edited together | PASS | Agent harness unit at `7ccd038`; consolidated terminology/discovery batch at `f4bb2ef` (7 HTML files + sitemap). Local script verified exact Git blobs/anchors, local links/fragments and sitemap; owner reviewed all seven changed pages visually. |
| W5: content, links and publish/index state independently verified | OPEN | Pages [run 44942344575](https://github.com/RichBayer/tensaengineering.dev/actions/runs/44942344575) SUCCESS for `f4bb2ef`; local page/layout checks owner PASS. Production crawl/fragment validation, mobile-specific coverage, GSC indexing and rankings remain unverified. |

## Last session
2026-11-21: V2 integration at `ccbd4c1` validated (Grok/Claude PASS, both local session checks PASS, Pages run `44935871438` success, script URLs 404). Context Engineering article retitled and moved at `0d887d9`: [Pages run 44937807731](https://github.com/RichBayer/tensaengineering.dev/actions/runs/44937807731) SUCCESS; owner confirmed new live article loads, updated Knowledge Base label and local old-URL browser redirect. Checked public HTML/sitemap with `git grep` for old slug: no references. Full production link/fragment and GSC indexing validation remain unverified.

## Decisions in force
- 2026-11-21: use V2 source routing, not duplicate content standards or repeat completed audits.
- Existing website lane is `main`; changed production HTML on `main` triggers GitHub Pages.
- Agent harness / harness engineering unit published at `7ccd038` on Driveline, supervised-engineering article, and glossary. Future term changes must keep affected tooltip `data-definition`, anchors and page metadata synchronized.
- Canonical Context Engineering article URL is `/knowledge-base/ai-operations/context-engineering-ai-project-continuity.html`; old `/knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html` remains as a browser-redirect fallback (not an HTTP 301). Updated metadata, JSON-LD, sitemap and public links in migration `0d887d9`.
- Avoid: broken glossary anchors, invented product capabilities, unnecessary URL churn, unsupported SEO/indexing success claims.

## Next
State: site-wide industry terminology and discovery batch published on `main` as `f4bb2ef`; Pages run `44942344575` SUCCESS. Owner checked seven local preview pages; all eight changed files passed review and local structural checks. No known pending public HTML edits. After this connector-only log save, Rich's local `main` needs a fast-forward before further local work.
Next session: do not repeat the completed terminology batch. Check production links/fragments and genuine mobile/responsive behavior only as needed, then monitor Google Search Console using the saved Oct 21–Nov 17 28-day baseline (298 impressions, 0 clicks, average position 10.87) against a later matching 28-day window; report indexing/query changes without assuming the edits caused them. Blog is a separate V2 lane. Keep W5 OPEN until production and indexing evidence exists.

## Read before working
- `docs/planning/seo_topic_map.md` — search intent and priority.
- `docs/planning/glossary_strategy.md` — term choices and anchor behavior.
- `docs/planning/page_inventory.md` — current routes/status.
- `docs/planning/content_source_map.md` — factual source requirements.
- `docs/planning/content_style_guide.md` — claims and public voice.
- `docs/planning/internal_linking_strategy.md` — preferred destinations.
Follow these to the actual target HTML, glossary, scripts, article template and authoritative project evidence as needed.

## Closeout updates
2026-11-21: Agent harness terminology pass CLOSED for editing/publishing: commit `7ccd038` on `main` (3 public HTML pages + V2 operating rules + this log), Pages deployment [run 44940287637](https://github.com/RichBayer/tensaengineering.dev/actions/runs/44940287637) SUCCESS. Owner Driveline screenshot, combined diff reviewed, redundant sentence removed, 156 local internal links/anchors PASS. Complete live wording/responsive review and GSC indexing not independently established; W5 stays OPEN. Next owner-approved direction: batch remaining site-wide terminology/SEO improvements in one consolidated pass; do not redo finished work.
2026-11-21: Context Engineering migration closeout: `0d887d9`, Pages SUCCESS, owner live-page and navigation confirmation, browser redirect tested locally, old-slug grep clear. Not a verified HTTP 301 and not proof of indexing or ranking improvement.
2026-11-21: Site-wide SEO terminology/discovery closeout: owner-approved guarded local batch changed 7 HTML pages and `sitemap.xml` (107 additions, 16 deletions). Added `AGENTS.md`/`CLAUDE.md` context guidance, agentic/vibe coding comparisons, spec-driven terminology, homepage and Knowledge Base discovery wording, glossary and relevant links, and sitemap `lastmod` entries for changed pages. Exact original Git blobs and text anchors checked; hrefs/fragments and sitemap XML passed locally; `git diff --check` clean; consolidated patch reviewed; owner reported local previews load/look good. Owner approved and pushed `f4bb2ef` to `main`; GitHub Pages [run 44942344575](https://github.com/RichBayer/tensaengineering.dev/actions/runs/44942344575) completed SUCCESS. This verifies deployment, not Google indexing or SEO performance. W5 remains OPEN.
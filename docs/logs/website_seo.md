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
| W5: content, links and publish/index state independently verified | OPEN | Production read-only Python crawl: 26 pages, 961 internal references, 17 assets, zero issues or redirects, no page cap; checks included discovered fragment targets. Owner Chrome 400px responsive review of homepage, Knowledge Base and glossary PASS after CSS correction `1ee0a99`; owner screenshot shows Pages deployment #74 SUCCESS on `main`. Native-device behavior, full breakpoint coverage, and GSC indexing/rankings remain unverified. |

## Last session
2026-11-21: Verified production crawl of 26 pages / 961 internal references / 17 assets: 0 detected issues, 0 redirects, page cap not reached. Chrome DevTools 400px checks: homepage and glossary visually PASS; Knowledge Base revealed blue default inline links. Scoped 13-line `styles.css` correction locally applied and reviewed (`git diff --check` PASS), owner preview confirmed green underlined links and readable cards. Owner pushed `1ee0a99` to `main`; screenshot shows latest Pages deployment #74 SUCCESS. V2 session check PASS on synced clean `main` before this connector log save; this log save will put local `main` behind until fast-forwarded.

## Decisions in force
- 2026-11-21: use V2 source routing, not duplicate content standards or repeat completed audits.
- Existing website lane is `main`; changed production HTML on `main` triggers GitHub Pages.
- Agent harness / harness engineering unit published at `7ccd038` on Driveline, supervised-engineering article, and glossary. Future term changes must keep affected tooltip `data-definition`, anchors and page metadata synchronized.
- Canonical Context Engineering article URL is `/knowledge-base/ai-operations/context-engineering-ai-project-continuity.html`; old `/knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html` remains as a browser-redirect fallback (not an HTTP 301). Updated metadata, JSON-LD, sitemap and public links in migration `0d887d9`.
- Avoid: broken glossary anchors, invented product capabilities, unnecessary URL churn, unsupported SEO/indexing success claims.

## Next
State: terminology/discovery batch `f4bb2ef` and mobile link-color fix `1ee0a99` published. Production internal-link/fragment crawl PASS (26 pages, 961 references, 17 assets); sampled 400px responsive layouts PASS after fix. No known pending public page edits. Owner's clean local `main` was synchronized at `1ee0a99` before this connector log update; **fast-forward local `main` after this save** before any local work.
Next session: monitor Google Search Console indexing, search queries and performance, comparing later equivalent 28-day periods against Oct 21–Nov 17 (298 impressions, 0 clicks, avg. position 10.87). Do not imply ranking gains or causation without evidence. Only expand responsive testing if a concrete issue arises; native-device/touch behavior and full breakpoint coverage remain unverified. Blog remains a separate V2 lane. W5 stays OPEN pending indexing/performance evidence.

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
2026-11-21: Production/mobile verification closeout: one read-only live crawl checked 26 pages, 961 internal references, 17 assets, zero detected broken targets/anchors or redirects; limited to crawler coverage, not a guarantee for all interactions. Owner reviewed homepage, Knowledge Base and glossary with Chrome responsive emulation (400px); corrected default-blue Knowledge Base introductory paragraph links using a 13-line scoped CSS addition. Local preview and entire `styles.css` diff owner-confirmed; `git diff --check` clean; commit `1ee0a99` pushed to `main`. Owner screenshot shows latest Pages run #74 green SUCCESS; this is deployment evidence, not Google indexing or a native-device test. W5 remains OPEN for GSC evidence.
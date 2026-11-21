# Blog — V2 work log

## Purpose
Prove TENSA's practical Blog with an approved, sourced AI Coding article, then a category page and Blog home, keeping all unpublished paths out of navigation and sitemap.

## Gates
| Gate | Status | Evidence and limits |
| --- | --- | --- |
| B1: Article #1 topic and source packet approved | PASS | 2026-10-11 decision in Blog branch `docs/planning/blog_strategy.md` |
| B2: current provider/account statements reverified | OPEN | Official sources and account wording need fresh checks before publication |
| B3: branch updated from main without losing approved Blog research | OPEN | The Blog branch has newer `blog_*` files and older shared docs; integrate main locally before publication, not after every log save |
| B4: proof article drafted and reviewed | OPEN | No public Blog HTML exists on main |
| B5: category/home, links/metadata and publication checked | OPEN | No Blog URLs should enter public nav or sitemap until approved real pages |

## Last session
2026-11-21: V2 read-only audit inspected actual site and the newer Blog branch's approved Article #1 source packet. No Blog public pages or plan rewrites performed. Independent reviewers found gaps; a bounded V2 correction is staged on `docs/website-v2-continuity-20261121`, not yet merged.

## Decisions in force
- Approved October 11 article: `/blog/ai-coding/why-ai-coding-uses-up-your-usage-limit.html`; do not choose a historical candidate title or restart finished reader research.
- Source packet: usage mechanics first; continuity/repeated work is qualified secondary reporting. No unsupported savings numbers or assumptions about plan/chat usage.
- The three Blog-specific files (`blog_strategy.md`, `blog_reader_experience.md`, `blog_engagement_strategy.md`) are authoritative on `feature/blog-public-foundation`; shared `seo_topic_map.md`, `content_style_guide.md` and `page_inventory.md` are newer on `main` until reconciled.
- The **approved Article #1 draft text** is already written: Blog-branch `docs/planning/blog_strategy.md`, under `Source Packet: Article #1` → `Approved draft text, 2026-10-11` (about lines 1219–1340). The document exceeds connector whole-file limits; read that section in chunks or locally, do not regenerate from scratch. Delete the draft block **only after** the published article HTML exists and approval allows source-file editing.
- No unmeasured usage/cost-saving claims or teaser for a planned comparison; confirm ChatGPT plan-limit and Grok Usage account wording on publication day.
- Avoid: overwriting divergent branch work, unverified provider claims, publishing empty categories, early nav/sitemap additions, or launching RSS/comments/newsletter/affiliates.

## Next
State: active content branch `feature/blog-public-foundation`; it diverges from `main`. Last local confirmation on 2026-11-21 listed this branch, but **its current working tree, ahead/behind and uncommitted files are unknown**. No local branch merge is assumed.
After V2 merge and Rich's local status: merge current `main` **into** `feature/blog-public-foundation` locally, preserve its approved Blog-specific research/draft, validate shared standards and do not rebase, force-push or merge unfinished Blog into `main`. Then reread the approved draft, recheck official source pages, four GitHub issues and provider/account wording; build Article #1, then category and Blog home, subject to Rich's editing and publication approval.

## Read before working
- `docs/planning/blog_strategy.md` — **read on Blog branch**, approved source packet.
- `docs/planning/blog_reader_experience.md` — **Blog branch**, article and index patterns.
- `docs/planning/blog_engagement_strategy.md` — **Blog branch**, CTA/disclosures.
- `docs/planning/seo_topic_map.md` — read newer **main** version until merged, topic intent.
- `docs/planning/content_style_guide.md` — read newer **main** version until merged, public voice and claims.
- `docs/planning/content_source_map.md` — page-specific evidence and linked project claims.
Follow to page inventory, indexing strategy, internal links, actual HTML and official sources when required.

## Closeout updates
After verified branch reconciliation and approved Article #1 publication, record commit evidence and adjust next path. Do not close Blog lane while launch remains incomplete.
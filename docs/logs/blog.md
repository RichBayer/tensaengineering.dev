# Blog — V2 work log

## Purpose
Prove TENSA's practical Blog with an approved, sourced AI Coding article, then a category page and Blog home, keeping all unpublished paths out of navigation and sitemap.

## Gates
| Gate | Status | Evidence and limits |
| --- | --- | --- |
| B1: Article #1 topic and source packet approved | PASS | 2026-10-11 decision in Blog branch `docs/planning/blog_strategy.md` |
| B2: current provider/account statements reverified | OPEN | Official sources and account wording need fresh checks before publication |
| B3: branch divergence resolved without losing Blog research | OPEN | `feature/blog-public-foundation` diverges from main (11 commits exclusive on branch / 30 on main at V2 review) |
| B4: proof article drafted and reviewed | OPEN | No public Blog HTML exists on main |
| B5: category/home, links/metadata and publication checked | OPEN | No Blog URLs should enter public nav or sitemap until approved real pages |

## Last session
2026-11-21: V2 read-only audit inspected actual site and the newer Blog branch's approved Article #1 source packet. No Blog public pages or plan rewrites performed. V2 staging is isolated on `docs/website-v2-continuity-20261121`.

## Decisions in force
- Approved October 11 article: `/blog/ai-coding/why-ai-coding-uses-up-your-usage-limit.html`; do not choose a historical candidate title or restart finished reader research.
- Source packet: usage mechanics first; continuity/repeated work is qualified secondary reporting. No unsupported savings numbers or assumptions about plan/chat usage.
- Blog plan authority is on `feature/blog-public-foundation`, not older `main` copies.
- Avoid: overwriting divergent branch work, unverified provider claims, publishing empty categories, early nav/sitemap additions, or launching RSS/comments/newsletter/affiliates.

## Next
State: active content branch `feature/blog-public-foundation`; it diverges from `main`. Last local confirmation on 2026-11-21 listed this branch, but **its current working tree, ahead/behind and uncommitted files are unknown**. No local branch merge is assumed.
After V2 migration is merged and Rich provides local status, reconcile Blog branch against main while retaining Blog-specific planning. Then recheck official source pages, four GitHub issues and current account-screen wording; build approved Article #1 followed by category and Blog home, with Rich's approval before edits/publication.

## Read before working
- `docs/planning/blog_strategy.md` — **read on Blog branch**, approved source packet.
- `docs/planning/blog_reader_experience.md` — **Blog branch**, article and index patterns.
- `docs/planning/blog_engagement_strategy.md` — **Blog branch**, CTA/disclosures.
- `docs/planning/seo_topic_map.md` — **Blog branch**, topic intent.
- `docs/planning/content_style_guide.md` — public voice and claims; check main and intended branch state.
- `docs/planning/content_source_map.md` — page-specific evidence and linked project claims.
Follow to page inventory, indexing strategy, internal links, actual HTML and official sources when required.

## Closeout updates
After verified branch reconciliation and approved Article #1 publication, record commit evidence and adjust next path. Do not close Blog lane while launch remains incomplete.
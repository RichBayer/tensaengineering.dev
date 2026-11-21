# TENSA Website: Now

Updated: 2026-11-21 (post-cleanup)
Two lanes: website and Blog. Ask Rich which lane unless his request already selects one.

## Completed — do not repeat without a new concrete defect

- **Repository cleanup CLOSED:** final handoff closeout `876581a` on GitHub `main` (2026-11-21). Knowledge Base editorial, teaching, and navigation guidance was consolidated into the existing `docs/planning/content_style_guide.md` and `docs/planning/knowledge_base_article_template.md` at `18a8ffe`; no duplicate standard, public article, CSS, sitemap, or unrelated file was changed.
- **Historical branch preservation:** the two final KB branches were archived on GitHub and retired: `repair/kb-context-article-reading-pass` (`51fd594e` -> `archive/website-20261121-kb-context-article-reading`) and `docs/long-form-kb-style` (`cc4ed242` -> `archive/website-20261121-kb-long-form-style`). Prior archival/retirement, four obsolete worktrees, merged branches, and reconciled stash were already completed. Do not repeat branch archaeology or cleanup.
- **Publication already validated:** the 11-file reconciliation was published at `5845e58`, GitHub Pages #55 passed, and Rich confirmed both live articles. Full patch, HTML/CSS/metadata, 283 links, 78 fragments, sitemap and AO evidence already reviewed. Prior closeout `7b19003`, handoff `d521245`. Do not restart publication or source audits.
- **Confirmed final local state:** Legion `main` clean and synchronized at `876581a`; local branches listed were `main` and `feature/blog-public-foundation`. The Local LLM Recommender is approved future work; its planning branch need not be checked until resuming that task.
- **Outside cleanup:** live copy-button behavior and search indexing remain unverified. Neither blocks the completed repository closeout.

## Website lane — next active priority

- **NEXT:** Resume the approved **industry-vocabulary / non-branded SEO pass**. First capture a Google Search Console baseline; consult the November 19 TENSA Marketing audit in `RichBayer/tensa-marketing/docs/planning/grok_bot_pilot_20261119.md`, then verify current engineering source evidence. Work one subject/page and its matching glossary definitions together.
- **Next subject:** Agent harness / harness engineering terminology on TENSA Driveline and supervised-engineering pages. Preserve URLs, existing glossary anchors, TENSA naming, and explicit current-versus-planned capability boundaries. Do not claim unverified functionality.
- **Already done:** Context Engineering article and matching glossary terminology published and owner-confirmed November 20 (`e9383cc`); four Driveline engineering articles published November 3 (`7a849d3`). No need to redo these.
- **Read for this pass:** `docs/planning/seo_topic_map.md`, `glossary_strategy.md`, `page_inventory.md`, `content_source_map.md`, `content_style_guide.md` and relevant authoritative project sources. Current KB article format is in `knowledge_base_article_template.md`.
- **Visibility:** Windsor.ai is connected to Search Console for `sc-domain:tensaengineering.dev`; 24-URL sitemap fetched. Indexing for new articles is not confirmed; source of record: `docs/planning/search_indexing_strategy.md`. Keep the 90-day traffic plan and current website/Blog queues.
- **Parked afterward:** Local LLM Model Recommender, “What local AI model can run on my PC?”, using `docs/linux-calculator-toolkit-plan` and its approved `docs/linux-calculator-toolkit-plan.md`; verify current model specs and memory-fit assumptions before build/test, without restarting planning. AI Operations category/index restructuring follows on `feature/kb-ai-operations-index` (not created).

## Blog lane — separate approved work

- Work on existing `feature/blog-public-foundation`, not a new Blog branch. No Blog implementation is active yet.
- **NEXT:** Build approved Article #1 from the Source Packet in `docs/planning/blog_strategy.md`: `/blog/ai-coding/why-ai-coding-uses-up-your-usage-limit.html`. Text, outline and sources were approved October 11; do not restart research.
- Before publishing, directly recheck official sources, four GitHub issues, ChatGPT plan limits and Grok Usage wording. Do not make a measured claim before the planned comparison. Remove the draft block from the Source Packet after the page exists.
- Read `blog_strategy.md`, `blog_reader_experience.md`, `blog_engagement_strategy.md` and `seo_topic_map.md` from the **Blog branch**, whose copies are newer than `main`. Build article, validate, then category and Blog home. No Blog navigation/sitemap entries before validated public pages.

## Resume

Read `docs/ai-operations/operating_rules.md` and only the selected lane's named documents. Do not reopen the completed cleanup, legacy branches, stashes, worktrees, publication audits, or documentation-standard integration. For a GitHub connector commit, Rich's local repository must be fast-forwarded afterward.

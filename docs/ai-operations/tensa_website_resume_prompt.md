# TENSA Website: Now

Updated: 2026-11-21
Two lanes. Ask Rich which one before reading anything else.

## Website lane

- Active priority (owner Nov 20): industry vocabulary / SEO wording pass. First capture Search Console baseline; consult the Nov 19 TENSA Marketing audit (`RichBayer/tensa-marketing`, `docs/planning/grok_bot_pilot_20261119.md`) and verify current engineering evidence. Revise one subject/page and matching glossary entries together; retain existing anchors, URLs, branding and claim boundaries. First terminology batch published and verified November 20, 2026: Context Engineering article and matching glossary definition, commit e9383cc. Owner confirmed both live pages. Next: Agent harness / harness engineering terminology on Driveline and supervised-engineering pages, with matching glossary changes. Preserve existing URLs, anchors, and implementation-status boundaries. Read `seo_topic_map.md`, `glossary_strategy.md`, page inventory and required source/style docs.
- Completed 2026-11-03: Four Driveline engineering articles published on `main` at `7a849d3`; GitHub Pages run 47 succeeded and Rich confirmed the live pages. The prior single long-form draft is not published.

- Visibility follow-up (2026-11-03): Windsor.ai is connected to Google Search Console for `sc-domain:tensaengineering.dev`. The 24-URL sitemap was fetched successfully. The 90-day traffic plan is recorded in `docs/planning/seo_topic_map.md`; connection and indexing evidence are in `docs/planning/search_indexing_strategy.md`. New article indexing remains unconfirmed. Preserve the existing website and Blog queues.
- Parked next: Local LLM Model Recommender — "What local AI model can run on my PC?"
- Branch: `docs/linux-calculator-toolkit-plan` (historical branch name retained).
- Utility resume: Resume the approved utility plan, verify current model specifications and memory-fit assumptions, then build and test the interactive page. Do not restart planning.
- Read: `docs/linux-calculator-toolkit-plan.md` on the named branch, operating rules, and required website page-planning docs.
- Queued afterward: AI Operations category/index restructuring on `feature/kb-ai-operations-index` (not yet created).

## Repository cleanup - COMPLETE (2026-11-21)
- **Already DONE; NEVER recheck without a new concrete defect:** 11-file reconciliation published at `5845e58`; GitHub Pages #55 PASS; owner visually confirmed both live articles; full patch, HTML/CSS/metadata, 283 links, 78 fragments, sitemap and AO historical evidence already reviewed. Closeout `7b19003` pushed/fast-forwarded to main, branch equality confirmed. Handoff commit `d521245` on main. No repeat publishing checks, source investigation, diff archaeology, SEO work or previously completed Git branch discovery. Live copy-button interaction and search indexing remain unverified but are **outside this cleanup**.
- **Completed analysis; DO NOT repeat:** Rich supplied the November 21 comprehensive audit (baseline `d521245`), reviewing the complete 290-line Knowledge Base reading standard, 616-line long-form guide, current template/glossary strategy, content-operations architecture and branch dispositions. All published-site checks, release evidence and this historic branch analysis are DONE. Only unresolved content question: integrate genuinely missing KB editorial/navigation guidance from `repair/kb-context-article-reading-pass` and `docs/long-form-kb-style` into the *existing* authoritative mainline guides. Do not copy duplicate standards, old CSS, branch snapshots or public article content. Leave Blog and Local LLM Recommender branches untouched.
- **Completed cleanup — NEVER rediscover it:** On Legion the prior approved batch deleted four obsolete worktrees, six merged local branches, four merged remote branches; stash previously reconciled and dropped (`01249b8f`, `git stash list` returned NONE). A second approved batch PASSED preflight, created and pushed five GitHub archive tags (`archive/website-20261121-{career-evidence,driveline-draft,content-operations,driveline-development,kb-reading}`), then deleted three historical remote branches (`career/ahead-public-evidence-20260815`, `content/tensa-driveline-project-page`, `planning/content-operations-architecture`) and two historical local branches (`work/tensa-driveline`, `content/knowledge-base-reading-experience`). Git reported success, and the sole surviving worktree `/mnt/g/ai/projects/tensaengineering.dev` was clean on synchronized `main` at `ff032ea` before this handoff update. Do NOT inspect old worktrees, stash, deleted refs, archive candidates, or repeat any related analysis. Archive tags preserve historical tips.
- **Completed 2026-11-21:** Knowledge Base guidance consolidated on main at `18a8ffe`. Both historical KB branch tips preserved with GitHub archive tags and their working branches retired. No public pages, CSS, sitemap, or unrelated projects changed.
### Final historical KB branch retirement — COMPLETE

- Knowledge Base guidance integration: `18a8ffe` on `main`.
- `repair/kb-context-article-reading-pass` archived at `51fd594e89574fef3d78bfb1b95bfcff3236125c` as `archive/website-20261121-kb-context-article-reading`; historical branch retired.
- `docs/long-form-kb-style` archived at `cc4ed2422f0d2cb497893d7f8ea629ee1ddf0a33` as `archive/website-20261121-kb-long-form-style`; historical branch retired.
- Previously approved publication, stash reconciliation, worktree cleanup, branch retirement and validation remain complete. No further repository cleanup assignment is open.
- Preserve the Blog and Local LLM Recommender branches as active work.

## Blog lane

- Branch: `feature/blog-public-foundation`. Do not start another Blog implementation branch.
- Active: none.
- Next step: build the Article #1 page at the slug below from the approved draft text in the Source Packet: Article #1 section of `blog_strategy.md`, committed 2026-10-11. The text, outline and sources are approved, and it includes the plan-in-chat section, the tips list and the Grok scope. No new research.
- Selected 2026-10-11. Slug: `/blog/ai-coding/why-ai-coding-uses-up-your-usage-limit.html`. Before publishing, read each official source page directly, reopen the four GitHub issues, and re-check the ChatGPT plan limits and Grok Usage wording. Delete the draft block from the packet once the page exists. A measured comparison is planned after the weekly limit reset; until it is run, the post makes no measured claim.
- Do not restart the research from zero. It is recorded in `docs/planning/blog_strategy.md`.
- Order: source packet, text and outline are done. Next the page build, then validation, category page, Blog home.
- The Blog stays on its branch until the proof article validates. No Blog navigation or sitemap entries until real pages exist and validate.
- Read for it, from the Blog branch and not from `main`, whose copies are older: `blog_strategy.md`, `blog_reader_experience.md`, `blog_engagement_strategy.md`, `seo_topic_map.md`, all in `docs/planning/`.

## Preserved active lanes
- Blog (`feature/blog-public-foundation`) and Local LLM Recommender (`docs/linux-calculator-toolkit-plan`) remain approved active work, not cleanup leftovers. Historical refs already archived and retired; no stash task remains.

## To resume
Repository cleanup is complete. Do not restart historical audits, branch archaeology, or retired-branch work. Resume only the selected website or Blog lane using its instructions and operating rules.

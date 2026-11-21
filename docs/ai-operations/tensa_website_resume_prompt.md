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

## Repository reconciliation - PUBLICATION COMPLETE (2026-11-21)
- **Published:** Website reconciliation merged by fast-forward into `main` at `5845e58` on November 21, 2026. GitHub Pages build/deployment #55 succeeded. Rich confirmed both the new Agent Operations Engineering History article and revised Context Engineering article load on the live site. The history article's November 2 evidence was independently reconciled against archived AO experiment records. Earlier four focused Agent Operations articles were already published November 3. The live copy-button interaction was not separately retested; its local implementation validation passed. Search indexing remains unverified.
- **Closeout:** Eleven intended website files published; link/anchor checks, sitemap XML, source review and owner visual review completed. Page inventory marks the history article Live. This handoff records publication; documentation closeout commit/push remains to be completed separately. No public article changes are pending in this release.
- **Exact next action:** Review this documentation diff, then commit and publish the two closeout documents with Rich's authorization. Afterward, separately inventory and reconcile local worktrees, remote branches and the protected stash before returning to the existing SEO terminology queue. Do not assume obsolete branches or stashed files can be deleted without inspection and explicit approval. Preserve `stash@{0}` (`content/knowledge-base-reading-experience`), backups, Driveline KB worktree, and unique Blog/utility work. No reset, force push, deletion or stash mutation. Remote-access recipe: `RichBayer/home-network/docs/remote_access.md` Recipe C.
## Blog lane

- Branch: `feature/blog-public-foundation`. Do not start another Blog implementation branch.
- Active: none.
- Next step: build the Article #1 page at the slug below from the approved draft text in the Source Packet: Article #1 section of `blog_strategy.md`, committed 2026-10-11. The text, outline and sources are approved, and it includes the plan-in-chat section, the tips list and the Grok scope. No new research.
- Selected 2026-10-11. Slug: `/blog/ai-coding/why-ai-coding-uses-up-your-usage-limit.html`. Before publishing, read each official source page directly, reopen the four GitHub issues, and re-check the ChatGPT plan limits and Grok Usage wording. Delete the draft block from the packet once the page exists. A measured comparison is planned after the weekly limit reset; until it is run, the post makes no measured claim.
- Do not restart the research from zero. It is recorded in `docs/planning/blog_strategy.md`.
- Order: source packet, text and outline are done. Next the page build, then validation, category page, Blog home.
- The Blog stays on its branch until the proof article validates. No Blog navigation or sitemap entries until real pages exist and validate.
- Read for it, from the Blog branch and not from `main`, whose copies are older: `blog_strategy.md`, `blog_reader_experience.md`, `blog_engagement_strategy.md`, `seo_topic_map.md`, all in `docs/planning/`.

## Parked

- Remote branch reconciliation: `content/ai-ops-project-context` and `career/ahead-public-evidence-reconcile-20260815` are ancestors of main; Driveline draft matches main; older career copy is superseded by later public pages. Preserve refs until local check and explicit removal approval. `docs/long-form-kb-style` and `repair/kb-context-article-reading-pass` retain historical guidance (current article template and glossary strategy govern); `planning/content-operations-architecture` is unimplemented historical planning, parked pending comparison with Marketing/Driveline. Blog and utility branches retain unique active planning. No wholesale merges or stash actions.
- Protected local stash: `stash@{0}: On content/knowledge-base-reading-experience: WIP knowledge-base-reading-experience before ai-ops guardrail update`. No stash action of any kind without Rich approving that exact action. It is local only; GitHub cannot see it.

## To resume

Read this note and ask which lane. Then read `docs/ai-operations/operating_rules.md` and only the docs that lane names above. Then ask Rich for `git status --short`, the current branch and `git stash list`. What the repo is: `README.md`.

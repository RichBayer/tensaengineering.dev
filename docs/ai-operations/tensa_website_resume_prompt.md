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

## Repository reconciliation - PUBLISHED; CLEANUP AUDIT NEXT (2026-11-21)
- **Release CLOSED; do not revalidate:** Reconciliation merged by fast-forward into GitHub `main` at `5845e58` (11 files); Pages run #55 succeeded, Rich visually verified live Agent Operations Engineering History and revised Context Engineering articles. Local HTML/metadata/CSS, 283 references, 78 fragments, sitemap XML, full 4,367-line patch, November 2 AO historical evidence and owner approval were already checked. Live copy-prompt interaction was not separately retested (local implementation passed); indexing remains unverified. Closeout-only commit `7b19003` updated inventory and handoff, fast-forwarded to `main`, verified identical to integration branch. No repeat publication audits without a specific new defect.
- **Cleanup inventory; NO deletion authorized:** Five worktrees: `/mnt/g/ai/projects/tensaengineering.dev` clean (`integration/website-reconciliation-20261120` at `7b19003`); `/mnt/g/ai/projects/tensa-seo-publish` clean detached `b220005`; `/mnt/g/ai/projects/tensaengineering-driveline` clean `work/tensa-driveline` at `8c7f784` (two historical commits absent from main); `/mnt/g/ai/projects/tensaengineering-driveline-kb` at `fe5908c`, modified `projects/neurocore.html` and untracked AO history article both byte-identical to published copies; `/mnt/g/ai/projects/tensaengineering-driveline-publish` clean `c44dfac`. Local `main` at `b220005` was five commits behind origin/main; do not reset/switch blindly. `content/tensa-driveline-kb`, `publish/tensa-driveline`, `feature/kb-reading-experience-standard`: no commits ahead of main. `feature/blog-public-foundation`: 11 historically unique commits, approved unfinished Blog work, KEEP. `repair/kb-context-article-reading-pass`: 3 historically unique commits; 290-line `docs/planning/knowledge_base_reading_experience_standard.md` absent from current main: KEEP pending full-content review. Driveline page is already published; old branch-to-main D/M lists reflect branch age, not desired deletions.
- **NEXT: one comprehensive read-only cleanup audit, not serial little diffs/grep hits:** Use evidence above, inspect full relevant content of remaining unique branches (including KB reading standard), branch/worktree state, and **only the inventory** of protected stash in one bounded pass. Read complete files and compare meaning with current `main`; do not redo completed website validation or launch piecemeal archaeology. Produce one evidence-backed **Keep / Integrate / Archive / Remove** disposition table by exact branch/path, then request authorization for a coordinated set of changes. Integrate only missing, still-valid work. Do not merge old branches wholesale. Preserve Blog/utility work, unique history, all backups and `stash@{0}` on `content/knowledge-base-reading-experience`; no apply/drop/pop or other stash mutation, branch/worktree removal, force push or reset without Rich's explicit approval. Rich reviews complete proposed diff before any commit/push. Remote access: `RichBayer/home-network/docs/remote_access.md` Recipe C. Return to SEO terminology queue after cleanup decisions.
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

# TENSA Website Operating Rules

Every workflow rule for this repo, stated once. Where a rule came from a known incident, the incident is in brackets. Change these only by the one-in-one-out rule in `README.md`.

Planning docs own their subject. They do not set the workflow. Where a planning doc says how to start a session, how to edit, or what to update at closeout, the operating rules win.

## Resuming

1. Read the note, `docs/ai-operations/tensa_website_resume_prompt.md`.
2. Read these rules, then choose website SEO or Blog as the menu names (ask only when unclear).
3. Read the lane log on `main`: `docs/logs/website_seo.md` or `docs/logs/blog.md`, including its current gates, next action and source pointers.
4. Read only the selected sources and page-specific documents actually required. For Blog, the three `blog_*` strategy/experience/engagement files are authoritative on `feature/blog-public-foundation` until reconciled; shared source, SEO, style, and inventory docs on `main` are newer. Do not let stale branch copies override them.
5. Before any write or local-state-dependent action, request the session check below and inspect local unpushed changes; reconcile first if it is unsafe.

- No `tree`, `find` or href grep at every start. When the task touches structure, use `git ls-files`. When it touches links, routes or navigation, run a real link check, not a grep.
- When facts conflict, trust them in this order: local files and command output from Rich, his browser preview, validation output, GitHub, planning docs, chat memory.
- Finish a required research or validation gate before drafting. Candidate titles, candidate paths and old next-step suggestions in planning docs are guidance, not assignments. (A historical article title nearly bypassed the Blog pain-point research; commit `2c625a2`.)
- A branch or a stash existing is not a reason to resume it. Only what the note names is active.
- Don't invent the next step. The active log's `Next` owns it; ask only when both menu and log lack a grounded direction.
- During a resume, never propose new process or a new planning doc.

## V2 continuity and content routing

- `main` owns the 40-line menu and two 80-line V2 logs. The menu owns *open paths* only; logs own detailed next steps. Logs use seven headings: Purpose, Gates (PASS/OPEN/FAIL with evidence), Last session, Decisions in force, Next (branch, last verified local state, uncommitted files, precise next step/approval), Read before working (up to six starting paths), Closeout updates. Rewrite the active log as one bounded update; no endless checkpoints.
- At resume, report done, next, and unverified; saved notes never authorize implementation or publishing. On `save(website_seo)` / `save(blog)` or `handoff(<lane>)`, update only the active `main` log with evidence, then check it. Change the menu only when a lane opens or closes, by Rich's approval. Fresh-thread closeout checks stated evidence against commits and validation; unverified items stay qualified.
- The six initial read pointers are a starting point, **not a cap on necessary evidence**. Before public content work use the page inventory for status/URLs, content source map for source ownership, information architecture for page role, style guide for voice/claims, and the actual target HTML and existing page-specific CSS.
- Focused Knowledge Base article: additionally use `docs/planning/knowledge_base_article_template.md` and reference article `knowledge-base/ai-operations/context-engineering-ai-project-continuity.html`; preserve article/category/index/related-reading routes and existing CSS classes.
- Industry vocabulary / glossary: use `docs/planning/seo_topic_map.md`, `glossary_strategy.md`, `internal_linking_strategy.md`, public `glossary/index.html`, `assets/js/glossary-tooltips.js` and affected pages. Tooltip text is embedded separately in each page's `.glossary-term[data-definition]`; update every affected page's `data-definition` and `data-term` as needed when the linked definition changes. Preserve anchors, URLs and fallback links.
- Blog: use three **Blog-branch** `docs/planning/blog_*` files (strategy, reader experience, engagement), including Article #1 approved draft; use **main** for shared `seo_topic_map.md`, `content_style_guide.md`, `page_inventory.md`, and other updated site standards until locally reconciled. To prepare the Blog branch for publication, merge current `main` into `feature/blog-public-foundation` locally, without rebase or force; review conflicts and preserve approved Blog source/draft. Ordinary main-only log saves do not require immediate Blog reconciliation.
- For any public change, check page discovery (relevant category/index and related reading), nav, glossary, metadata/canonical/schema, reused styles/assets, responsive and interaction behavior, internal links/anchors and source-backed present/future claims. Update inventory/link map/sitemap only when their owned facts change; confirm Pages and live content before claiming deployment, and Search Console evidence before claiming indexing.
- From the **TENSA website terminal**, run `(git fetch -q origin && git show origin/main:scripts/session_check.py > /tmp/tensa_website_session_check.py && python3 /tmp/tensa_website_session_check.py <main|feature/blog-public-foundation> <website_seo|blog>) || echo "SESSION CHECK: FAIL (could not fetch or run)"`. Before V2 merges, use the review branch worktree: `git show origin/docs/website-v2-continuity-20261121:scripts/session_check.py > /tmp/tensa_website_session_check.py` then `python3 /tmp/tensa_website_session_check.py docs/website-v2-continuity-20261121 website_seo --review` (repeat with `blog`). Review mode checks staged menu/log shape but marks all connector/log writes NOT SAFE; it does not verify a deployed installation. Stop for any final `SESSION CHECK: FAIL`. PASS means continuity structure is valid, **not** write or publish authorization. Connector writes require `CONNECTOR WRITE TO THIS BRANCH: SAFE` on the actual target branch. Main-owned log saves require `LOG SAVE TO main: SAFE`: once Blog work is committed and the folder is clean, switch this same folder to `main` and run the check with `main blog`. No additional worktree is required; a Blog-branch check cannot certify a `main` write. Read-only reviews need no local check.

## Edits and commits

- Discuss every file edit with Rich before making it. Change only what was agreed, with no "while I'm in here" edits.
- No local commit, push, tag or merge unless Rich asks. He reads the diff first. A separately approved GitHub connector edit commits automatically; no redundant commit approval is needed. Finishing a step is not finishing the task.
- Only this repo is writable. Other repos are read-only reference.
- Read the whole current file before editing it or quoting it as current state. Never edit from grep snippets.
- A workflow change does not touch public pages, `sitemap.xml` or site state. Public HTML must be previewed locally before release, not edited directly on live `main` through the connector.
- Local edit scripts touch only the named files, fail loudly when the expected text is missing, and report what they changed. Verify each edit before the next.
- Network and remote-access facts live in the `home-network` repo. Point to it; never copy them here.

## Commands given to Rich

- Never put `set -e`, `set -u`, `set -o pipefail` or `set -euo pipefail` in Rich's terminal. They close the VS Code terminal on the first failure. If strict mode is needed, run it inside `bash -c '…'` or a script.
- No `exit`, `exec`, persistent `trap` or shell-option changes in pasted commands.
- Treat an expected nonzero result as evidence to read, not a reason for the shell to stop.
- No pagers: use `git --no-pager` or `GIT_PAGER=cat`.
- When the next command depends on the output, give one command or one tight group and wait. No chains of speculative fixes.
- Never put triple-backtick fences inside a block meant to be copied. It splits the block.
- Use absolute paths, and say which repo window the command belongs in.
- Don't ask Rich for anything the repo already answers.
- Copy and paste can turn LF into CRLF. Check line endings before treating a file as changed.
- Never paste login URLs, tokens or auth codes into chat, and never type a password or token into a terminal prompt.

## Editing through the GitHub connector

- The connector is read-only until Rich approves a write. One approval can cover an agreed batch of files.
- For connector edits, require clean synchronized local state for the target branch and the correct SAFE verdict; never overwrite locally unpushed work. Test new continuity infrastructure on a review branch before integration.
- The connector writes whole files only. Read the complete current file, change only the agreed lines, write the complete file back, then read it back and confirm nothing else changed and nothing was cut off.
- Keep files edited through the connector under about 700 to 800 lines. Larger files get cut off; edit those locally.
- One file per call is a tool limit, not a safety rule. Plan the agreed change set together, then write the files one after another.
- Check the file's current SHA before writing, so a stale copy never overwrites newer work.
- Local beats GitHub. If the local copy might hold unpushed work, get `git status` and the local file from Rich before writing anything.
- No force-push. No deletes unless Rich approves them. Afterward, report what changed and on which branch, and remind Rich to pull.

## Public content

- Check before you write:
  - any public page: `docs/planning/page_inventory.md`
  - a factual page: `docs/planning/content_source_map.md`
  - a long Knowledge Base article: `docs/planning/knowledge_base_article_template.md`
  - a Blog page: `blog_strategy.md`, `blog_reader_experience.md`, `blog_engagement_strategy.md` and `content_style_guide.md`, all in `docs/planning/`
  - major links or navigation: `docs/planning/internal_linking_strategy.md`
  - a new page, a new section or a new kind of content: the Purpose, Website Role and Core Positioning sections of `docs/planning/website_information_architecture.md`
- **Evidence-driven content research (Agent Operations and Argus Ventures article tests, 2026-10-31):** Start with the owner's purpose, experience, existing drafts and relevant context packs, using them for perspective rather than as proof of implementation. Verify current facts in the authoritative project sources, then investigate relevant Git history (including non-default branches and historical tags when useful), build logs, tests, independent reviews, failed experiments, reversals and decisions. For important incidents, trace the problem, evidence, decision or change, observed result and lesson; keep checkable source references for material claims. Distinguish documented facts from recollection or interpretation, and demonstrated capabilities from accepted plans or future ideas. Write from this understanding to explain what happened, why choices mattered and what can be learned, rather than listing features or retelling commits. Use other primary evidence when Git does not apply. Do not publish private source, sensitive or client information, proprietary processes or links to private repositories.
- Current versus future claims, product maturity and planning language on public pages: follow `docs/planning/content_style_guide.md`.
- One page or structure decision at a time.

## Publishing

- GitHub Pages builds from `main` at the repository root. Any change to `main` rebuilds the live site within minutes, including a commit that only updates the note.
- A push is not a deployment. Make no deployment or indexing claim without evidence: the Pages build result, the loaded page, or the webmaster tool.
- Internal planning never becomes public content.
- Internal docs are kept off the site by the root `_config.yml`, which excludes `docs/`, `scripts/` and `README.md` (commit `b5fe6b3`). Verified 2026-10-10: the build passed, and `/docs/website_state.html`, `/docs/website_state.md`, `/docs/ai-operations/tensa_website_resume_prompt.html` and `/docs/infrastructure/tensa_repository_map.txt` all returned 404.
- The exclude hides files from the website only. They stay readable on GitHub while the repository is public.
- Any internal file or folder added outside `docs/` joins the exclude list before it reaches `main`; `scripts/` is excluded for the V2 checker. Check both its raw address and its `.html` address afterward.

## Closeout

1. Link check, if links, routes or navigation changed.
2. Preview each changed public page: navigation, paths, images, no planning language, no unsupported or future-as-current claims.
3. `page_inventory.md`, if a page was added, removed or changed status.
4. `sitemap.xml`, if a public URL was added and is ready to index.
5. A planning doc only when its own subject changed: linking strategy for navigation, source map for a new page type, indexing strategy for sitemap or search-console state.
6. Update the active V2 work log (`main`) with evidence, next step, and local-state limits. Update the menu only if a lane opens or closes.
7. Rich reads the diff and authorizes local commit/push/merge; a separately approved connector write includes its automatic commit.

`docs/website_state.md` is touched only when a branding choice, a deployment fact or an open decision changes.

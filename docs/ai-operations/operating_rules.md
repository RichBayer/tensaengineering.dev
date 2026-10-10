# TENSA Website Operating Rules

Every workflow rule for this repo, stated once. Where a rule came from a known incident, the incident is in brackets. Change these only by the one-in-one-out rule in `README.md`.

Planning docs own their subject. They do not set the workflow. Where a planning doc says how to start a session, how to edit, or what to update at closeout, the operating rules win.

## Resuming

1. Read the note, `docs/ai-operations/tensa_website_resume_prompt.md`.
2. Ask Rich which lane: website work or Blog work.
3. Read these rules.
4. Read only the docs the lane's next step names.
5. Ask Rich for `git status --short`, the current branch and `git stash list`.

- No `tree`, `find` or href grep at every start. When the task touches structure, use `git ls-files`. When it touches links, routes or navigation, run a real link check, not a grep.
- When facts conflict, trust them in this order: local files and command output from Rich, his browser preview, validation output, GitHub, planning docs, chat memory.
- Finish a required research or validation gate before drafting. Candidate titles, candidate paths and old next-step suggestions in planning docs are guidance, not assignments. (A historical article title nearly bypassed the Blog pain-point research; commit `2c625a2`.)
- A branch or a stash existing is not a reason to resume it. Only what the note names is active.
- Don't invent the next step. If the note doesn't say, ask one question.
- During a resume, never propose new process or a new planning doc.

## Edits and commits

- Discuss every file edit with Rich before making it. Change only what was agreed, with no "while I'm in here" edits.
- No commit, push, tag or merge unless Rich asks. He reads the diff first. Finishing a step is not finishing the task.
- Only this repo is writable. Other repos are read-only reference.
- Read the whole current file before editing it or quoting it as current state. Never edit from grep snippets.
- A workflow change does not touch public pages, `sitemap.xml` or site state.
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
- No factual page from memory.
- Current versus future claims, product maturity and planning language on public pages: follow `docs/planning/content_style_guide.md`.
- One page or structure decision at a time.

## Publishing

- GitHub Pages builds from `main` at the repository root. Any change to `main` rebuilds the live site within minutes, including a commit that only updates the note.
- A push is not a deployment. Make no deployment or indexing claim without evidence: the Pages build result, the loaded page, or the webmaster tool.
- Internal planning never becomes public content.
- Internal docs are kept off the site by the root `_config.yml`, which excludes `docs/` and `README.md` (commit `b5fe6b3`). Verified 2026-10-10: the build passed, and `/docs/website_state.html`, `/docs/website_state.md`, `/docs/ai-operations/tensa_website_resume_prompt.html` and `/docs/infrastructure/tensa_repository_map.txt` all returned 404.
- The exclude hides files from the website only. They stay readable on GitHub while the repository is public.
- Any internal file or folder added outside `docs/` joins the exclude list before it reaches `main`. Check both its raw address and its `.html` address afterward.

## Closeout

1. Link check, if links, routes or navigation changed.
2. Preview each changed public page: navigation, paths, images, no planning language, no unsupported or future-as-current claims.
3. `page_inventory.md`, if a page was added, removed or changed status.
4. `sitemap.xml`, if a public URL was added and is ready to index.
5. A planning doc only when its own subject changed: linking strategy for navigation, source map for a new page type, indexing strategy for sitemap or search-console state.
6. The note: active, next step, date.
7. Rich reads the diff. Commit, push and merge happen when he says.

`docs/website_state.md` is touched only when a branding choice, a deployment fact or an open decision changes.

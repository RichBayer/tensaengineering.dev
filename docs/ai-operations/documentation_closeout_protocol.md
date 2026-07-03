# TENSA Engineering Website – Documentation Closeout Protocol

---

## Purpose

This document defines the mandatory documentation workflow for TENSA Engineering website build sessions.

It exists to prevent:

- website drift
- stale navigation
- missing page inventory entries
- broken internal links
- outdated repository maps
- public pages that outgrow the documentation system
- internal planning language leaking into public pages
- factual claims being written without source docs
- full-file replacement mistakes going undetected

This is an AI-operations control document for website build sessions.

It is not a public website page.

---

## Core Principle

Documentation must reflect the real website, not intention.

If the website, repository tree, navigation, page inventory, or documentation disagree:

    update the documentation to match reality

If a public page exists:

    it must be tracked

If a navigation link exists:

    it must have a known destination

If a factual page is expanded:

    source requirements must be checked first

If a full-file replacement is made:

    verify the intended change landed before moving on

---

## When This Protocol Is Triggered

Run this protocol:

- at the end of every serious website build session
- before committing changes
- before pushing to GitHub
- after adding, removing, renaming, or restructuring public pages
- after adding new asset directories or branding files
- after changing navigation
- after creating or changing planning docs
- when workflow rules change
- when explicitly requested by the user

This protocol should not be skipped.

---

## Pre-Closeout Context Check

Before documentation closeout, confirm current context is valid.

Required current context:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md

If any required context is missing, stale, uncertain, or not loaded in the current session:

    STOP
    request the required file or current repo output
    do not perform closeout from memory

Do not rely on prior conversation as source of truth.

Use uploaded documents, current file contents, repository output, and user-provided command output.

---

## Required Build-End Checks

Before updating closeout docs, run or request output for:

    git status --short
    tree -a -I '.git|.obsidian|node_modules|__pycache__'
    find . -maxdepth 3 -name "*.html" -print
    grep -R "href=" -n index.html about.html projects/*.html knowledge-base/*.html knowledge-base/*/*.html glossary/*.html story/*.html

Purpose:

- confirm modified files
- confirm new files and directories
- confirm public page inventory
- confirm current navigation and links
- detect stale anchors or broken internal routing
- confirm whether repo map and page inventory need updates

When public links, navigation, or routes changed, prefer a real local internal-link validation script/check over grep-only review.

The link validation check should:

- scan public HTML files
- extract internal href targets
- resolve relative paths
- resolve directory routes to index.html
- validate same-page and cross-page anchors
- ignore external links
- report broken local targets clearly

Future recommended permanent script:

    scripts/check_internal_links.py

Until that exists, a temporary Python link checker may be used during closeout.

---

## Documentation Responsibility Model


---

## Connector Access Rules

When repository connector access is available, it may be used during closeout to read committed repository files as baseline context.

Connector access should reduce manual upload friction, not replace local working-tree truth.

Default connector posture:

    read-only

Allowed by default:

    fetch committed repository files
    inspect committed source docs
    compare connector-read baseline docs against user-provided local output
    identify stale documentation based on verified source files and local command output
    load unchanged committed files when local working-tree status confirms they were not edited

Not allowed by default, even if the connector exposes write-capable tools:

    create repository files through connector tools
    update repository files through connector tools
    delete repository files through connector tools
    commit through connector tools
    push through connector tools
    modify public website files through connector tools
    modify closeout docs through connector tools

Write-capable connector tools may only be used if Richard explicitly authorizes the specific write action in the current session.

Preferred closeout workflow remains:

    connector reads committed baseline docs when useful
    Richard provides local git status / tree / validation output
    assistant requests exact local file contents for modified or about-to-be-edited files
    assistant proposes scoped local changes
    Richard applies changes locally
    targeted verification runs locally
    Richard reviews diff/status
    Richard commits and pushes manually

Connector-read access does not replace required local evidence for:

    git status
    tree output
    local uncommitted changes
    modified closeout/planning docs
    browser preview
    link validation results
    deployment checks

---

## Repository Boundary Lock

Once the active writable repository and approved edit scope are established, the boundary remains locked until Richard explicitly expands it.

For normal TENSA website work, the active writable repository is:

    RichBayer/tensaengineering.dev

External repositories may be loaded as read-only reference context when the active task requires them, but connector visibility does not grant write authority.

During workflow-only updates, do not change public page content, sitemap state, deployment state, indexing claims, website state, branch closeout state, current public page inventory, or next public build options unless Richard explicitly approves that website-state or public-content update.

Potential improvements outside the approved boundary should be recorded as recommendations or follow-up items, not silently implemented.

---

## Local Working Tree Priority Rule

During closeout, local repository state wins over connector-read state for any file that was edited, generated, created, deleted, or verified during the current session.

Use connector reads for:

    committed baseline context
    unchanged source docs
    unchanged public files
    confirming what was last committed

Use Richard-provided local output or full local file contents for:

    git status
    current tree output
    current validation output
    local browser review
    uncommitted public pages
    uncommitted planning docs
    uncommitted closeout docs
    any file about to be edited during closeout

Do not close out from connector-read committed files when `git status --short` shows local modifications.

Do not edit closeout or planning docs from grep snippets alone.

If a closeout or planning doc is modified locally, request the full current local file before editing it.

If Richard starts reverting to old upload-bundle habits, remind him:

    connector first for committed baseline
    local output/files for uncommitted truth
    exact local files only when needed


User:

- confirms when the build session is ending
- provides missing context if requested
- reviews closeout replacements before saving
- runs targeted verification commands after replacements
- confirms whether optional broader cleanup should be included

Assistant:

- determines which docs were impacted
- asks for missing source files or repo output
- updates all impacted closeout docs
- avoids unrelated cleanup
- preserves verified information
- does not invent file paths, page status, or future plans
- keeps public-facing content separate from internal planning content
- provides targeted verification commands after each full-file replacement

The assistant is responsible for identifying documentation impact, but must not make undocumented assumptions.

---

## Unknown Authority Rule

Any existing source-of-truth document that has not been loaded or bundled in full during the current session is an unknown authority document.

Unknown authority documents must not be:

- modified
- summarized as current state
- indirectly synchronized from memory
- rewritten from assumptions
- used as proof of implementation status

If a file may need to change, load the full current file first.

If a file exists only locally or may differ from GitHub, use local evidence or the read-only bundler workflow before editing.

---

## Bundler-First Local Context Workflow

When local files, uncommitted changes, generated artifacts, browser-preview observations, validation output, deployment evidence, or machine-specific state matter, and full local context is not already available, request a read-only context bundle or targeted local evidence before generating local editor scripts.

The bundle or local evidence should collect only relevant context, such as:

- required AI-operations docs
- repository map and website state docs
- affected planning docs
- affected public HTML, CSS, JavaScript, sitemap, robots, or asset references
- current local file contents or diffs
- `git status --short`
- `git diff --stat`
- full relevant `git diff` output
- internal-link validation output
- browser-preview observations
- deployment or search-console evidence when deployment or indexing claims matter

The bundler must not edit repository files.

After Richard uploads a bundle or local evidence, review it before generating any local Python editor script.

---

## Closeout Update Order

Use this order during website closeout:

1. Confirm build-end command output
2. Identify impacted files and docs
3. Update public HTML and indexing files if navigation or sitemap changed
4. After each full-file replacement, run a targeted verification check
5. Update repository map if structure changed
6. Update page inventory if pages were created, removed, renamed, or changed status
7. Update internal linking strategy if navigation or major link destinations changed
8. Update content source map if new page types or source requirements changed
9. Update search indexing strategy if sitemap, robots, or indexing state changed
10. Update documentation strategy if internal doc ownership or workflow rules changed
11. Update website state
12. Update resume prompt if workflow, structure, rules, or current state changed
13. Run final status and review diff
14. Commit and push after user approval

---

## Impact Detection Rules

### If files or directories changed

Update:

    docs/infrastructure/tensa_repository_map.txt

Examples:

- new public directory
- new asset directory
- new planning doc
- new AI-operations doc directory
- new script directory
- renamed or removed files
- major tree structure change

---

### If a public page was created, removed, renamed, or changed status

Update:

    docs/planning/page_inventory.md
    docs/website_state.md

Examples:

- created `/knowledge-base/index.html`
- created `/story/index.html`
- changed Argus ACLI from placeholder to live
- retired a page
- renamed a route

---

### If navigation changed

Update:

    docs/planning/internal_linking_strategy.md
    docs/planning/page_inventory.md
    docs/website_state.md

Examples:

- Knowledge Base nav changes from `#knowledge` to `/knowledge-base/`
- Story changes from homepage anchor to `/story/`
- GitHub proof moves to Resources
- new section is added to primary nav

---

### If a new public page category was introduced

Update:

    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/content_source_map.md
    docs/website_state.md

Examples:

- Knowledge Base category pages
- Story pages
- Resources pages
- Build Notes pages
- About page
- product install/download pages

---

### If factual project content changed

Check first:

    docs/planning/content_source_map.md

Then update as needed:

    docs/website_state.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/ai-operations/tensa_website_resume_prompt.md

Do not write or close out factual project changes unless source docs were loaded and used.

---

### If branding assets changed

Update:

    docs/infrastructure/tensa_repository_map.txt
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md

Update page inventory only if branding change affects page status or page purpose.

---

### If workflow rules changed

Update:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/planning/documentation_strategy.md
    docs/website_state.md if the change affects future build-start or closeout expectations

Examples:

- new mandatory build-start command
- new full-file replacement rule
- new replacement verification rule
- new link-checking workflow
- new source-doc rule
- new documentation governance rule
- new connector-read workflow rule
- new local working-tree source-of-truth rule

---

### If search indexing changed

Update:

    docs/planning/search_indexing_strategy.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/page_inventory.md
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md if future sessions need to know

Examples:

- sitemap.xml changed
- robots.txt changed
- new public URL added to sitemap
- indexing workflow changed
- Google Search Console or Bing status changed

---

## Closeout Documentation Matrix

| Change Type | Required Docs |
|---|---|
| New public page | repo map, page inventory, internal linking strategy, website state, sitemap if public URL should be indexed |
| New public directory | repo map, page inventory, website state |
| New asset directory or branding assets | repo map, website state, resume prompt if important |
| Navigation changed | internal linking strategy, page inventory, website state, affected HTML pages |
| Public page status changed | page inventory, website state, resume prompt if major |
| Factual project page expanded | content source map checked, page inventory, website state, internal linking strategy |
| Knowledge Base category/article added | page inventory, internal linking strategy, content source map, website state, sitemap |
| Story page added | page inventory, internal linking strategy, content source map, website state, sitemap |
| New planning doc created | repo map, page inventory if important, documentation strategy, website state, resume prompt if it becomes core context |
| New AI-operations doc created | repo map, page inventory if important, documentation strategy, website state, resume prompt if it becomes core context |
| New workflow rule added | resume prompt, closeout protocol, documentation strategy, website state if relevant |
| Old-site migration decision made | old-site migration plan, website state, resume prompt if major |
| SEO/content strategy changed | SEO topic map, website state, resume prompt if major |
| Sitemap changed | search indexing strategy, repo map, website state, resume prompt if useful |

---

## Surgical Update Rule

Before providing a documentation replacement, state:

1. exact file being updated
2. specific intended changes
3. why the changes are required

Do not:

- silently rewrite unrelated sections
- do cosmetic cleanup outside scope
- restructure sections unless needed
- invent new future plans
- change project positioning without source docs
- add links that were not created
- describe placeholder pages as complete
- describe future features as available

If broader cleanup would improve the document:

    STOP
    explain the optional cleanup
    ask for approval before including it

---

## Full-File Replacement Rule

The user prefers full-file replacements for accuracy.

For closeout documentation, provide:

    one full file replacement per file

Do not provide partial patches or snippets unless explicitly requested.

If multiple files need updates, handle them one at a time unless the user asks for a batch.

For Markdown files, avoid nested triple-backtick fences inside copy blocks when possible.

Use indented text blocks inside Markdown documents to avoid breaking the outer copy block.

---

## Python Full-File Writer Rule

Python-based file writing is allowed and often preferred for closeout documentation delivery, but only under the right conditions.

Use Python as a delivery mechanism when:

- the current full file context has been loaded or otherwise verified
- the complete intended replacement or approved scoped edit has been decided
- every existing file being edited is inside the approved repository boundary
- the command is easier and safer than manual copy/paste
- the replacement or edit can be verified immediately afterward

Local Python editor scripts must:

- edit only approved files
- create only approved new files
- preserve unrelated content
- fail loudly if an expected marker, heading, or exact replacement count is missing
- avoid silently continuing after a failed required replacement
- print every file they create or update
- leave review to `git status --short`, `git diff --stat`, targeted `git --no-pager diff`, and local validation

Do not use Python as a shortcut to:

- inspect only partial file context
- make blind surgical patches from incomplete information
- guess what a hidden section probably says
- rewrite unrelated content without approval
- bypass Richard's review expectations
- change public content, sitemap state, branch state, website state, deployment state, or indexing claims during workflow-only updates

Preferred safe pattern:

    full context first
    define intended changes
    write the complete file or approved scoped edit
    run targeted verification
    wait for user output

This rule exists because Python is reliable for writing files, but reliability does not replace source-of-truth context.

---

## Replacement Verification Rule

After each full-file replacement during closeout or live website editing, run a targeted verification check before moving to the next file.

The verification should confirm that:

- the intended new text, link, or status exists
- the stale text, link, or status was removed when applicable
- the correct file was edited
- the file was saved
- no obvious paste truncation occurred

Examples:

    grep -n 'href="../story/"\|href="../index.html#story"' projects/argus-acli.html
    grep -n "27 directories, 64 files\|glossary/index.html\|assets/js/glossary-tooltips.js" docs/infrastructure/tensa_repository_map.txt
    grep -n "https://tensaengineering.dev/story/" sitemap.xml

This rule exists to catch:

- paste mistakes
- missed saves
- wrong-file edits
- stale snippets
- unintended partial replacements
- copy/paste truncation
- accidental edits to the wrong file

Do not continue to the next replacement until the targeted verification check passes or the mismatch is understood and corrected.

---

## Public vs Internal Language Rule

Public website pages must not sound like internal planning docs.

Avoid public-facing language like:

- “this section should”
- “future articles should”
- “the assistant must”
- “update this later”
- “source docs required”
- “do not overstate”

Those belong in internal planning docs.

Public pages should speak to visitors:

- what this page explains
- what readers can learn
- how the ecosystem fits together
- where they can go next
- what exists now vs what is planned

Internal docs may include instructions, rules, status labels, source requirements, and closeout procedures.

---

## Page Inventory Rules

If a public page exists, it must appear in:

    docs/planning/page_inventory.md

The inventory must track:

- path
- page title
- type
- status
- purpose
- source docs required
- navigation status
- next action

If a page changes status, update the inventory.

Examples:

    Placeholder → Live
    Planned → Structure-only
    Structure-only → Live
    Live → Needs review

Do not allow public pages to exist without inventory tracking.

---

## Internal Linking Rules

If a major link, route, topic destination, or navigation target changes, update:

    docs/planning/internal_linking_strategy.md

The strategy must track:

- current navigation targets
- preferred destination for major topics
- temporary links
- future preferred destinations
- planned link upgrades
- link audit expectations

Do not keep stale anchor links once real pages exist.

Example:

Once `/knowledge-base/` exists:

    Knowledge Base nav should point to `/knowledge-base/`

not:

    `#knowledge`

Once `/story/` exists:

    Story nav should point to `/story/`

not:

    `/index.html#story`

---

## Source Map Rules

Before writing or significantly expanding factual pages, check:

    docs/planning/content_source_map.md

If a new page type is created and source requirements are not documented, update the content source map.

Examples of pages that require source requirements:

- full Argus ACLI page
- full Argus Lab page
- Knowledge Base architecture articles
- Story origin pages
- Build Notes pages
- old-site migration content
- install/download guidance

Do not create factual pages from memory.

---

## Repository Map Rules

If the repository tree changes, update:

    docs/infrastructure/tensa_repository_map.txt

Use this command:

    tree -a -I '.git|.obsidian|node_modules|__pycache__'

The repository map should include:

- current tree
- directory purpose
- key file purpose
- current public pages
- current internal docs
- missing/planned directories
- future structure
- source-of-truth rule
- working rules
- build-start checks
- last known tree output

---

## Website State Rules

Update:

    docs/website_state.md

at the end of major website build sessions.

It should reflect:

- current public pages
- current repo structure
- current branding system
- current navigation state
- current page statuses
- completed work
- not-yet-completed work
- anti-drift context pack
- build-start checks
- next recommended steps
- source docs used recently
- working rules
- tone and guiding rule

This is the live-current-state record.

It should not become the entire strategy document.

---

## Resume Prompt Rules

Update:

    docs/ai-operations/tensa_website_resume_prompt.md

when the session changes:

- current public page set
- repository size
- core anti-drift docs
- build-start checks
- workflow rules
- next recommended work
- strategic direction
- major completed work
- major not-yet-completed work

The resume prompt should stay compressed.

It should not become a full duplicate of `website_state.md`.

It should help a fresh AI session restart correctly.

---

## Page Content Review Gate

Before closeout, public pages changed during the session should be checked for:

- correct navigation
- correct relative paths
- correct branding/image paths
- no internal planning language
- no dead links
- no accidental future-feature claims
- no factual claims unsupported by loaded docs
- consistent tone
- clear current-vs-future distinction

If a public page sounds like an internal planning document:

    revise it before closeout

---

## Link Validation Gate

Before closeout, run or request a real local internal-link validation check when public links, routes, or navigation changed.

The preferred validation should confirm:

- all public HTML files are discovered
- internal href targets resolve to existing local files
- relative paths resolve correctly from nested pages
- directory routes resolve to index.html
- same-page anchors resolve
- cross-page anchors resolve
- external links are skipped or separately reviewed
- broken internal paths are reported clearly

For small visual reviews, this grep remains useful:

    grep -R "href=" -n index.html about.html projects/*.html knowledge-base/*.html knowledge-base/*/*.html glossary/*.html story/*.html

But grep is not enough by itself when significant routes or article paths were added.

Temporary Python validation is acceptable until a permanent script exists.

Future recommended script:

    scripts/check_internal_links.py

Record significant validation results in closeout docs when useful.

Example result worth recording:

    Public HTML files checked: 17
    Internal links checked: 403
    External/skipped links: 0
    Result: all checked internal links resolved successfully

---

## Completion Gate

Before declaring closeout complete, verify:

- `git status --short` was reviewed
- connector-read files were not used as closeout truth for locally modified files
- current tree was reviewed
- HTML page list was reviewed
- link output or local link validation was reviewed
- repo map is updated if tree changed
- page inventory is updated if pages changed
- internal linking strategy is updated if links changed
- content source map is updated if source requirements changed
- search indexing strategy is updated if sitemap or indexing state changed
- documentation strategy is updated if workflow or doc ownership changed
- website state is updated
- resume prompt is updated if current state or workflow changed
- public pages do not contain internal planning language
- all changed public pages were locally previewed or user-confirmed
- targeted verification checks passed after full-file replacements
- local internal-link validation passed when public links, routes, or navigation changed
- final diff/status is ready for review

If any required condition fails:

    closeout is not complete

---

## Commit Gate

Before commit:

1. Run:

       git status --short

2. Review relevant diffs.

3. Confirm there are no unintended file changes.

4. Use a clear commit message.

Recommended commit message format:

    Update TENSA site structure and documentation

or:

    Add Knowledge Base structure and branding assets

or:

    Update TENSA website continuity docs

or:

    Add TENSA Story page and update navigation

or:

    Add TENSA Knowledge Base article path

Choose the message based on the actual work completed.

---

## Final Rule

Documentation is part of the website system.

If documentation is wrong:

    the website system is wrong

No serious website build session is complete until documentation, navigation, page inventory, link strategy, repository state, and verification checks are aligned with reality.

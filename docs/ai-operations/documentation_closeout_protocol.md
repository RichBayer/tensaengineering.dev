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
    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html

Purpose:

- confirm modified files
- confirm new files and directories
- confirm public page inventory
- confirm current navigation and links
- detect stale anchors or broken internal routing
- confirm whether repo map and page inventory need updates

Future recommended replacement for manual link grep:

    scripts/check_internal_links.py

---

## Documentation Responsibility Model

User:

- confirms when the build session is ending
- provides missing context if requested
- reviews closeout replacements before saving
- confirms whether optional broader cleanup should be included

Assistant:

- determines which docs were impacted
- asks for missing source files or repo output
- updates all impacted closeout docs
- avoids unrelated cleanup
- preserves verified information
- does not invent file paths, page status, or future plans
- keeps public-facing content separate from internal planning content

The assistant is responsible for identifying documentation impact, but must not make undocumented assumptions.

---

## Closeout Update Order

Use this order during website closeout:

1. Confirm build-end command output
2. Identify impacted files and docs
3. Update repository map if structure changed
4. Update page inventory if pages were created, removed, renamed, or changed status
5. Update internal linking strategy if navigation or major link destinations changed
6. Update content source map if new page types or source requirements changed
7. Update website state
8. Update resume prompt if workflow, structure, rules, or current state changed
9. Run final status and review diff
10. Commit and push after user approval

---

## Impact Detection Rules

### If files or directories changed

Update:

    docs/infrastructure/tensa_repository_map.txt

Examples:

- new public directory
- new asset directory
- new planning doc
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
    docs/website_state.md if the change affects future build-start or closeout expectations

Examples:

- new mandatory build-start command
- new full-file replacement rule
- new link-checking workflow
- new source-doc rule
- new documentation governance rule

---

## Closeout Documentation Matrix

| Change Type | Required Docs |
|---|---|
| New public page | repo map, page inventory, internal linking strategy, website state |
| New public directory | repo map, page inventory, website state |
| New asset directory or branding assets | repo map, website state, resume prompt if important |
| Navigation changed | internal linking strategy, page inventory, website state, affected HTML pages |
| Public page status changed | page inventory, website state, resume prompt if major |
| Factual project page expanded | content source map checked, page inventory, website state, internal linking strategy |
| Knowledge Base category added | page inventory, internal linking strategy, content source map, website state |
| New planning doc created | repo map, website state, resume prompt if it becomes core context |
| New workflow rule added | resume prompt, closeout protocol, website state if relevant |
| Old-site migration decision made | old-site migration plan, website state, resume prompt if major |
| SEO/content strategy changed | SEO topic map, website state, resume prompt if major |

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

Before closeout, run:

    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html

Confirm:

- Knowledge Base points to `/knowledge-base/`
- Story temporary links point to homepage story anchor until `/story/` exists
- GitHub temporary links point to homepage proof anchor until Resources exists
- project links point to real project pages
- no stale `#knowledge` navigation remains except homepage section IDs or labels
- no dead internal paths were introduced

Future recommended script:

    scripts/check_internal_links.py

---

## Completion Gate

Before declaring closeout complete, verify:

- `git status --short` was reviewed
- current tree was reviewed
- HTML page list was reviewed
- link output was reviewed
- repo map is updated if tree changed
- page inventory is updated if pages changed
- internal linking strategy is updated if links changed
- content source map is updated if source requirements changed
- website state is updated
- resume prompt is updated if current state or workflow changed
- public pages do not contain internal planning language
- all changed public pages were locally previewed or user-confirmed
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

Choose the message based on the actual work completed.

---

## Final Rule

Documentation is part of the website system.

If documentation is wrong:

    the website system is wrong

No serious website build session is complete until documentation, navigation, page inventory, link strategy, and repository state are aligned with reality.
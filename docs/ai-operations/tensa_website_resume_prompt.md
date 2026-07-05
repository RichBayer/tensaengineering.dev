# TENSA Engineering Website – Resume Prompt (Compressed)

Use this prompt when starting a fresh TENSA Engineering website session.

The website is the public home for TENSA Engineering:

    https://tensaengineering.dev

Local repository path:

    /mnt/g/ai/projects/tensaengineering.dev

GitHub repository:

    RichBayer/tensaengineering.dev

Deployment:

    GitHub Pages

DNS / domain:

    Cloudflare

Default working assumption:

    Richard is usually in VS Code at the repository root with an integrated terminal open.
    Provide copy-ready commands that can be run from the repo root unless told otherwise.

---

## Current Committed Baseline

The latest confirmed website-content closeout merged and pushed to `main` was:

    5687392 Refine KB article reading experience

That commit converted the focused AI Operations project-context article into the first prose-first Knowledge Base article reading-standard proof page.

Current repository size from latest local closeout evidence:

    27 directories, 72 files

Current public HTML page count:

    19

Latest local internal-link validation from closeout:

    Public HTML files checked: 19
    Internal links checked: 579
    External/skipped links: 21
    Result: all checked internal links and anchors resolved successfully

Do not assume the live site deployed just because `main` was pushed. GitHub Pages deployment and live-page behavior must be verified from current evidence before making deployment or indexing claims.

---

## Most Recent Completed Work

Completed in the latest reading-experience branch:

- branch `feature/kb-reading-experience-standard` was committed, fast-forward merged into `main`, and pushed to `origin/main`
- focused article updated at:

        knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html

- article became the first prose-first Knowledge Base article standard / proof page
- list-heavy structure was replaced with fuller article prose
- raw/code-looking diagrams were reduced to three styled explanatory diagrams
- article metadata was changed from pill-style tags to one plain reader-context sentence
- shared `styles.css` now includes reusable Knowledge Base article diagram, FAQ, and metadata styling
- closeout docs were updated to record the article format standard and next IA direction

Important:

    This latest branch did not add new public routes, directories, assets, sitemap entries, or navigation destinations.

---

## Current Next Website Direction

Next high-value website work:

    AI Operations category / article index conversion

Recommended next branch:

    feature/kb-ai-operations-index

or:

    feature/kb-category-article-index

Target structure:

    knowledge-base/ai-operations/
        index.html
            future AI Operations category / article index page

        what-is-ai-operations.html
            likely future home for the current long-form AI Operations landing-page content
            final slug still needs explicit approval

        how-to-keep-ai-from-losing-project-context.html
            existing focused continuity guide and article-format proof page

Do not start by rewriting the whole Knowledge Base. Work one page / structure decision at a time.

---

## Critical Local-Only Context

A protected local stash existed at latest local confirmation:

    stash@{0}: On content/knowledge-base-reading-experience: WIP knowledge-base-reading-experience before ai-ops guardrail update

Rules:

- do not apply, pop, drop, rewrite, or otherwise touch this stash unless Richard explicitly approves that exact stash action
- the stash is local-only and may not be visible through the GitHub connector
- if branch repair comes up, request current local Git output first

Suggested inspection commands only if Richard intentionally revisits that repair work:

    git branch
    git stash list
    git checkout content/knowledge-base-reading-experience
    git status --short
    git stash show --stat "stash@{0}"
    git stash show --patch "stash@{0}"

---

## Session Initialization Protocol

At the start of every serious website build session:

1. Treat the session as having zero reliable prior context.
2. Use connector reads first for committed source-of-truth docs when connector access is available.
3. Do not ask Richard for giant upload bundles by habit.
4. Ask Richard for current local command output that connector reads cannot provide.
5. Ask for exact local file contents only when a file is modified, uncommitted, local-only, or about to be edited.
6. Do not analyze, summarize, or act on incomplete source context while required docs are still being loaded.

Build-start local checks:

    git status --short
    git branch --show-current
    git log --oneline --decorate -5
    git stash list
    tree -a -I '.git|.obsidian|node_modules|__pycache__'
    find . -maxdepth 3 -name "*.html" -print | sort
    grep -R "href=" -n index.html about.html contact.html projects/*.html knowledge-base/*.html knowledge-base/*/*.html glossary/*.html story/*.html

When public links, routes, or navigation matter, prefer real local internal-link validation over grep-only review.

Future recommended permanent script:

    scripts/check_internal_links.py

---

## Source-of-Truth Priority

Use this order when facts conflict:

1. current local files and local command output supplied by Richard
2. current browser preview observations supplied by Richard
3. current local validation output supplied by Richard
4. committed repository files read through the connector
5. current planning / closeout docs
6. previous chat context and model memory

Do not close out from connector-read committed files when local modifications exist.

During closeout, local working-tree files and local command output override connector-read committed state.

---

## Connector Access Rules

Default connector posture:

    read-only

Connector reads are appropriate for:

- committed AI-operations docs
- committed planning docs
- committed website state files
- committed public HTML/CSS/JS source files
- committed repository map and source maps

Connector reads do not replace local command output for:

- uncommitted working-tree changes
- current `git status --short`
- current branch state
- current stash state
- local `tree` output
- browser preview
- internal-link validation results
- deployment checks

Connector writes are disabled by policy unless Richard explicitly authorizes the specific write action in the current session.

If Richard explicitly authorizes a connector write:

- keep it scoped to the named file(s)
- avoid public page changes unless he explicitly asked for them
- do not force-push
- do not delete files unless explicitly authorized
- report exactly what was changed and which branch was updated
- remind Richard to pull locally if the connector wrote to a branch he has checked out

Normal preferred workflow remains:

    assistant reads and analyzes
    assistant provides local commands or full-file replacement content
    Richard applies changes locally
    Richard reviews diffs
    Richard commits and pushes manually

---

## Critical Operating Rules

- Do not guess page state, repository structure, paths, links, deployment state, or project facts.
- Do not treat prior conversation as system truth.
- Do not invent public-facing claims.
- Do not write factual public pages without checking source requirements.
- Do not edit closeout or planning docs from grep snippets alone.
- Read or request full-file context before editing closeout or planning docs.
- Do not use Python to blindly patch unknown sections from partial context.
- Controlled Python edits are acceptable after full-file context has been reviewed and intended changes are clear.
- Use full file replacements when manual copy/paste editing would be error-prone.
- Do not make hidden changes.
- After each full-file replacement or controlled Python edit, run targeted verification before moving on.
- Keep public-facing content separate from internal planning content.
- Do not let the site grow faster than the documentation system that tracks it.
- Build one page or structure decision at a time.

If something is unclear:

    STOP
    explain what is missing
    ask for the needed file, repo output, browser observation, validation result, or source doc

---

## Core Context Docs

Load or inspect these at the start of serious website sessions as needed:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/ai-operations/claude/claude_website_polish_resume_prompt.md
    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/content_style_guide.md
    docs/planning/documentation_strategy.md
    docs/planning/glossary_strategy.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/search_indexing_strategy.md
    docs/planning/search_answer_optimization_template.md
    docs/planning/seo_topic_map.md

Purpose of each:

    tensa_website_resume_prompt.md
        compressed startup protocol and current direction

    documentation_closeout_protocol.md
        mandatory documentation closeout workflow for serious website build sessions

    claude_website_polish_resume_prompt.md
        Claude prose-polish workflow and guardrails

    website_state.md
        current state record, completed work, incomplete work, and next steps

    website_information_architecture.md
        long-term site structure and expansion plan

    tensa_repository_map.txt
        repository structure and file-role map

    content_source_map.md
        source-doc requirements before writing factual pages

    content_style_guide.md
        public writing voice, tone, formatting, and article standards

    documentation_strategy.md
        documentation ownership, update triggers, and overlap boundaries

    glossary_strategy.md
        glossary purpose, term-selection rules, tooltip behavior, and expansion guardrails

    page_inventory.md
        page existence, status, purpose, navigation state, and next actions

    internal_linking_strategy.md
        logical link flow, preferred destinations, temporary links, and link-audit expectations

    search_indexing_strategy.md
        sitemap, robots.txt, Google Search Console, Bing Webmaster Tools, and indexing workflow

    search_answer_optimization_template.md
        future search-and-answer optimization workflow for page clarity and reader/search intent

    seo_topic_map.md
        future SEO topic planning and Knowledge Base search strategy

---

## Current Public Pages

Current public pages:

    /
    /projects/
    /projects/neurocore.html
    /projects/argus-acli.html
    /projects/argus-lab.html
    /knowledge-base/
    /glossary/
    /about.html
    /contact.html
    /knowledge-base/ai-operations/
    /knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html
    /knowledge-base/persistent-ai-memory/
    /knowledge-base/controlled-ai-systems/
    /knowledge-base/local-first-ai/
    /knowledge-base/safe-tool-interaction/
    /knowledge-base/linux-diagnostics/
    /knowledge-base/troubleshooting-training/
    /knowledge-base/neurocore-architecture/
    /story/

Current public HTML page count:

    19

---

## Current Navigation State

Primary navigation:

    Home
    Projects
    Knowledge Base
    Glossary
    Story
    About

Primary targets:

    Home → /index.html
    Projects → /projects/
    Knowledge Base → /knowledge-base/
    Glossary → /glossary/
    Story → /story/
    About → /about.html

Footer targets:

    Contact → /contact.html
    About → /about.html
    Projects → /projects/
    Knowledge Base → /knowledge-base/
    Glossary → /glossary/

Important navigation rules:

- Contact is footer-only.
- Public GitHub navigation has been removed from current public pages.
- Direct public links to private implementation repositories have been removed from current public pages.
- Knowledge Base index links to all eight foundation Knowledge Base articles.
- The foundation path links article-to-article and loops back to AI Operations from NeuroCore Architecture.
- AI Operations links to the focused project-context guide.
- Inline glossary terms in Knowledge Base articles point to `/glossary/` entries.

---

## Current Knowledge Base State

Knowledge Base index:

    /knowledge-base/

Current eight-article foundation path:

    1. AI Operations
       /knowledge-base/ai-operations/

    2. Persistent AI Memory
       /knowledge-base/persistent-ai-memory/

    3. Controlled AI Systems
       /knowledge-base/controlled-ai-systems/

    4. Local-First AI
       /knowledge-base/local-first-ai/

    5. Safe Tool Interaction
       /knowledge-base/safe-tool-interaction/

    6. Linux Diagnostics
       /knowledge-base/linux-diagnostics/

    7. Troubleshooting Training
       /knowledge-base/troubleshooting-training/

    8. NeuroCore Architecture
       /knowledge-base/neurocore-architecture/

Current focused AI Operations article:

    How to Keep AI From Losing Project Context
    /knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html

Current article-format standard:

    The project-context article is the proof page for the prose-first Knowledge Base article standard.

That standard means:

- fuller paragraphs with natural transitions
- fewer lists and numbered sections
- bullets only when they improve scanning
- two or three strong explanatory diagrams rather than many weak ones
- diagrams that feel like article graphics, not code blocks or file trees
- useful FAQ, but secondary to the main article
- clear distinction between current reality and future plans

Category pages and focused article pages should have different jobs:

    Category page:
        route readers to articles and briefly explain the topic area

    Focused article:
        answer one reader question in depth

---

## Current Search / SEO State

Root search files:

    robots.txt
    sitemap.xml

Current sitemap URL after deployment:

    https://tensaengineering.dev/sitemap.xml

Current robots URL after deployment:

    https://tensaengineering.dev/robots.txt

Current sitemap contains 19 canonical HTTPS non-www URLs.

Known Search Console note:

    Google reported "Page with redirect" for alternate redirect versions:
        http://tensaengineering.dev/
        https://www.tensaengineering.dev/

This is expected and harmless because the intended canonical indexed URL is:

    https://tensaengineering.dev/

Post-deploy checks after the reading-experience merge:

- confirm the focused article loads at its canonical URL
- confirm the AI Operations page still links to the focused guide
- confirm the live sitemap still contains 19 URLs
- inspect the focused article in Google Search Console if appropriate
- do not claim indexing until webmaster-tool evidence confirms it

---

## Current Ecosystem Model

TENSA Engineering:

- umbrella engineering company
- public brand and ecosystem owner
- public hub
- knowledge base
- ecosystem portal
- future product funnel

NeuroCore:

- local-first governed AI runtime platform
- persistent daemon-based architecture
- continuity and memory direction
- current local retrieval / RAG foundation
- future structured knowledge base direction
- future context-aware memory / CAG-style context assembly direction
- controlled tool interaction
- real Linux system awareness
- governed execution
- operational continuity

Argus ACLI:

- first product built on NeuroCore
- local-first read-only Linux diagnostics
- real telemetry
- structured findings
- severity classification
- recommendations
- raw evidence
- AI explanation grounded in structured evidence
- no uncontrolled AI authority over the machine

Argus Lab:

- early real-Linux troubleshooting, training, and validation environment
- controlled failure scenarios
- resettable lab sessions
- mentor-style AI guidance
- validation environment for NeuroCore, Argus ACLI, and model-guided troubleshooting

AI Operations:

- disciplined AI-assisted workflow
- documentation as memory
- source-grounded session continuity
- anti-drift guardrails
- closeout protocols
- resume prompts
- human review and local verification

Glossary:

- compact public reference layer for recurring ecosystem terms
- supports Knowledge Base readers without bloating every article
- provides inline tooltip destinations for selected Knowledge Base terms
- should remain compact and should not replace full Knowledge Base articles

Private implementation repositories and internal source docs:

- preserve engineering source of truth during active development
- preserve implementation history
- preserve architecture docs and build logs
- are not currently public proof links on the website

Future public technical artifacts:

- may include selected documentation, examples, release materials, downloads, videos, or open technical components when useful

---

## Public Writing Rules

Public pages should:

- be professional, practical, and technically credible
- sound human and builder-oriented
- explain technical terms in plain language
- avoid AI hype
- avoid corporate fluff
- distinguish current reality from future plans
- use conversational prose for story and explainer pages
- use prose-first article flow for long-form Knowledge Base content
- use bullets only when they improve clarity
- route readers toward deeper pages instead of dumping everything on one page

Public pages should not:

- sound like internal instructions
- say “this section should”
- expose internal planning language
- overstate product maturity
- imply future features already exist
- duplicate entire technical repository docs
- look like raw documentation checklists unless the page is intentionally a reference page

---

## Current Completed Work Summary

Completed so far:

- GitHub repo created
- repo cloned locally
- custom domain configured
- GitHub Pages enabled
- Cloudflare DNS configured
- HTTPS enabled
- website live
- homepage created and refined
- Projects overview page created
- NeuroCore page created and expanded
- Argus ACLI full public page created
- Argus Lab full public project page created
- Knowledge Base index created and upgraded into a foundation-path hub
- eight Knowledge Base foundation articles created
- focused AI Operations project-context article created
- focused AI Operations project-context article converted into the first prose-first article-format proof page
- Story page created
- Glossary page created and added to primary navigation
- About page created
- Contact page created after email routing was configured and tested
- branding asset hierarchy created
- TENSA, NeuroCore, Argus ACLI, and Argus Lab logos added
- favicon assets created and wired across current public pages
- public GitHub navigation removed from current public pages
- direct public links to private implementation repositories removed from current public pages
- inline glossary tooltip JavaScript added
- Knowledge Base articles received selected inline glossary tooltip links
- closeout / planning docs created and maintained
- sitemap.xml contains 19 canonical URLs
- local internal-link validation passed for 579 internal links across 19 public HTML files during the latest closeout

---

## Current Not Completed

Not yet completed:

- GitHub Pages live deployment verification after the reading-experience merge
- live verification of the focused project-context article
- live verification that the AI Operations page still links to the focused article
- live verification that sitemap.xml still contains 19 canonical URLs
- Google/Bing discovery review after deployment
- AI Operations category / article index conversion
- migration of the current long-form AI Operations landing-page content into a dedicated article page
- optional stock / editorial image system for future Knowledge Base article polish
- Resources page
- Build Notes section
- old-site migration plan
- permanent internal link checker script
- analytics decisions
- future install/download guidance for Argus ACLI
- reusable article templates for future Knowledge Base expansion
- public technical artifact strategy

---

## Source-Doc Rules

Before writing or significantly rewriting factual pages, check:

    docs/planning/content_source_map.md

Before creating or changing public pages, check:

    docs/planning/page_inventory.md

Before adding or changing major links, check:

    docs/planning/internal_linking_strategy.md

Before assuming file paths or repo structure, check:

    docs/infrastructure/tensa_repository_map.txt

Do not write full factual Argus ACLI, Argus Lab, NeuroCore, Story, or Knowledge Base pages without the required source docs.

---

## Editing Rule

Richard prefers full-file replacements when manual copy/paste editing would be error-prone.

Do not provide small manual find/replace snippets unless explicitly requested.

For code, HTML, CSS, or long Markdown replacements that Richard must paste manually:

    provide the complete replacement file

For closeout docs and planning docs:

    do not edit from grep snippets alone
    first review or request the full current file
    then use the smallest safe edit

Controlled Python edits are acceptable after full-file context has been reviewed and the intended changes are clear.

---

## Replacement Verification Rule

After each full-file replacement or controlled Python edit during closeout or live website editing, run a targeted verification check before moving to the next file.

The verification should confirm:

- the intended new text, link, or status exists
- stale text, links, or statuses were removed when applicable
- the correct file was edited
- the file was saved
- no obvious paste truncation occurred

Do not move to the next replacement until verification passes or the mismatch is understood and corrected.

---

## Documentation Closeout Rules

During closeout:

- do not silently rewrite docs
- do not make unknown documentation changes
- do not perform broad cleanup unless explicitly requested
- only update docs directly impacted by the build session
- preserve unchanged sections unless modification is needed
- explain what each closeout doc update is meant to capture
- keep closeout docs aligned with real repo state
- run targeted verification after each full-file replacement or controlled edit

Closeout docs usually include only the files impacted by the session. Do not update every planning doc by habit.

---

## Current Next Best Step

Immediate after latest push:

1. Verify GitHub Pages deployed the latest `main` changes.
2. Confirm the focused article loads at its canonical URL.
3. Confirm the AI Operations page still links to the focused article.
4. Confirm the live sitemap still contains 19 canonical URLs.
5. Pull the latest `main` locally if a connector write updated this file.

Next build session:

1. Start a fresh thread from this resume prompt.
2. Run the build-start checks.
3. Load core context docs through connector reads first.
4. Ask Richard for local git status, tree, validation, stash, and browser observations as needed.
5. Start a fresh branch for the AI Operations category / article index conversion.
6. Do not touch the protected local stash unless Richard explicitly approves that exact action.

---

## Next Public Build Options

Highest-priority next public build:

    AI Operations category / article index conversion

Later options:

- Resources page
- Build Notes section
- additional focused Knowledge Base articles after source requirements and link destinations are defined
- optional stock / editorial image system for future Knowledge Base article polish
- permanent internal-link checker script when manual validation becomes annoying

Keep sitemap.xml URL-only unless a reliable `lastmod` workflow is added.

---

## Final Principle

TENSA Engineering should become the public home, knowledge hub, and ecosystem portal for the systems it builds.

Private implementation repositories and internal source docs preserve the engineering source of truth during active development.

Public technical artifacts should be added later when they are useful, intentional, and ready.

The social content tells the story and teaches the lessons.

The website organizes everything into a clear, trusted, expandable public hub.

Long-term goal:

    Teach the ideas.
    Explain the systems.
    Preserve the work.
    Build trust.
    Convert attention into adoption.

Do not let the site grow faster than the documentation system that keeps it organized.

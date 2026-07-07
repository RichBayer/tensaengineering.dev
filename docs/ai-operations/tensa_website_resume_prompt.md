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

The latest confirmed website-content closeout merged and pushed to `main` before the current Blog planning branch was:

    5687392 Refine KB article reading experience

That commit converted the focused AI Operations project-context article into the first prose-first Knowledge Base article reading-standard proof page.

Docs-only connector / local follow-up after that closeout:

- `docs/ai-operations/tensa_website_resume_prompt.md` was refreshed after the reading-experience merge.
- `docs/planning/knowledge_base_article_template.md` was created as the canonical Knowledge Base article template / creation guide.
- This resume prompt was then updated to include the new template doc in the core context set.
- Local Legion evidence confirmed the repository tree was 27 directories and 73 files after the template-doc closeout.
- Local closeout updated the repository map, documentation strategy, website state, and resume prompt for the new template doc.

Current working branch closeout:

    feature/blog-planning-foundation

Current Blog planning branch state:

- branch contains Blog planning docs and structure-only scaffold directories
- local cleanup commit `2dfa282 Align blog strategy scaffold naming` is present on the branch
- current local tree is 41 directories and 90 files
- current public HTML page count remains 19
- no public Blog pages exist yet
- no public Blog articles exist yet
- no Blog URLs are in `sitemap.xml`
- no Blog links are in public navigation
- no Blog RSS feed, newsletter signup, comment system, guest-post flow, affiliate flow, CSS change, JavaScript change, or public HTML change exists yet

New internal Blog planning docs:

    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md

New structure-only scaffold directories:

    blog/
    blog/ai-coding/
    blog/homelab/
    blog/tools-and-models/
    blog/local-ai/
    blog/build-lessons/
    blog/buying-guides/

New structure-only Blog image asset directories:

    assets/images/blog/
    assets/images/blog/ai-coding/
    assets/images/blog/homelab/
    assets/images/blog/tools-and-models/
    assets/images/blog/local-ai/
    assets/images/blog/build-lessons/
    assets/images/blog/buying-guides/

Current public HTML page count:

    19

Latest local internal-link validation from the previous reading-experience closeout:

    Public HTML files checked: 19
    Internal links checked: 579
    External/skipped links: 21
    Result: all checked internal links and anchors resolved successfully

Important:

    The Blog planning branch is planning / scaffold only.
    It is not a public Blog launch.
    Do not assume the live site deployed just because a branch or `main` was pushed.
    GitHub Pages deployment and live-page behavior must be verified from current evidence before making deployment or indexing claims.

---

## Most Recent Completed Work

Completed in the current Blog planning branch:

- branch `feature/blog-planning-foundation` was created for Blog planning and structure-only scaffolding
- `docs/planning/blog_strategy.md` was created for future Blog strategy and category planning
- `docs/planning/blog_reader_experience.md` was created for future Blog article reader-experience planning
- `docs/planning/blog_engagement_strategy.md` was created for future Blog contact, collaboration, attribution, and link-safety planning
- structure-only future Blog scaffold directories were created under `blog/`
- structure-only future Blog image asset scaffold directories were created under `assets/images/blog/`
- planned route naming was aligned to `/blog/build-lessons/`
- repository map was updated to 41 directories and 90 files for Blog planning / scaffold state
- website information architecture was updated to include Blog as a planned long-term content pillar
- documentation strategy was updated to define ownership for Blog planning docs
- page inventory was updated to track Blog planning docs and future planned Blog public pages
- content source map was updated with future Blog page and article source requirements
- website state was updated with Blog planning / scaffold closeout state
- resume prompt was updated with Blog planning branch state and future-session context

Important:

    The Blog planning branch did not add public Blog pages, public article routes, sitemap entries, navigation links, RSS feeds, newsletter signup, comment systems, guest-post systems, affiliate systems, CSS changes, JavaScript changes, or public HTML changes.
    It created planning docs and `.gitkeep` scaffold directories only.

Previous completed work in the reading-experience branch:

- branch `feature/kb-reading-experience-standard` was committed, fast-forward merged into `main`, and pushed to `origin/main`
- focused article updated at:

        knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html

- article became the first prose-first Knowledge Base article standard / proof page
- list-heavy structure was replaced with fuller article prose
- raw/code-looking diagrams were reduced to three styled explanatory diagrams
- article metadata was changed from pill-style tags to one plain reader-context sentence
- shared `styles.css` now includes reusable Knowledge Base article diagram, FAQ, and metadata styling
- closeout docs were updated to record the article format standard and next IA direction

Completed in the docs-only connector / local closeout follow-up before the Blog branch:

- created `docs/planning/knowledge_base_article_template.md`
- defined the reusable long-form Knowledge Base article structure
- documented the project-context article as the reference implementation, not a file to blindly copy
- recorded prose, diagram, FAQ, SEO/schema, internal-link, and source-doc expectations for future articles
- added the template doc to this resume prompt's core context set
- local Legion evidence confirmed the repository tree was 27 directories and 73 files
- repository map updated for the new template doc
- documentation strategy updated to define template-doc ownership
- website state updated to record the template doc and current closeout state
- resume prompt updated to treat the template doc as core future-session context

---

## Current Next Website Direction

Immediate branch closeout:

    Finish reviewing, committing, pushing, and merging `feature/blog-planning-foundation`.

This branch should remain planning / scaffold only.

Before committing, confirm:

- only Blog planning / scaffold documentation changed
- no public HTML files changed
- no sitemap.xml changes exist
- no robots.txt changes exist
- no public navigation changes exist
- no CSS or JavaScript changes exist
- `git diff --check` is clean

Future Blog implementation option:

    feature/blog-public-foundation

Recommended first public Blog implementation goal:

    Create the Blog index, one category index, and one proof post.

Recommended first proof post:

    /blog/ai-coding/why-ai-code-breaks-after-it-works-once.html

Recommended second proof post:

    /blog/homelab/what-is-a-homelab-actually-for.html

Before creating public Blog pages or posts, load:

    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md
    docs/planning/content_source_map.md
    docs/planning/content_style_guide.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/website_state.md

Separate non-Blog high-value website work remains:

    AI Operations category / article index conversion

Recommended future branch for that work:

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

Do not start by rewriting the whole Knowledge Base or launching a full Blog operation.

Work one page / structure decision at a time.

Before creating or rewriting a long-form Knowledge Base article, load:

    docs/planning/knowledge_base_article_template.md

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
    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md
    docs/planning/content_source_map.md
    docs/planning/content_style_guide.md
    docs/planning/documentation_strategy.md
    docs/planning/glossary_strategy.md
    docs/planning/knowledge_base_article_template.md
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

    blog_strategy.md
        future Blog strategy, categories, reader groups, first-post candidates, and public implementation boundaries

    blog_reader_experience.md
        future Blog article layout, reader features, quick-answer boxes, metadata, CTAs, RSS/newsletter planning, and launch boundaries

    blog_engagement_strategy.md
        future Blog contact CTA, reader-question workflow, guest posts, collaboration, attribution, outbound-link, and affiliate/sponsored-link boundaries

    content_source_map.md
        source-doc requirements before writing factual pages

    content_style_guide.md
        public writing voice, tone, formatting, and article standards

    documentation_strategy.md
        documentation ownership, update triggers, and overlap boundaries

    glossary_strategy.md
        glossary purpose, term-selection rules, tooltip behavior, and expansion guardrails

    knowledge_base_article_template.md
        reusable structure, pacing, diagram, FAQ, SEO/schema, source-doc, and internal-link guidance for future long-form Knowledge Base articles

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

Current Blog planning / scaffold directories:

    blog/
    blog/ai-coding/
    blog/homelab/
    blog/tools-and-models/
    blog/local-ai/
    blog/build-lessons/
    blog/buying-guides/

Current Blog image planning / scaffold directories:

    assets/images/blog/
    assets/images/blog/ai-coding/
    assets/images/blog/homelab/
    assets/images/blog/tools-and-models/
    assets/images/blog/local-ai/
    assets/images/blog/build-lessons/
    assets/images/blog/buying-guides/

Important Blog boundary:

    Blog directories are structure-only placeholders.
    They contain `.gitkeep` files only.
    They do not create public Blog pages, sitemap entries, navigation links, RSS feeds, newsletter signup, or article content.

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
- Blog does not appear in current public navigation.

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
    The canonical internal template / creation guide is `docs/planning/knowledge_base_article_template.md`.

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

## Current Blog Planning State

Current status:

    Planned / scaffold only

Current internal planning docs:

    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md

Current planned categories:

    AI Coding
    Homelab
    Tools and Models
    Local AI
    Build Lessons
    Buying Guides

Current Blog boundary:

    No public Blog HTML pages exist yet.
    No public Blog articles exist yet.
    No Blog routes are in sitemap.xml.
    No Blog links are in public navigation.
    No Blog RSS feed exists yet.
    No newsletter signup exists yet.
    No comment system exists yet.
    No guest-post submission system exists yet.
    No affiliate/sponsored-link system exists yet.

Future Blog implementation should be handled on a separate branch after loading the Blog planning docs, content source map, content style guide, page inventory, internal linking strategy, and website state.

Recommended future branch:

    feature/blog-public-foundation

Recommended first proof post:

    /blog/ai-coding/why-ai-code-breaks-after-it-works-once.html

Recommended second proof post:

    /blog/homelab/what-is-a-homelab-actually-for.html

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

No Blog URLs are currently included in sitemap.xml.

Known Search Console note:

    Google reported "Page with redirect" for alternate redirect versions:
        http://tensaengineering.dev/
        https://www.tensaengineering.dev/

This is expected and harmless because the intended canonical indexed URL is:

    https://tensaengineering.dev/

Post-deploy checks after the reading-experience merge and docs-only template closeout:

- confirm the focused article loads at its canonical URL
- confirm the AI Operations page still links to the focused guide
- confirm the live sitemap still contains 19 URLs
- inspect the focused article in Google Search Console if appropriate
- do not claim indexing until webmaster-tool evidence confirms it

Do not add Blog URLs to sitemap.xml until real public Blog HTML pages exist and are ready to be indexed.

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

Blog:

- planned future public content section
- structure-only scaffold exists
- internal planning docs exist
- no public Blog pages or articles exist yet
- future practical posts should be source-aware, reader-focused, and connected to deeper Knowledge Base or Project pages where useful

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
- `docs/planning/knowledge_base_article_template.md` created as the canonical long-form Knowledge Base article template / creation guide
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
- repository map updated to 27 directories and 73 files after the Knowledge Base article template closeout
- documentation strategy updated to include Knowledge Base article template ownership
- website state updated to include the Knowledge Base article template doc and current docs-only closeout state
- resume prompt updated to include local 27 directories / 73 files evidence
- sitemap.xml contains 19 canonical URLs
- local internal-link validation passed for 579 internal links across 19 public HTML files during the latest reading-experience closeout
- `docs/planning/blog_strategy.md` created for future Blog strategy and category planning
- `docs/planning/blog_reader_experience.md` created for future Blog article reader-experience planning
- `docs/planning/blog_engagement_strategy.md` created for future Blog contact, collaboration, attribution, and link-safety planning
- structure-only future Blog scaffold directories created under `blog/`
- structure-only future Blog image asset scaffold directories created under `assets/images/blog/`
- Blog planned route naming aligned to `/blog/build-lessons/`
- repository map updated to 41 directories and 90 files for Blog planning / scaffold state
- website information architecture updated to include Blog as a planned long-term content pillar
- documentation strategy updated to define ownership for Blog planning docs
- page inventory updated to track Blog planning docs and future planned Blog public pages
- content source map updated with future Blog page and article source requirements
- website state updated with Blog planning / scaffold closeout state
- resume prompt updated with Blog planning branch state and future-session context

---

## Current Not Completed

Not yet completed:

- review, commit, push, and merge of the Blog planning closeout branch
- GitHub Pages live deployment verification after the KB reading-experience merge and docs-only template closeout
- live verification of the focused project-context article
- live verification that the AI Operations page still links to the focused article
- live verification that sitemap.xml still contains 19 canonical URLs
- Google/Bing discovery review after deployment
- AI Operations category / article index conversion
- migration of the current long-form AI Operations landing-page content into a dedicated article page
- optional stock / editorial image system for future Knowledge Base article polish
- public Blog index page
- public Blog category index pages
- first public Blog proof article
- Blog RSS feed
- Blog newsletter signup
- Blog comment system
- Blog guest-post / collaboration submission workflow
- Blog affiliate / sponsored-link disclosure workflow
- Resources page
- Build Notes section
- old-site migration plan
- permanent internal link checker script
- analytics decisions
- future install/download guidance for Argus ACLI
- public technical artifact strategy

---

## Source-Doc Rules

Before writing or significantly rewriting factual pages, check:

    docs/planning/content_source_map.md

Before creating or changing public pages, check:

    docs/planning/page_inventory.md

Before creating or rewriting long-form Knowledge Base articles, check:

    docs/planning/knowledge_base_article_template.md

Before creating or rewriting public Blog pages or posts, check:

    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md
    docs/planning/content_source_map.md
    docs/planning/content_style_guide.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md

Before adding or changing major links, check:

    docs/planning/internal_linking_strategy.md

Before assuming file paths or repo structure, check:

    docs/infrastructure/tensa_repository_map.txt

Do not write full factual Argus ACLI, Argus Lab, NeuroCore, Story, Knowledge Base, or Blog pages without the required source docs.

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

Immediate branch closeout:

1. Review the Blog planning closeout diffs.
2. Confirm only Blog planning / scaffold documentation changed.
3. Confirm no public HTML, sitemap, robots, navigation, CSS, or JavaScript files changed.
4. Commit and push `feature/blog-planning-foundation`.
5. Merge only after review.

Next Blog build option:

1. Start a future `feature/blog-public-foundation` branch.
2. Load the three Blog planning docs plus source map, style guide, page inventory, internal linking strategy, and website state.
3. Create only the Blog index, one category index, and one proof post first.
4. Do not add Blog routes to sitemap.xml or public navigation until real public Blog HTML pages exist and are ready to be indexed.
5. Keep RSS, newsletter signup, comments, guest posts, and affiliate/sponsored-link behavior deferred until the public Blog foundation is stable.

Separate non-Blog option:

1. Start a fresh branch for the AI Operations category / article index conversion.
2. Run the build-start checks.
3. Load core context docs through connector reads first.
4. Ask Richard for local git status, tree, validation, stash, and browser observations as needed.
5. Load `docs/planning/knowledge_base_article_template.md` before creating or rewriting long-form Knowledge Base articles.
6. Do not touch the protected local stash unless Richard explicitly approves that exact action.

---

## Next Public Build Options

Near-term Blog option:

- Blog public foundation branch with `/blog/`, one category index, and one proof post
- first proof post candidate: `/blog/ai-coding/why-ai-code-breaks-after-it-works-once.html`
- second proof post candidate: `/blog/homelab/what-is-a-homelab-actually-for.html`

Separate Knowledge Base option:

- AI Operations category / article index conversion
- migration of the current long-form AI Operations landing-page content into a dedicated article page
- additional focused Knowledge Base articles after source requirements and link destinations are defined

Later options:

- Resources page
- Build Notes section
- optional stock / editorial image system for future Knowledge Base or Blog article polish
- permanent internal-link checker script when manual validation becomes annoying

Keep sitemap.xml URL-only unless a reliable `lastmod` workflow is added.

---

## Final Principle

TENSA Engineering should become the public home, knowledge hub, and ecosystem portal for the systems it builds.

Private implementation repositories and internal source docs preserve the engineering source of truth during active development.

Public technical artifacts should be added later when they are useful, intentional, and ready.

The Blog should eventually answer timely practical questions and route readers toward deeper source-grounded Knowledge Base or Project pages when useful.

The social content tells the story and teaches the lessons.

The website organizes everything into a clear, trusted, expandable public hub.

Long-term goal:

    Teach the ideas.
    Explain the systems.
    Preserve the work.
    Build trust.
    Convert attention into adoption.

Do not let the site grow faster than the documentation system that keeps it organized.
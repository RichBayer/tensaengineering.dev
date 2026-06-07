# TENSA Engineering Website – Resume Prompt (Compressed)

We are continuing development of the TENSA Engineering website:

    https://tensaengineering.dev

Repository path:

    /mnt/g/ai/projects/tensaengineering.dev

Default working assumption:

    The user is usually in VS Code at the repository root with an integrated terminal open.
    Provide commands that can be copied and run from the repo root unless told otherwise.

Deployment:

    GitHub Pages

DNS / domain:

    Cloudflare

Current repository size:

    27 directories, 64 files

Verify at build start with:

    tree -a -I '.git|.obsidian|node_modules|__pycache__'

Do not rely on an old repository size count.

---

# CRITICAL OPERATING RULES

- Do NOT guess page state, repo structure, paths, links, or project facts.
- Do NOT treat prior conversation as system truth.
- Only treat uploaded docs, current file contents, repo output, and user-provided command output as truth.
- Always reference the repository map before assuming file locations.
- Ask for exact docs or files when context is missing.
- Do not edit closeout or planning docs from grep snippets alone.
- Read or request full-file context before editing closeout or planning docs.
- Use full file replacements when the user must manually paste large code/docs.
- Controlled Python edits are acceptable after full-file context has been reviewed and the intended changes are clear.

Python full-file writers are allowed when full context is loaded and the complete intended replacement is known.

Do not use Python to blindly patch unknown sections from partial context.
- Do NOT provide snippets unless explicitly requested.
- After each full-file replacement or controlled Python edit, run a targeted verification check before moving to the next file.
- Do NOT make hidden changes.
- Do NOT invent public-facing claims.
- Do NOT write factual project pages without checking source requirements.
- Do NOT let the site grow faster than the documentation system that tracks it.
- Public website copy must not sound like internal planning notes.
- Do NOT describe TENSA Engineering as “the public explanation layer,” “the teaching layer,” or merely “the public-facing explanation” of NeuroCore.
- Treat TENSA Engineering as the umbrella engineering company, public brand, and ecosystem owner.
- Treat the Knowledge Base as the public teaching/explanation layer.
- Treat NeuroCore as the platform foundation inside the TENSA ecosystem, not the thing TENSA exists only to explain.
- Keep the homepage as a front door, not a giant explanation page.

If something is unclear:

    STOP
    explain what is missing
    ask for the needed file, repo output, or source doc

---

# SESSION INITIALIZATION PROTOCOL

At the start of a serious website build session:

- Treat the session as having zero reliable prior context.
- Use connector reads first for committed repository docs when connector access is available.
- Do not ask Richard to upload every core context document by habit.
- Ask Richard for local command output that connector reads cannot provide:
    - `git status --short`
    - current `tree` output
    - current public HTML list
    - current local validation output
    - browser preview observations
- Ask Richard for exact local file contents when a file is modified, uncommitted, local-only, or about to be edited.
- During closeout, local working-tree files and local command output override connector-read committed state.
- Avoid giant all-doc upload bundles unless connector access is unavailable or many local-only files must be reviewed together.
- Do not analyze, summarize, or act on incomplete context when source docs are still being loaded.
- Begin analysis only after the required connector reads, local command output, or requested file contents are available.

Correct rhythm:

    Start of session:
        connector reads committed repo docs first
        Richard provides git status / tree / validation output
        assistant asks only for local files that are changed or needed

    During build:
        local repo becomes source of truth for edited files
        connector remains useful only for unchanged committed files

    During closeout:
        use local file contents/output for anything modified
        request exact full local docs before editing planning/closeout docs
        avoid giant upload bundles unless connector is unavailable or many local-only files changed

    After commit/push:
        connector state can be trusted again as committed baseline

---

# CONNECTOR ACCESS RULES

When repository connector access is available, the assistant may use it as the first-pass read-only source-loading mechanism for current committed repository files.

Connector-read workflow:

    use repository connector access for read-only source-of-truth retrieval
    prefer current committed repository files over prior conversation memory
    cite or clearly identify connector-read source files when summarizing retrieved context
    still request user-provided command output for local working-tree state, uncommitted changes, browser review, and validation results
    request exact local file contents when local files may differ from committed connector state
    never use connector-read committed files as closeout truth for files edited locally during the session

Default connector posture:

    read-only

Even if write-capable connector tools are available in the future:

    do not write repository files through connector tools
    do not create files through connector tools
    do not update files through connector tools
    do not delete files through connector tools
    do not commit through connector tools
    do not push through connector tools

Exception:

    Richard must explicitly authorize the specific connector write action in the current session before it is used.

Normal website workflow remains:

    assistant reads and analyzes
    assistant provides local commands, verification checks, or full-file replacement content
    Richard applies changes locally
    Richard reviews diffs
    Richard commits and pushes manually

Treat connector write capability as disabled-by-policy unless Richard explicitly enables it for a specific action.

Connector reads are appropriate for:

    committed AI-operations docs
    committed planning docs
    committed website state files
    committed public HTML/CSS/JS files
    committed repository map and source maps

Richard-provided local context is required for:

    uncommitted working-tree changes
    current git status
    current tree output
    current local validation output
    browser preview results
    local files edited during the current session before commit

Closeout and planning docs must not be edited from grep snippets alone.

If a closeout or planning doc is being edited and the connector version may be stale, request the full current local file before editing.

---

# CORE CONTEXT DOCS

Request or load these docs at the start of serious website sessions:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/ai-operations/claude/claude_website_polish_resume_prompt.md
    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/documentation_strategy.md
    docs/planning/glossary_strategy.md
    docs/planning/page_inventory.md
    docs/planning/search_answer_optimization_template.md
    docs/planning/internal_linking_strategy.md
    docs/planning/search_indexing_strategy.md
    docs/planning/content_style_guide.md
    docs/planning/seo_topic_map.md

Purpose:

    tensa_website_resume_prompt.md
        compressed startup protocol and current direction

    documentation_closeout_protocol.md
        documentation closeout workflow for serious website build sessions

    claude_website_polish_resume_prompt.md
        Claude prose-polish handoff workflow and guardrails

    website_state.md
        current live-state record

    website_information_architecture.md
        long-term website structure and expansion plan

    tensa_repository_map.txt
        authoritative repository structure and file map

    content_source_map.md
        source-doc requirements before writing factual pages

    documentation_strategy.md
        documentation ownership, update triggers, and overlap boundaries

    glossary_strategy.md
        glossary scope, term-selection rules, tooltip behavior, and expansion guardrails

    page_inventory.md
        page existence, status, purpose, navigation state, and next actions

    internal_linking_strategy.md
        logical link flow, preferred destinations, temporary links, and link-audit expectations

    search_indexing_strategy.md
        sitemap, robots.txt, Google Search Console, Bing Webmaster Tools, and indexing workflow

    search_answer_optimization_template.md
        future search-and-answer optimization workflow for page clarity and reader/search intent

    content_style_guide.md
        public writing voice, tone, formatting, and page-copy standards

    seo_topic_map.md
        future SEO topic planning and Knowledge Base search strategy

---

# BUILD-START CHECKS

At the beginning of serious website build sessions, run:

    git status --short
    tree -a -I '.git|.obsidian|node_modules|__pycache__'
    find . -maxdepth 3 -name "*.html" -print
    grep -R "href=" -n index.html about.html projects/*.html knowledge-base/*.html knowledge-base/*/*.html glossary/*.html story/*.html

For diff checks, prefer no-pager output to avoid clipped terminal pager output:

    git --no-pager diff -- <path>
    git --no-pager diff --stat

Purpose:

- confirm repository state
- confirm current tree
- confirm public page inventory
- confirm current links
- detect stale navigation targets
- prevent broken links and drift

When public links, routes, or navigation changed, prefer real local internal-link validation over grep-only review.

Future recommended permanent script:

    scripts/check_internal_links.py

---

# CURRENT SITE STATE

Current public pages:

    /
    /projects/
    /projects/neurocore.html
    /projects/argus-acli.html
    /projects/argus-lab.html
    /knowledge-base/
    /glossary/
    /about.html
    /knowledge-base/ai-operations/
    /knowledge-base/persistent-ai-memory/
    /knowledge-base/controlled-ai-systems/
    /knowledge-base/local-first-ai/
    /knowledge-base/safe-tool-interaction/
    /knowledge-base/linux-diagnostics/
    /knowledge-base/troubleshooting-training/
    /knowledge-base/neurocore-architecture/
    /story/

Current internal planning / continuity docs:

    docs/ai-operations/claude/claude_website_polish_resume_prompt.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/content_style_guide.md
    docs/planning/documentation_strategy.md
    docs/planning/internal_linking_strategy.md
    docs/planning/page_inventory.md
    docs/planning/search_indexing_strategy.md
    docs/planning/seo_topic_map.md
    docs/planning/website_information_architecture.md
    docs/website_state.md

Current public page status:

    /                           Live homepage / ecosystem front door
    /projects/                  Live ecosystem project index
    /projects/neurocore.html    Live expanded NeuroCore platform page
    /projects/argus-acli.html   Live full Argus ACLI public product page
    /projects/argus-lab.html    Live full Argus Lab public project page
    /knowledge-base/                                      Live Knowledge Base article-path hub
    /glossary/                                            Live public Glossary page
    /knowledge-base/ai-operations/                        Live Knowledge Base article
    /knowledge-base/persistent-ai-memory/                 Live Knowledge Base article
    /knowledge-base/controlled-ai-systems/                Live Knowledge Base article
    /knowledge-base/local-first-ai/                       Live Knowledge Base article
    /knowledge-base/safe-tool-interaction/                Live Knowledge Base article
    /knowledge-base/linux-diagnostics/                    Live Knowledge Base article
    /knowledge-base/troubleshooting-training/             Live Knowledge Base article
    /knowledge-base/neurocore-architecture/               Live Knowledge Base article
    /story/                                               Live full public Story page

---

# CURRENT SEARCH / SEO STATE

Current root search files:

    robots.txt
    sitemap.xml

Current sitemap URL after deployment:

    https://tensaengineering.dev/sitemap.xml

Current robots URL after deployment:

    https://tensaengineering.dev/robots.txt

Current sitemap contains canonical HTTPS non-www URLs for:

    https://tensaengineering.dev/
    https://tensaengineering.dev/about.html
    https://tensaengineering.dev/projects/
    https://tensaengineering.dev/projects/neurocore.html
    https://tensaengineering.dev/projects/argus-acli.html
    https://tensaengineering.dev/projects/argus-lab.html
    https://tensaengineering.dev/knowledge-base/
    https://tensaengineering.dev/glossary/
    https://tensaengineering.dev/story/
    https://tensaengineering.dev/knowledge-base/ai-operations/
    https://tensaengineering.dev/knowledge-base/persistent-ai-memory/
    https://tensaengineering.dev/knowledge-base/controlled-ai-systems/
    https://tensaengineering.dev/knowledge-base/local-first-ai/
    https://tensaengineering.dev/knowledge-base/safe-tool-interaction/
    https://tensaengineering.dev/knowledge-base/linux-diagnostics/
    https://tensaengineering.dev/knowledge-base/troubleshooting-training/
    https://tensaengineering.dev/knowledge-base/neurocore-architecture/

Current SEO/social metadata:

- public HTML pages have canonical URLs
- public HTML pages have tuned meta descriptions
- public HTML pages use Open Graph metadata where currently implemented
- public HTML pages use Twitter large-image card metadata where currently implemented
- public HTML pages use the dedicated TENSA social preview image where currently implemented
- public HTML pages use JSON-LD structured data where currently implemented

Current social preview asset:

    assets/images/social/tensa-og-image.png

Current search registration status:

    Google Search Console verified
    sitemap submitted successfully to Google
    Bing Webmaster Tools imported from Google Search Console
    sitemap submitted to Bing and processing
    /story/ included in sitemap.xml
    /glossary/ included in sitemap.xml locally
    /about.html included in sitemap.xml locally
    sitemap.xml is URL-only locally
    first eight Knowledge Base article URLs included in sitemap.xml locally

Latest local internal-link validation result:

    Public HTML files checked: 17
    Internal links checked: 403
    External/skipped links: 0
    Result: all checked internal links resolved successfully

Known Search Console status:

    Google reported "Page with redirect" for:
        http://tensaengineering.dev/
        https://www.tensaengineering.dev/

This is expected and harmless because those are alternate redirect versions. The intended canonical indexed version is:

    https://tensaengineering.dev/

Post-deploy search checks after the latest sitemap URL-only cleanup and documentation closeout:

- Confirm the live Knowledge Base index loads:

      https://tensaengineering.dev/knowledge-base/

- Confirm all eight Knowledge Base article URLs load live.

- Confirm the live sitemap is URL-only and includes About, Glossary, Story, and all eight Knowledge Base article URLs.

- Inspect the Knowledge Base index and key article URLs in Google Search Console if appropriate:

      https://tensaengineering.dev/knowledge-base/
      https://tensaengineering.dev/knowledge-base/ai-operations/
      https://tensaengineering.dev/knowledge-base/neurocore-architecture/

Future SEO work:

- Add or verify richer Open Graph / Twitter / JSON-LD metadata on the updated NeuroCore page.
- Keep sitemap.xml URL-only unless a reliable lastmod maintenance process is added later.
- Run a dedicated SEO/topic-map session for the first Knowledge Base article path.
- Focus future search growth on useful Knowledge Base content and clean internal links, not metadata alone.

---

# CURRENT STRATEGIC DIRECTION

TENSA Engineering is no longer just a small static site.

It is becoming:

    a modular ecosystem knowledge platform

The website should increasingly function as:

- public umbrella for the ecosystem
- structured knowledge hub
- public teaching layer
- ecosystem portal
- future product funnel
- SEO destination
- public home, knowledge hub, and ecosystem portal for NeuroCore, Argus ACLI, and Argus Lab

The site should not become one huge homepage.

Correct structure:

    Homepage
        ecosystem introduction + navigation layer

    Project pages
        major system explanations

    Story
        origin and philosophy

    Knowledge Base
        educational concept pages

    Build Notes
        readable public development history

    Resources
        future public technical artifacts, selected documentation, examples, release materials, downloads, videos, and public resources

---

# CURRENT ECOSYSTEM MODEL

TENSA Engineering:

- public hub
- brand home
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
- architecture showcase explaining runtime, control plane, tool layers, Argus diagnostics, model explanation, ACLI output, and near-term Kernel-Up / Service Intelligence expansion

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

Story:

- public origin and philosophy page
- explains the continuity failure that started NeuroCore
- explains why documentation became project memory
- connects the origin story to NeuroCore, Argus ACLI, Argus Lab, and AI Operations

AI Operations:

- disciplined AI-assisted workflow
- documentation as memory
- source-grounded session continuity
- anti-drift guardrails
- closeout protocols
- resume prompts
- human review and local verification

Private implementation repositories and internal source docs:

- preserve engineering source of truth during active development
- preserve implementation history
- preserve architecture docs and build logs
- are not currently public proof links on the website

Future public technical artifacts:

- may include selected documentation, examples, release materials, downloads, videos, or open technical components when useful

Knowledge Base:

- public teaching layer for philosophy, architecture, AI operations, diagnostics, training systems, memory/context systems, and long-term platform vision
- current live eight-article recommended path:
    - AI Operations
    - Persistent AI Memory
    - Controlled AI Systems
    - Local-First AI
    - Safe Tool Interaction
    - Linux Diagnostics
    - Troubleshooting Training
    - NeuroCore Architecture

Glossary:

- public compact reference layer for recurring ecosystem terms
- supports Knowledge Base readers without bloating every article
- provides inline tooltip destinations for selected Knowledge Base terms
- should remain compact and should not replace full Knowledge Base articles

---

# CURRENT CLAUDE POLISH WORKFLOW

A Claude-specific website polish prompt now exists at:

    docs/ai-operations/claude/claude_website_polish_resume_prompt.md

Purpose:

- preserve consistent tone and cadence across TENSA public pages
- let Claude polish readability without becoming the source of truth
- keep ChatGPT as the factual proofing / alignment layer
- preserve HTML structure, metadata, links, CSS classes, and current-vs-future boundaries
- reduce drift when using Claude for wording polish

Recommended workflow:

    ChatGPT prepares technically accurate public-page draft
    Claude polishes readability and cadence using the constrained prompt
    ChatGPT reviews Claude output for factual drift, invented claims, maturity drift, and formatting issues
    Richard reviews locally in browser before publishing

Important:

Claude should not be treated as project source of truth.

Claude improves readability.

Source docs and ChatGPT proofing preserve accuracy.

---

# CURRENT BRANDING SYSTEM

Branding hierarchy exists at:

    assets/images/branding/tensa/
    assets/images/branding/neurocore/
    assets/images/branding/argus-acli/
    assets/images/branding/argus-lab/

Current branding behavior:

- all current public pages use the header-optimized TENSA logo
- homepage hero uses the TENSA stacked logo
- Projects page hero uses the TENSA stacked logo
- NeuroCore page hero uses the NeuroCore stacked logo
- Argus ACLI page hero uses the Argus ACLI stacked logo
- Argus Lab page hero uses the Argus Lab stacked logo
- Knowledge Base index hero uses the TENSA stacked logo
- Knowledge Base articles use TENSA site branding
- Story page hero uses the TENSA stacked logo
- Glossary page uses TENSA site branding
- homepage and Projects page project cards use horizontal project logos
- transparent PNG variants are used to avoid baked black logo backgrounds
- header logo removes the tiny unreadable subtitle line

Current visual direction:

- black backgrounds
- neon green signal/circuit motif
- blue/purple accents for architecture and model explanation sections
- hexagonal / system geometry
- modern technical typography
- consistent ecosystem branding
- full-width showcase sections for complex architecture
- styled content lists instead of default browser bullets
- reusable Knowledge Base article layout
- readable Knowledge Base index links with explicit styling
- glossary reference page layout
- inline glossary tooltip styling

---

# CURRENT NAVIGATION STATE

Current primary navigation:

    Home
    Projects
    Knowledge Base
    Glossary
    Story
    About

Current targets:

    Home → /index.html
    Projects → /projects/
    Knowledge Base → /knowledge-base/
    Glossary → /glossary/
    Story → /story/
    About → /about.html

Knowledge Base points to the real `/knowledge-base/` page.

Glossary points to the real `/glossary/` page.

Story points to the real `/story/` page.

Public GitHub navigation has been removed from current public pages.

Direct public links to private implementation repositories have been removed from current public pages.

Knowledge Base index links to all eight current Knowledge Base articles.

The current Knowledge Base article path links article-to-article and loops back to the start.

Inline glossary terms in Knowledge Base articles point to `/glossary/` entries.

When `/resources/` is created:

    use it to organize future public technical artifacts, selected documentation, examples, release materials, downloads, videos, and any intentional public repository or open-component links

---

# CURRENT COMPLETED WORK

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
- Knowledge Base index created
- Knowledge Base index upgraded into a live article-path hub
- first eight Knowledge Base articles created
- Story page created
- branding asset hierarchy created
- TENSA, NeuroCore, Argus ACLI, and Argus Lab logos added
- transparent logo variants created
- header-optimized TENSA logo created
- branding integrated across all current public pages
- Knowledge Base nav links updated across current pages
- Story nav links updated across current pages
- repository map created and updated
- website state created and updated
- content source map created and updated
- page inventory created and updated
- internal linking strategy created and updated
- documentation closeout protocol created and updated
- documentation strategy created and updated
- search indexing strategy created and updated
- content style guide created
- SEO topic map created
- Claude website polish resume prompt created
- targeted verification rule added to closeout workflow
- Python full-file writer rule added to closeout workflow
- real local internal-link validation rule added to closeout workflow
- root sitemap.xml created
- `/story/` added to sitemap.xml
- eight Knowledge Base article URLs added to sitemap.xml
- root robots.txt created
- dedicated 1200 x 630 TENSA social preview image created
- canonical URLs added across current public HTML pages
- Open Graph metadata added across current public HTML pages where currently implemented
- Twitter large-image card metadata added across current public HTML pages where currently implemented
- SEO titles and meta descriptions tuned across current public pages
- Google Search Console verified
- sitemap submitted successfully to Google
- Bing Webmaster Tools imported from Google Search Console
- sitemap submitted to Bing and processing
- Glossary page created and added to primary navigation
- About page created and added to sitemap.xml
- inline glossary tooltip JavaScript added
- glossary reference styling added
- inline glossary tooltip styling added
- Knowledge Base articles received inline glossary tooltip links
- `/glossary/` added to sitemap.xml
- local internal-link validation completed successfully for 403 internal links/assets across 17 public HTML files
- glossary strategy planning doc created
- search-answer optimization template planning doc created
- repository map updated to 27 directories and 64 files

Recent completed website work:

- First eight Knowledge Base article pages created:
    - `knowledge-base/ai-operations/index.html`
    - `knowledge-base/persistent-ai-memory/index.html`
    - `knowledge-base/controlled-ai-systems/index.html`
    - `knowledge-base/local-first-ai/index.html`
    - `knowledge-base/safe-tool-interaction/index.html`
    - `knowledge-base/linux-diagnostics/index.html`
    - `knowledge-base/troubleshooting-training/index.html`
    - `knowledge-base/neurocore-architecture/index.html`
- `knowledge-base/index.html` upgraded into a live article-path hub.
- Knowledge Base article layout and index link styling added to `styles.css`.
- Article path links were validated locally.
- Temporary local internal-link validation previously checked 346 internal links successfully across 16 public HTML files; latest validation checked 403 internal links/assets across 17 public HTML files.
- `sitemap.xml` updated with `/glossary/` and the eight Knowledge Base article URLs.
- Closeout docs updated for the Knowledge Base article path, sitemap update, source requirements, link validation, and Python writer workflow.
- `story/index.html` created as a full public Story page.
- Story page explains:
    - the day the AI forgot everything
    - AI memory failure as a project continuity problem
    - documentation becoming project memory
    - workflow discipline beginning to mirror architecture discipline
    - local AI changing the direction
    - real systems requiring control
    - NeuroCore as the platform
    - Argus ACLI as the first practical product
    - Argus Lab as the early training and validation environment
    - AI Operations as the disciplined way of working behind the ecosystem
- Story page was drafted by ChatGPT, polished by Claude using constrained instructions, proofed by ChatGPT, and reviewed locally by Richard.
- Primary navigation updated so Story points to `/story/`.
- Homepage Story preview now links to `/story/`.
- `sitemap.xml` updated to include `https://tensaengineering.dev/story/`.
- `docs/ai-operations/claude/claude_website_polish_resume_prompt.md` created to preserve Claude polish workflow and reduce tone drift.
- Closeout docs updated for the new Story page, Claude prompt, sitemap entry, navigation changes, and targeted verification workflow.

Previous completed website work:

- `projects/neurocore.html` updated with a stronger public platform story.
- NeuroCore page architecture section replaced with a visual architecture showcase.
- Architecture showcase now explains:
    - CLI / ACLI
    - daemon and runtime manager
    - control plane
    - execution engine
    - Argus tool layer
    - system tool layer
    - CommandRunner and Linux
    - structured telemetry and raw evidence return path
    - Argus diagnostic result
    - model explanation layer
    - ACLI output
    - near-term Kernel-Up / Service Intelligence expansion
- NeuroCore page now includes a continuity/memory section explaining:
    - current local retrieval / RAG foundation
    - planned Karpathy-style structured knowledge base
    - planned context-aware memory / CAG-style context assembly
    - future explanation in the Knowledge Base
- NeuroCore page bottom CTA cleaned up:
    - Review the architecture
    - Explore Argus ACLI
    - Explore Argus Lab
- `projects/argus-acli.html` upgraded into a full public product page.
- Argus ACLI page now emphasizes:
    - local-first diagnostics
    - no pasting sensitive system data into cloud chatbots
    - read-only Linux system intelligence
    - raw evidence
    - AI explanation grounded in structured diagnostics
    - NeuroCore as the controlled runtime
- `styles.css` updated with:
    - architecture showcase styling
    - improved card/list styling
    - responsive behavior for architecture sections

Current Glossary / tooltip work completed:

- `glossary/index.html` created as a compact public reference page.
- `assets/js/glossary-tooltips.js` created for inline glossary tooltip behavior.
- Glossary reference layout and tooltip styling added to `styles.css`.
- Primary navigation updated to include Glossary across current public pages.
- Knowledge Base articles received selected inline glossary tooltip links.
- Glossary links were kept out of footers after cleanup.
- Internal link validation passed after glossary/nav changes.
- `docs/planning/glossary_strategy.md` created.
- `docs/planning/search_answer_optimization_template.md` created.
- Closeout docs updated to reflect connector-read / local-working-tree workflow improvements.


Current public-page cleanup completed:

- Public GitHub navigation removed from current public pages.
- Direct public links to private implementation repositories removed from current public pages.
- Homepage repository-proof section replaced with public explanation / future public artifacts framing.
- Knowledge Base repository-proof language replaced with public artifacts language.
- NeuroCore business-safety wording softened into controlled system awareness and local-first design language.
- Argus ACLI and Story wording standardized around Argus ACLI as the first practical product built on NeuroCore.
- Resources page deferred until useful public artifacts exist.

---

# CURRENT NOT COMPLETED

Not yet completed:

- Resources page
- Contact page
- Contact email forwarding setup
- Build Notes section
- old-site migration plan
- permanent internal link checker script
- analytics decisions
- future install/download guidance for Argus ACLI
- deeper NeuroCore metadata / SEO pass after latest page expansion
- dedicated SEO/topic-map session for the first Knowledge Base article path
- live sitemap confirmation after latest sitemap URL-only cleanup deployment
- Google Search Console inspection of Knowledge Base index and key article URLs after deployment if appropriate
- article templates for future Knowledge Base expansion
- public technical artifact strategy
- public repository / open-component strategy

---

# SOURCE-DOC RULES

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

# PUBLIC WRITING RULES

Public pages should:

- be professional, practical, and technically credible
- sound human and builder-oriented
- explain technical terms in plain language
- avoid AI hype
- avoid corporate fluff
- avoid over-compressed explanations
- distinguish current reality from future plans
- use conversational prose for story/explainer pages
- use bullets only when they improve clarity
- route readers toward deeper pages instead of dumping everything on one page

Public pages should not:

- sound like internal instructions
- say “this section should”
- expose internal planning language
- overstate product maturity
- imply future features already exist
- duplicate entire technical repository docs

---

# EDITING RULE

The user prefers full file replacements when manual copy/paste editing would be error-prone.

Do not provide small manual find/replace snippets unless explicitly requested.

For code, HTML, CSS, or long Markdown replacements that the user must paste manually:

    provide the complete replacement file

For closeout docs and planning docs:

    do not edit from grep snippets alone
    first review or request the full current file
    then use the smallest safe edit

Controlled Python edits are acceptable after full-file context has been reviewed and the intended changes are clear.

For mechanical multi-file link corrections, command-based edits are acceptable only when the user approves the workflow.

---

# REPLACEMENT VERIFICATION RULE

After each full-file replacement during closeout or live website editing, run a targeted verification check before moving to the next file.

The verification should confirm:

- the intended new text, link, or status exists
- stale text, links, or statuses were removed when applicable
- the correct file was edited
- the file was saved
- no obvious paste truncation occurred

Example checks:

    grep -n 'href="../story/"\|href="../index.html#story"' projects/argus-acli.html
    grep -n "27 directories, 64 files\|glossary/index.html\|assets/js/glossary-tooltips.js" docs/infrastructure/tensa_repository_map.txt
    grep -n "https://tensaengineering.dev/knowledge-base/neurocore-architecture/" sitemap.xml

Do not move to the next replacement until verification passes or the mismatch is understood and corrected.

---

# DOCUMENTATION CLOSEOUT RULES

During closeout:

- Do not silently rewrite docs.
- Do not make unknown documentation changes.
- Do not perform broad cleanup unless explicitly requested.
- Only update docs directly impacted by the build session.
- Preserve unchanged sections unless modification is needed.
- Explain what each closeout doc update is meant to capture.
- Keep closeout docs aligned with real repo state.
- Run targeted verification after each full-file replacement.

Closeout docs usually include:

    docs/infrastructure/tensa_repository_map.txt
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md

Update only the docs actually impacted by the session.

---

# CURRENT NEXT BEST STEP

Recommended next website session priority:

    1. Set up email routing or forwarding for contact@tensaengineering.dev.
    2. Confirm the address forwards correctly before publishing it publicly.
    3. Create or plan /contact.html only after email routing is confirmed.

Planned Contact page:

    Future path: /contact.html
    Planned public email: contact@tensaengineering.dev
    Purpose: allow readers to ask questions, report site issues, or make appropriate TENSA Engineering inquiries.
    Do not publish the Contact page until email routing or forwarding is confirmed.

Later-phase public-page idea:

    FAQ page after recurring site, project, product, or Knowledge Base questions emerge.

Recommended SEO/topic work:

    Run a dedicated SEO/topic-map session for the first Knowledge Base article path.

Reason:

The homepage, About page, Projects, NeuroCore, Argus ACLI, Argus Lab, Knowledge Base, Glossary, Story, and the first eight Knowledge Base articles now all have public site structure. The next website session should confirm the public contact path, organize public resources, publish public-friendly build history, or expand the teaching layer with additional focused articles.

---

# NEXT PUBLIC BUILD OPTIONS

Possible next public work:

1. Set up and confirm forwarding for `contact@tensaengineering.dev`.
2. Review `/about.html` locally and polish it only if needed.
3. Create `/contact.html` after email forwarding is confirmed.
4. Create `/resources/index.html`.
5. Create `/build-notes/index.html`.
6. Run a dedicated SEO/topic-map pass for the first Knowledge Base article path.
7. Add deeper SEO/metadata pass for updated pages.
8. Keep sitemap.xml URL-only unless a reliable lastmod maintenance process is added later.
9. Create permanent internal link checker script.
10. Create additional focused Knowledge Base articles.
11. Review glossary terms after future Knowledge Base expansion.
12. Use the search-answer optimization template during a focused SEO/content clarity pass.

Recommended next direction:

    Confirm the public contact path, then create or plan the Contact page.

Reason:

The homepage, About page, core project pages, Glossary, Story page, Knowledge Base index, and first eight Knowledge Base articles now exist. The next session should make TENSA easier to understand and contact without publishing an unconfirmed email address.

---

# FINAL PRINCIPLE

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
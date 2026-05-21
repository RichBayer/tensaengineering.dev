# TENSA Engineering Website State

---

## Current Status

TENSA Engineering website foundation is live.

The site is transitioning from a small static landing page into a modular ecosystem knowledge platform.

Current phase:

    live public website foundation
    information architecture complete
    homepage refined
    Projects section created
    NeuroCore project page expanded into a stronger public platform page
    Argus ACLI project page upgraded into a full public product page
    Argus Lab full public landing page created
    Story page created
    branding asset hierarchy established
    consistent branding added across current public pages
    Knowledge Base index created
    page inventory created
    internal linking strategy created
    repository map updated
    content style guide created
    SEO topic map created
    Claude website polish prompt created
    closeout verification workflow improved

The site now functions more like an ecosystem portal than a single landing page.

The homepage remains the front door.

Deeper explanations are moving into dedicated pages.

---

## URL

Primary domain:

    https://tensaengineering.dev

Domain provider / DNS:

    Cloudflare

Deployment:

    GitHub Pages

HTTPS:

    enabled

---

## Repository

Local path:

    /mnt/g/ai/projects/tensaengineering.dev

Current key files:

- index.html
- styles.css
- README.md
- CNAME
- robots.txt
- sitemap.xml
- assets/images/branding/tensa/
- assets/images/branding/neurocore/
- assets/images/branding/argus-acli/
- assets/images/branding/argus-lab/
- assets/images/social/tensa-og-image.png
- projects/index.html
- projects/neurocore.html
- projects/argus-acli.html
- projects/argus-lab.html
- knowledge-base/index.html
- story/index.html
- docs/ai-operations/claude/claude_website_polish_resume_prompt.md
- docs/ai-operations/documentation_closeout_protocol.md
- docs/ai-operations/tensa_website_resume_prompt.md
- docs/infrastructure/tensa_repository_map.txt
- docs/planning/content_source_map.md
- docs/planning/content_style_guide.md
- docs/planning/documentation_strategy.md
- docs/planning/internal_linking_strategy.md
- docs/planning/page_inventory.md
- docs/planning/search_indexing_strategy.md
- docs/planning/seo_topic_map.md
- docs/planning/website_information_architecture.md
- docs/website_state.md

Current repository size:

    17 directories, 51 files

Last verified by user-provided output during closeout:

    git status --short
    tree -a -I '.git|.obsidian|node_modules|__pycache__'
    find . -maxdepth 3 -name "*.html" -print
    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html story/*.html

---

## Current Website Structure

Current public pages:

    /
    /projects/
    /projects/neurocore.html
    /projects/argus-acli.html
    /projects/argus-lab.html
    /knowledge-base/
    /story/

Current internal planning / continuity docs:

    docs/ai-operations/claude/claude_website_polish_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/ai-operations/tensa_website_resume_prompt.md
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

---

## Current Branding System

A formal branding asset hierarchy has been established.

Current asset structure:

    assets/images/branding/tensa/
    assets/images/branding/neurocore/
    assets/images/branding/argus-acli/
    assets/images/branding/argus-lab/

Current TENSA branding assets:

    tensa-horizontal-logo.png
    tensa-horizontal-logo-transparent.png
    tensa-horizontal-header-transparent.png
    tensa-stacked-logo.png
    tensa-stacked-logo-transparent.png

Current NeuroCore branding assets:

    neurocore-horizontal.png
    neurocore-horizontal-transparent.png
    neurocore-stacked.png
    neurocore-stacked-transparent.png

Current Argus ACLI branding assets:

    argus-acli-neurocore-horizontal.png
    argus-acli-neurocore-horizontal-transparent.png
    argus-acli-neurocore-stacked.png
    argus-acli-neurocore-stacked-transparent.png
    argus-acli-system-intelligence-horizontal.png
    argus-acli-system-intelligence-horizontal-transparent.png
    argus-acli-system-intelligence-stacked.png
    argus-acli-system-intelligence-stacked-transparent.png

Current Argus Lab branding assets:

    argus-lab-interactive-analysis-horizontal.png
    argus-lab-interactive-analysis-horizontal-transparent.png
    argus-lab-interactive-analysis-stacked.png
    argus-lab-interactive-analysis-stacked-transparent.png
    argus-lab-neurocore-horizontal.png
    argus-lab-neurocore-horizontal-transparent.png
    argus-lab-neurocore-stacked.png
    argus-lab-neurocore-stacked-transparent.png

Current social preview asset:

    assets/images/social/tensa-og-image.png

Current branding behavior:

- all current public pages use the TENSA header logo
- homepage hero uses the TENSA stacked logo
- Projects page hero uses the TENSA stacked logo
- NeuroCore page hero uses the NeuroCore stacked logo
- Argus ACLI page hero uses the Argus ACLI stacked logo
- Argus Lab page hero uses the Argus Lab stacked logo
- Story page hero uses the TENSA stacked logo
- homepage and Projects project cards use horizontal project logos
- transparent PNG variants are used to avoid baked black logo backgrounds
- the header uses a header-optimized TENSA logo without the tiny unreadable subtitle line

Current visual direction:

- black backgrounds
- neon green signal/circuit motif
- blue/purple accents for architecture and model explanation sections
- hexagonal / system geometry
- modern technical typography
- consistent ecosystem branding
- full-width showcase sections for complex architecture
- styled content lists instead of default browser bullets

---

## Current Navigation State

Current primary navigation:

    Home
    Projects
    Knowledge Base
    Story
    GitHub

Current navigation targets:

    Home → /index.html
    Projects → /projects/
    Knowledge Base → /knowledge-base/
    Story → /story/
    GitHub → mixed current behavior:
        homepage and most pages use /index.html#proof
        NeuroCore page header links directly to the NeuroCore GitHub repo

Important note:

    Knowledge Base points to the real /knowledge-base/ page.
    Story points to the real /story/ page.

When /resources/ or a GitHub/resources page is created, decide whether GitHub remains a homepage proof anchor, links directly to GitHub, or moves into Resources.

---

## Current Search / SEO Foundation

Current search support files:

    robots.txt
    sitemap.xml

Current sitemap URL:

    https://tensaengineering.dev/sitemap.xml

Current robots URL:

    https://tensaengineering.dev/robots.txt

Current sitemap contents:

- https://tensaengineering.dev/
- https://tensaengineering.dev/projects/
- https://tensaengineering.dev/projects/neurocore.html
- https://tensaengineering.dev/projects/argus-acli.html
- https://tensaengineering.dev/projects/argus-lab.html
- https://tensaengineering.dev/knowledge-base/
- https://tensaengineering.dev/story/

Current public HTML metadata support:

- canonical URLs are present on current public pages
- meta descriptions are present on current public pages
- Open Graph metadata is present where currently implemented
- Twitter large-image card metadata is present where currently implemented
- the dedicated TENSA social preview image is used where currently implemented
- JSON-LD structured data is present where currently implemented

Current indexing status:

    sitemap.xml created
    robots.txt created
    Google Search Console verified
    sitemap submitted successfully to Google
    Bing Webmaster Tools imported from Google Search Console
    sitemap submitted to Bing and processing
    /story/ added to sitemap locally during Story page closeout

Known Search Console note:

    Google reported "Page with redirect" for alternate redirect versions:
        http://tensaengineering.dev/
        https://www.tensaengineering.dev/

This is expected and harmless because the intended canonical indexed URL is:

    https://tensaengineering.dev/

Future SEO work:

- After deployment, confirm the live sitemap includes https://tensaengineering.dev/story/.
- Inspect https://tensaengineering.dev/story/ in Google Search Console if appropriate.
- Add or verify richer Open Graph / Twitter / JSON-LD metadata on the updated NeuroCore page.
- Optionally add sitemap lastmod dates.
- Focus future search growth on Knowledge Base pages, not metadata alone.

---

## Current Homepage

Current path:

    index.html

Current status:

    Live

The current homepage includes:

- TENSA Engineering branded header
- TENSA branded hero section
- controlled AI systems positioning
- core philosophy section
- ecosystem overview
- NeuroCore project card with logo
- Argus ACLI project card with logo
- Argus Lab project card with logo
- Knowledge Base direction preview
- origin story preview
- link to the full Story page
- GitHub proof section
- links to NeuroCore and Argus Lab GitHub repos
- navigation to Projects, Knowledge Base, and Story

The homepage treats TENSA Engineering as the single public hub for the ecosystem.

The homepage should remain concise.

It should stay a front door and navigation layer, not become a giant explanation page.

---

## Current Projects Page

Current path:

    projects/index.html

Current status:

    Live

Current purpose:

- explain the TENSA ecosystem
- separate NeuroCore, Argus ACLI, and Argus Lab
- provide a clean internal route from the homepage
- link to the NeuroCore detail page
- link to the Argus ACLI page
- link to the Argus Lab page
- reinforce the platform / product / lab model
- route to the Story page through primary navigation

Current project model:

    NeuroCore = platform
    Argus ACLI = first product / distribution
    Argus Lab = future training and validation environment

Current branding:

- TENSA header logo
- TENSA stacked logo in hero
- project logos in project cards

---

## Current NeuroCore Page

Current path:

    projects/neurocore.html

Current status:

    Live expanded platform page

Current purpose:

    Public NeuroCore platform explainer.

Current branding:

- TENSA header logo
- NeuroCore stacked logo in hero

Current content includes:

- local-first governed AI runtime positioning
- continuity / stateless AI problem
- privacy and business-safety framing
- current local retrieval / RAG foundation
- planned Karpathy-style structured knowledge base direction
- planned context-aware memory / CAG-style context assembly direction
- control plane and governed authority explanation
- visual architecture showcase
- daemon / runtime manager
- control plane
- execution engine
- Argus tool layer
- system tool layer
- CommandRunner and Linux boundary
- structured telemetry and raw evidence return path
- model explanation layer
- ACLI output layer
- near-term Kernel-Up / Service Intelligence expansion
- production-environment value proposition
- Argus ACLI as first distribution
- Argus Lab as future training and validation environment
- cleaned bottom CTA flow
- primary navigation to the Story page

Important note:

The NeuroCore page should stay public-facing and business-readable.

Do not turn it into a dry architecture reference page.

Future architecture detail should move into Knowledge Base pages and Build Notes pages, then be linked from the NeuroCore page.

---

## Current Argus ACLI Page

Current path:

    projects/argus-acli.html

Current status:

    Live full public product page

Current purpose:

- explain Argus ACLI as the first practical product / distribution built on NeuroCore
- explain local-first read-only Linux diagnostics
- explain why users should not have to paste sensitive logs and system data into cloud chatbots
- explain raw evidence, structured findings, severity, recommendations, and model explanation
- route readers back to NeuroCore and forward to Argus Lab
- route to the Story page through primary navigation

Current branding:

- TENSA header logo
- Argus ACLI stacked logo in hero

Current content includes:

- local-first Linux system intelligence positioning
- under-active-development status
- Linux troubleshooting problem statement
- read-only / evidence-backed / local-first principles
- NeuroCore origin connection
- example diagnostic output
- AI explanation grounded by deterministic evidence
- NeuroCore foundation
- command-line experience
- intended audience
- ecosystem role

Important note:

Argus ACLI should remain honest about current product maturity.

Do not imply install/download readiness until product packaging exists.

---

## Current Argus Lab Page

Current path:

    projects/argus-lab.html

Current status:

    Live full public landing page

Current purpose:

- explain Argus Lab as a planned real-Linux troubleshooting, training, and validation environment
- explain its origin as a personal Linux troubleshooting practice and portfolio project
- explain controlled failure scenarios and resettable lab sessions
- explain mentor-style AI guidance without implying the model gives away answers
- explain the validation role for NeuroCore, Argus ACLI, and model-guided troubleshooting
- keep future-phase status clear and honest
- route readers to Argus ACLI, NeuroCore, and the Projects page
- route to the Story page through primary navigation

Current branding:

- TENSA header logo
- Argus Lab stacked logo in hero

Current content includes:

- planned training and validation environment positioning
- real troubleshooting skill through experience, not memorization
- real systems, controlled failures, and guided growth principles
- support-ticket-style troubleshooting scenarios
- safe repeatable training loop
- NeuroCore, Argus ACLI, and model guidance relationship
- independent, assisted, and guided resolution modes
- validation and regression-testing role
- planned small-business-style Linux environment shape
- future-phase status / not currently available
- learner, diagnostics, and growth audiences
- clear explanation of what Argus Lab is not

Important note:

Argus Lab should remain clearly future-phase until implementation status changes.

Do not imply it is currently available, downloadable, or a finished training product.

---

## Current Knowledge Base Page

Current path:

    knowledge-base/index.html

Current status:

    Structure-only public index

Current purpose:

- establish the Knowledge Base as a top-level public site section
- move TENSA away from pure landing-page structure
- introduce major educational topic areas
- prepare for future modular knowledge-base articles
- route to the Story page through primary navigation

Current branding:

- TENSA header logo
- TENSA stacked logo in hero

Current topic areas introduced:

- Controlled AI Systems
- AI Operations
- Persistent AI Memory
- Local-First AI
- Safe Tool Interaction
- Linux Diagnostics
- Troubleshooting Training
- NeuroCore Architecture

Important note:

The Knowledge Base index is public-facing.

It should not read like an internal writing guide.

Future article/category pages should be created deliberately and tracked in:

    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/content_source_map.md

---

## Current Story Page

Current path:

    story/index.html

Current status:

    Live full public Story page

Current purpose:

- tell the origin story behind NeuroCore and TENSA Engineering
- explain the continuity failure that exposed the core lesson
- explain why documentation became project memory
- explain why workflow discipline started to mirror architecture discipline
- explain how local AI changed the direction
- explain why real systems required control
- connect NeuroCore, Argus ACLI, Argus Lab, and AI Operations

Current branding:

- TENSA header logo
- TENSA stacked logo in hero

Current content includes:

- the day the AI forgot everything
- early Linux learning and lab-building context
- reliance on AI as the memory layer
- documentation becoming the project’s memory
- workflow discipline becoming part of the system philosophy
- local-first AI direction
- authority boundaries
- NeuroCore as the platform
- Argus ACLI as the first practical proof
- Argus Lab as the future training and validation environment
- AI Operations as the disciplined way of working that made the system possible

Important note:

The Story page should remain human, grounded, and readable.

Do not turn it into:

- a technical architecture manual
- a Knowledge Base article
- a roadmap dump
- an internal planning document
- a hype-heavy marketing page

Deeper technical definitions belong in the Knowledge Base.

---

## Current Claude Polish Workflow

Current path:

    docs/ai-operations/claude/claude_website_polish_resume_prompt.md

Current status:

    Live internal AI-operations prompt

Current purpose:

- preserve consistent tone and cadence across TENSA public website pages
- define Claude as a prose-polish layer only
- keep ChatGPT as the factual proofing / alignment layer
- preserve HTML structure, metadata, links, CSS classes, and current-vs-future boundaries
- reduce drift when using Claude to improve readability

Current workflow:

    ChatGPT prepares technically accurate public-page draft
    Claude polishes readability and cadence using the constrained prompt
    ChatGPT reviews Claude output for factual drift, invented claims, maturity drift, and formatting issues
    Richard reviews locally in browser before publishing

Important note:

Claude should not be treated as the source of truth.

Claude improves readability.

Source docs and ChatGPT proofing preserve accuracy.

---

## Long-Term Website Direction

TENSA Engineering is intended to become:

- public umbrella for the ecosystem
- structured knowledge hub
- SEO-focused authority site
- public explanation layer for NeuroCore, Argus ACLI, and Argus Lab
- educational resource for controlled AI systems
- educational resource for persistent AI memory
- educational resource for local-first AI
- educational resource for safe tool interaction
- educational resource for AI operations
- future product funnel for Argus ACLI and later offerings

The site should expand into many categorized pages over time.

It should not become one massive homepage.

---

## Single Website Rule

TENSA Engineering is the only long-term public website.

The existing Argus ACLI landing page should be treated as temporary / legacy.

Long-term direction:

    tensaengineering.dev becomes the single public website.

Do not plan to maintain both TENSA and a separate Argus ACLI website long term.

Future work should migrate useful Argus ACLI landing page content into TENSA before retiring or redirecting the old site.

---

## Current Public Ecosystem

TENSA Engineering:

- public hub
- brand home
- knowledge base
- public explanation layer
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
- near-term Kernel-Up / Service Intelligence expansion

Argus ACLI:

- first product / distribution built on NeuroCore
- local-first read-only Linux diagnostics
- real telemetry
- structured findings
- severity classification
- recommendations
- raw evidence
- AI explanation grounded in structured evidence

Argus Lab:

- future real-Linux troubleshooting, training, and validation environment
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

GitHub repositories:

- engineering proof
- implementation history
- source-of-truth documentation
- architecture docs
- build logs
- credibility layer

Social content:

- educational discovery engine
- storytelling layer
- build-in-public traffic driver

---

## Completed

- GitHub repository created
- repository cloned locally
- initial static homepage created
- stylesheet created
- CNAME file created
- domain name acquired through Cloudflare
- GitHub Pages enabled
- Cloudflare DNS configured
- DNS check completed successfully
- HTTPS enabled
- tensaengineering.dev is live
- README expanded to capture long-term website vision
- AI resume prompt created for future planning continuity
- website information architecture plan created
- homepage refined around TENSA as the single public hub
- Projects overview page created
- NeuroCore project page created
- NeuroCore page expanded into a stronger public platform page
- Argus ACLI placeholder page created
- Argus ACLI full public product page created
- Argus Lab full public landing page created
- Story page created
- long-form article styling added
- project links updated so pages route internally
- Story navigation updated to point to `/story/`
- TENSA repository map created
- content source map created
- branding asset hierarchy created
- TENSA horizontal and stacked logos added
- NeuroCore, Argus ACLI, and Argus Lab logos copied from NeuroCore repo
- transparent logo variants created
- header-optimized TENSA logo created
- homepage branding integrated
- project card logo treatment added
- Projects page branding updated
- NeuroCore page branding updated
- Argus ACLI page branding updated
- Argus Lab full public landing page created and branded
- Story page branded
- Knowledge Base index page created
- Knowledge Base navigation updated across current public pages
- page inventory planning doc created
- internal linking strategy planning doc created
- TENSA website documentation closeout protocol created
- TENSA website documentation strategy created
- TENSA search indexing strategy created
- content style guide created
- SEO topic map created
- Claude website polish resume prompt created
- targeted verification rule added to closeout workflow
- root sitemap.xml created
- `/story/` added to sitemap.xml
- root robots.txt created
- dedicated TENSA social preview image created
- canonical URLs added across current public HTML pages
- Open Graph metadata added where currently implemented
- Twitter large-image card metadata added where currently implemented
- SEO titles and meta descriptions tuned across current public pages
- Google Search Console verified
- sitemap submitted successfully to Google
- Bing Webmaster Tools imported from Google Search Console
- sitemap submitted to Bing and processing
- Search Console redirect warning reviewed and confirmed as expected redirect behavior

---

## Not Yet Completed

- Resources page
- About page
- Build Notes section
- analytics decisions
- Google Search Console indexing data review after processing
- Bing Webmaster Tools indexing data review after processing
- live sitemap confirmation after Story deployment
- Google Search Console inspection of Story URL after deployment if appropriate
- old-site migration plan
- internal link checker script
- Knowledge Base category pages
- Knowledge Base article pages
- article templates
- future install/download guidance for Argus ACLI
- deeper NeuroCore metadata / SEO pass after latest page expansion
- optional sitemap lastmod dates

---

## Core Anti-Drift Context Pack

Use these docs at the start of future serious website sessions:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/ai-operations/claude/claude_website_polish_resume_prompt.md
    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/content_style_guide.md
    docs/planning/documentation_strategy.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/search_indexing_strategy.md
    docs/planning/seo_topic_map.md

Purpose of each:

    tensa_website_resume_prompt.md
        fresh-thread startup context

    documentation_closeout_protocol.md
        end-of-session documentation closeout workflow

    claude_website_polish_resume_prompt.md
        Claude prose-polish handoff workflow and guardrails

    website_state.md
        live-current-state record

    website_information_architecture.md
        long-term structure and planning direction

    tensa_repository_map.txt
        real repository structure and file map

    content_source_map.md
        required source docs before writing factual pages

    content_style_guide.md
        public writing voice, tone, formatting, and page-copy standards

    documentation_strategy.md
        documentation ownership, update triggers, and overlap boundaries

    page_inventory.md
        page existence, status, purpose, and next-action tracker

    internal_linking_strategy.md
        logical linking map, preferred destinations, temporary links, and link-audit expectations

    search_indexing_strategy.md
        sitemap, robots.txt, search engine registration, and indexing workflow

    seo_topic_map.md
        future SEO topic planning and Knowledge Base search strategy

---

## Build-Start Checks

At the beginning of serious website build sessions, run:

    git status --short
    tree -a -I '.git|.obsidian|node_modules|__pycache__'
    find . -maxdepth 3 -name "*.html" -print
    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html story/*.html

Future recommended replacement for manual link grep:

    scripts/check_internal_links.py

Purpose:

- confirm repository state
- confirm current tree
- confirm public page inventory
- confirm current links
- detect old navigation targets
- prevent broken links and drift

---

## Replacement Verification Rule

After each full-file replacement during closeout or live website editing, run a targeted verification check before moving to the next file.

The verification should confirm the intended change landed and old/stale text or links were removed when applicable.

Examples:

    grep -n 'href="../story/"\|href="../index.html#story"' projects/argus-lab.html
    grep -n "17 directories, 51 files\|story/index.html" docs/infrastructure/tensa_repository_map.txt
    grep -n "https://tensaengineering.dev/story/" sitemap.xml

This rule exists to catch:

- paste mistakes
- missed saves
- wrong-file edits
- stale snippets
- unintended partial replacements
- accidental edits to the wrong file

---

## Next Recommended Steps

Recommended next website session:

1. Run build-start checks.
2. Confirm repo is clean.
3. Review `docs/planning/page_inventory.md`.
4. Review `docs/planning/internal_linking_strategy.md`.
5. Review `docs/planning/content_source_map.md`.
6. Choose the next page or section deliberately before editing.

Recommended next public-page work:

    Resources page, About page, first Knowledge Base category pages, or Build Notes section

Reason:

NeuroCore, Argus ACLI, Argus Lab, Knowledge Base, and Story now all have public site structure. The next major website step should either organize public resources, add concise organizational identity, or begin focused teaching articles.

Recommended post-deploy checks after this session:

1. Confirm the Story page loads live:

       https://tensaengineering.dev/story/

2. Confirm the live sitemap includes Story:

       https://tensaengineering.dev/sitemap.xml

3. Inspect the Story URL in Google Search Console if appropriate:

       https://tensaengineering.dev/story/

---

## Source Docs Used Recently

Recent NeuroCore and Argus ACLI page work used context from:

- NeuroCore Vision
- Platform Ecosystem
- System Architecture
- System State
- Control Plane Architecture
- Tool Execution Architecture
- Security & Policy Architecture
- Argus ACLI specification
- Argus ACLI vision
- Argus System Summary design
- Phase 5J Argus Core Tool Expansion
- Service Intelligence Layer / Kernel-Up Service Intelligence design
- Context-Aware Memory Architecture
- Karpathy-Style Knowledge Base Layer
- NeuroCore / Argus platform context pack
- current website pages
- current `styles.css`

Recent Story page work used context from:

- NeuroCore origin story source material
- The Day The AI Forgot Everything source material
- AI Operations methodology split source material
- current public NeuroCore page
- current public Argus ACLI page
- current public Argus Lab page
- content style guide
- website information architecture
- website state
- Claude website polish workflow
- local browser review

Important:

Old build logs may contain former project names.

Public website copy should use NeuroCore unless explicitly discussing historical renaming.

---

## Working Rules

Use full file replacements only.

Do not provide snippets unless explicitly requested.

After each full-file replacement, run a targeted verification check before moving to the next file.

Do not make hidden changes.

No changes the user does not know about.

Before replacing a file, inspect or request the current full file contents unless it was generated in the same session and not changed afterward.

Do not guess.

If more context is needed, ask for the exact file or doc.

Use source docs before writing factual project pages.

Check the content source map before writing or significantly rewriting factual project pages:

    docs/planning/content_source_map.md

Check page inventory before creating or changing public pages:

    docs/planning/page_inventory.md

Check internal linking strategy before adding or changing major links:

    docs/planning/internal_linking_strategy.md

Keep the information architecture top-down and coherent.

Avoid turning every page into an encyclopedia.

TENSA site should organize the ecosystem and teach the public.

NeuroCore repo proves the engineering.

Argus ACLI page explains the product.

Argus Lab page explains training and validation.

Story explains origin and philosophy.

Knowledge Base teaches the philosophy, architecture, and methods.

Do not overbuild implementation before planning the site structure.

Build one page at a time.

---

## Tone

Professional, practical, technical but understandable.

Avoid AI hype.

Avoid corporate fluff.

Use clear builder-focused language.

Explain complicated architecture in plain English before or immediately after introducing technical terminology.

Use the real origin story where appropriate.

Do not compress important story into tiny marketing snippets when the page needs a fuller explanation.

Keep public pages honest about what exists now, what is being built, and what is future-phase.

---

## Guiding Rule

Do not expand the website randomly.

Plan the information architecture first, then build the site structure around that plan.

Build one page at a time.

The homepage is the front door.

Project pages explain the major systems.

Story pages explain origin and philosophy.

Knowledge Base pages teach individual concepts.

Build Notes explain how the system evolved.

GitHub remains the source of truth.

The site should never grow faster than the documentation system that keeps it organized.
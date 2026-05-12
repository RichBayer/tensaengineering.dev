# TENSA Engineering Website State

---

## Current Status

TENSA Engineering website foundation is live.

The site is transitioning from a small static landing page into a modular ecosystem knowledge platform.

Current phase:

    live public website foundation
    information architecture complete
    homepage refined
    initial Projects section created
    NeuroCore project page rewritten as story-first explainer
    Argus ACLI and Argus Lab placeholder pages created
    branding asset hierarchy established
    consistent branding added across current public pages
    Knowledge Base index created
    page inventory created
    internal linking strategy created
    repository map updated

The site now functions more like an ecosystem portal than a single landing page.

The homepage remains the front door.

Deeper explanations are beginning to move into dedicated pages.

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
- assets/images/branding/tensa/
- assets/images/branding/neurocore/
- assets/images/branding/argus-acli/
- assets/images/branding/argus-lab/
- projects/index.html
- projects/neurocore.html
- projects/argus-acli.html
- projects/argus-lab.html
- knowledge-base/index.html
- docs/ai-operations/documentation_closeout_protocol.md
- docs/ai-operations/tensa_website_resume_prompt.md
- docs/infrastructure/tensa_repository_map.txt
- docs/planning/content_source_map.md
- docs/planning/internal_linking_strategy.md
- docs/planning/page_inventory.md
- docs/planning/website_information_architecture.md
- docs/website_state.md

Current repository size:

    14 directories, 42 files

---

## Current Website Structure

Current public pages:

    /
    /projects/
    /projects/neurocore.html
    /projects/argus-acli.html
    /projects/argus-lab.html
    /knowledge-base/

Current internal planning / continuity docs:

    docs/ai-operations/documentation_closeout_protocol.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/internal_linking_strategy.md
    docs/planning/page_inventory.md
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

Current branding behavior:

- all current public pages use the TENSA header logo
- homepage hero uses the TENSA stacked logo
- Projects page hero uses the TENSA stacked logo
- NeuroCore page hero uses the NeuroCore stacked logo
- Argus ACLI placeholder hero uses the Argus ACLI stacked logo
- Argus Lab placeholder hero uses the Argus Lab stacked logo
- homepage and Projects project cards use horizontal project logos
- transparent PNG variants are used to avoid baked black logo backgrounds
- the header uses a header-optimized TENSA logo without the tiny unreadable subtitle line

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
    Story → /index.html#story
    GitHub → /index.html#proof

Important note:

    Knowledge Base now points to the real /knowledge-base/ page.

Story and GitHub still point to homepage sections until dedicated pages exist.

When /story/ is created, update Story navigation across all public pages.

When /resources/ or a GitHub/resources page is created, decide whether GitHub remains a homepage proof anchor or moves into Resources.

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
- GitHub proof section
- links to NeuroCore and Argus Lab GitHub repos
- navigation to Projects and Knowledge Base

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
- link to placeholder Argus ACLI and Argus Lab pages
- reinforce the platform / product / lab model

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

    Live

Current purpose:

    Story-first public NeuroCore explainer.

Current branding:

- TENSA header logo
- NeuroCore stacked logo in hero

Current content includes:

- story-first opening
- origin story
- context explanation
- continuity explanation
- Linux project origin
- local runtime path
- knowledge layer explanation
- RAG explanation
- daemon / persistent system explanation
- control plane explanation
- hallucination explanation
- controlled tool execution explanation
- observability explanation
- current Linux/Ubuntu focus
- Argus ACLI section
- Argus Lab section
- GitHub link

Important note:

The NeuroCore page should stay story-first.

Do not turn it into a dry architecture reference page.

Future architecture detail should move into Knowledge Base pages and Build Notes pages, then be linked from the NeuroCore page.

---

## Current Argus ACLI Page

Current path:

    projects/argus-acli.html

Current status:

    Branded placeholder

Current purpose:

- provide a clean public destination for Argus ACLI
- prevent dead links
- reserve page structure for future full Argus ACLI explanation
- keep current public navigation consistent

Current branding:

- TENSA header logo
- Argus ACLI stacked logo in hero

Future page should explain:

- what Argus ACLI is
- why read-only diagnostics matter
- how Argus uses NeuroCore
- system tools vs Argus tools
- structured telemetry
- findings
- severity
- recommendations
- raw evidence
- output controls
- current Linux/Ubuntu focus
- current V1 status
- future install/download guidance when ready

Do not write the full Argus ACLI page without source docs.

Before writing the full Argus ACLI page, check:

    docs/planning/content_source_map.md

---

## Current Argus Lab Page

Current path:

    projects/argus-lab.html

Current status:

    Branded placeholder

Current purpose:

- provide a clean public destination for Argus Lab
- reserve page structure for future full Argus Lab explanation
- keep current public navigation consistent

Current branding:

- TENSA header logo
- Argus Lab stacked logo in hero

Future page should explain:

- Argus Lab origin
- personal Linux troubleshooting practice goal
- real Linux failure scenarios
- controlled faults
- resettable sessions
- training role
- validation role
- mentor-style AI guidance
- adaptive difficulty
- future tracked troubleshooting sessions
- demonstrated proficiency direction

Do not write the full Argus Lab page without source docs.

Before writing the full Argus Lab page, check:

    docs/planning/content_source_map.md

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

- local-first AI platform
- persistent understanding
- memory direction
- controlled tool interaction
- real Linux system awareness
- governed execution
- operational continuity

Argus ACLI:

- first product / distribution built on NeuroCore
- read-only Linux diagnostics
- real telemetry
- structured findings
- severity classification
- recommendations
- raw evidence

Argus Lab:

- future real-Linux troubleshooting, training, and validation environment
- controlled failure scenarios
- resettable lab sessions
- mentor-style AI guidance
- validation environment for NeuroCore, Argus ACLI, and model-guided troubleshooting

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
- NeuroCore page rewritten as a story-first explainer
- Argus ACLI placeholder page created
- Argus Lab placeholder page created
- long-form article styling added
- project links updated so pages route internally
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
- Argus ACLI placeholder branding updated
- Argus Lab placeholder branding updated
- Knowledge Base index page created
- Knowledge Base navigation updated across current public pages
- page inventory planning doc created
- internal linking strategy planning doc created
- TENSA website documentation closeout protocol created

---

## Not Yet Completed

- full Argus ACLI page
- full Argus Lab page
- Story index page
- Resources page
- About page
- Build Notes section
- SEO strategy
- analytics/search indexing decisions
- content roadmap
- visual brand refinement beyond current static style
- migration plan from old Argus ACLI landing page
- install/download guidance for Argus ACLI
- article templates
- content style guide
- SEO topic map
- old-site migration plan
- documentation strategy doc for the TENSA website
- internal link checker script
- Knowledge Base category pages
- Knowledge Base article pages

---

## Core Anti-Drift Context Pack

Use these docs at the start of future serious website sessions:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md

Purpose of each:

    tensa_website_resume_prompt.md
        fresh-thread startup context

    documentation_closeout_protocol.md
        end-of-session documentation closeout workflow

    website_state.md
        live-current-state record

    website_information_architecture.md
        long-term structure and planning direction

    tensa_repository_map.txt
        real repository structure and file map

    content_source_map.md
        required source docs before writing factual pages

    page_inventory.md
        page existence, status, purpose, and next-action tracker

    internal_linking_strategy.md
        logical linking map, preferred destinations, temporary links, and link-audit expectations

---

## Build-Start Checks

At the beginning of serious website build sessions, run:

    git status --short
    tree -a -I '.git|.obsidian|node_modules|__pycache__'
    find . -maxdepth 3 -name "*.html" -print
    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html

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

## Next Recommended Steps

Recommended next session:

1. Run build-start checks.
2. Confirm repo is clean.
3. Review `docs/planning/page_inventory.md`.
4. Review `docs/planning/internal_linking_strategy.md`.
5. Decide whether to continue public site build or do documentation strategy planning.
6. Before writing factual pages, check `docs/planning/content_source_map.md`.

Recommended next planning move:

    Create a TENSA website documentation strategy doc.

Recommended next public-page options:

    projects/argus-acli.html
    projects/argus-lab.html
    story/index.html
    resources/index.html
    about.html

Recommended next Knowledge Base options:

    knowledge-base/controlled-ai-systems/
    knowledge-base/persistent-ai-memory/
    knowledge-base/ai-operations/
    knowledge-base/linux-diagnostics/

---

## Source Docs Used Recently

Recent NeuroCore page work used context from:

- NeuroCore Vision
- NeuroCore README
- System Architecture
- Control Plane Architecture
- Tool Execution Architecture
- Security & Policy Architecture
- Observability & Tracing
- NeuroCore Master Blueprint
- early build logs 000 through 006
- build log 009 daemon foundation
- build log 016 runtime control plane enforcement
- build log 017 execution layer and control integration
- build log 018 observability and tracing
- Argus Lab README / vision material

Recent site structure work used:

- TENSA website resume prompt
- TENSA website state
- TENSA website information architecture
- TENSA repository map
- TENSA content source map
- TENSA Website Session Additions – Tonight
- NeuroCore / Argus / Argus Lab deep context loading pack
- NeuroCore repository map

Important:

Old build logs still contain the former project name “Jarvis.”

Public website copy should use NeuroCore unless explicitly discussing historical renaming.

---

## Working Rules

Use full file replacements only.

Do not provide snippets unless explicitly requested.

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

Knowledge Base pages teach individual concepts.

Build Notes explain how the system evolved.

GitHub remains the source of truth.

The site should never grow faster than the documentation system that keeps it organized.
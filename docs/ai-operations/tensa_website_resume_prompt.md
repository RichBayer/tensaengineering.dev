# TENSA Engineering Website – Resume Prompt (Compressed)

We are continuing development of the TENSA Engineering website:

    https://tensaengineering.dev

Repository path:

    /mnt/g/ai/projects/tensaengineering.dev

Deployment:

    GitHub Pages

DNS / domain:

    Cloudflare

Current repository size:

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
- Use full file replacements only.
- Do NOT provide snippets unless explicitly requested.
- Do NOT make hidden changes.
- Do NOT invent public-facing claims.
- Do NOT write factual project pages without checking source requirements.
- Do NOT let the site grow faster than the documentation system that tracks it.
- Public website copy must not sound like internal planning notes.
- Keep the homepage as a front door, not a giant explanation page.

If something is unclear:

    STOP
    explain what is missing
    ask for the needed file, repo output, or source doc

---

# SESSION INITIALIZATION PROTOCOL

At the start of a serious website build session:

- Treat the session as having zero reliable prior context.
- Ask the user to upload or provide the core website context docs.
- Ingest uploaded documents silently.
- Do not analyze, summarize, or act during ingestion.
- Wait until the user explicitly says uploads are complete.

Only after context loading is complete should analysis begin.

---

# CORE CONTEXT DOCS

Request or load these docs at the start of serious website sessions:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/documentation_strategy.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/search_indexing_strategy.md
    docs/planning/content_style_guide.md
    docs/planning/seo_topic_map.md

Purpose:

    tensa_website_resume_prompt.md
        compressed startup protocol and current direction

    documentation_closeout_protocol.md
        documentation closeout workflow for serious website build sessions

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

    page_inventory.md
        page existence, status, purpose, navigation state, and next actions

    internal_linking_strategy.md
        logical link flow, preferred destinations, temporary links, and link-audit expectations

    search_indexing_strategy.md
        sitemap, robots.txt, Google Search Console, Bing Webmaster Tools, and indexing workflow

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
    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html

Purpose:

- confirm repository state
- confirm current tree
- confirm public page inventory
- confirm current links
- detect stale navigation targets
- prevent broken links and drift

Future recommended replacement for manual link grep:

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

Current internal planning / continuity docs:

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
    /projects/argus-lab.html    Branded placeholder with SEO-tuned troubleshooting training / diagnostic validation positioning
    /knowledge-base/            Structure-only Knowledge Base index

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
    https://tensaengineering.dev/projects/
    https://tensaengineering.dev/projects/neurocore.html
    https://tensaengineering.dev/projects/argus-acli.html
    https://tensaengineering.dev/projects/argus-lab.html
    https://tensaengineering.dev/knowledge-base/

Current SEO/social metadata:

- public HTML pages have canonical URLs
- public HTML pages have tuned meta descriptions
- public HTML pages use Open Graph metadata where currently implemented
- public HTML pages use Twitter large-image card metadata where currently implemented
- public HTML pages use the dedicated TENSA social preview image where currently implemented

Current social preview asset:

    assets/images/social/tensa-og-image.png

Current search registration status:

    Google Search Console verified
    sitemap submitted successfully to Google
    Bing Webmaster Tools imported from Google Search Console
    sitemap submitted to Bing and processing

Known Search Console status:

    Google reported "Page with redirect" for:
        http://tensaengineering.dev/
        https://www.tensaengineering.dev/

This is expected and harmless because those are alternate redirect versions. The intended canonical indexed version is:

    https://tensaengineering.dev/

Future SEO work:

- Add or verify richer Open Graph / Twitter / JSON-LD metadata on the updated NeuroCore page.
- Optionally add sitemap lastmod dates.
- Focus future search growth on Knowledge Base pages, not metadata alone.

---

# CURRENT STRATEGIC DIRECTION

TENSA Engineering is no longer just a static landing page.

It is becoming:

    a modular ecosystem knowledge platform

The website should increasingly function as:

- public umbrella for the ecosystem
- structured knowledge hub
- public teaching layer
- ecosystem portal
- future product funnel
- SEO destination
- public explanation layer for NeuroCore, Argus ACLI, and Argus Lab

The site should not become one huge homepage.

Correct structure:

    Homepage
        ecosystem introduction + navigation layer

    Project pages
        major system explanations

    Knowledge Base
        educational concept pages

    Story
        origin and philosophy

    Build Notes
        readable public development history

    Resources
        GitHub links, future downloads, videos, docs, and public resources

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

- first product / distribution built on NeuroCore
- local-first read-only Linux diagnostics
- real telemetry
- structured findings
- severity classification
- recommendations
- raw evidence
- AI explanation grounded in structured evidence
- no uncontrolled AI authority over the machine

Argus Lab:

- future real-Linux troubleshooting, training, and validation environment
- controlled failure scenarios
- resettable lab sessions
- mentor-style AI guidance
- validation environment for NeuroCore, Argus ACLI, and model-guided troubleshooting

GitHub:

- engineering proof
- implementation history
- source-of-truth documentation
- public credibility

Knowledge Base:

- public teaching layer for philosophy, architecture, AI operations, diagnostics, training systems, memory/context systems, and long-term platform vision

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
- Argus Lab placeholder hero uses the Argus Lab stacked logo
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

---

# CURRENT NAVIGATION STATE

Current primary navigation:

    Home
    Projects
    Knowledge Base
    Story
    GitHub

Current targets:

    Home → /index.html
    Projects → /projects/
    Knowledge Base → /knowledge-base/
    Story → /index.html#story
    GitHub → /index.html#proof or GitHub repo depending on page

Knowledge Base now points to the real `/knowledge-base/` page.

Story and GitHub are temporary homepage anchors until dedicated sections exist.

When `/story/` is created:

    update Story navigation across all public pages

When `/resources/` or GitHub/resources page is created:

    decide whether GitHub remains a homepage proof anchor or moves into Resources

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
- Argus Lab placeholder created
- Knowledge Base index created
- branding asset hierarchy created
- TENSA, NeuroCore, Argus ACLI, and Argus Lab logos added
- transparent logo variants created
- header-optimized TENSA logo created
- branding integrated across all current public pages
- Knowledge Base nav links updated across current pages
- repository map created and updated
- website state created and updated
- content source map created
- page inventory created
- internal linking strategy created
- documentation closeout protocol created
- documentation strategy created
- search indexing strategy created
- content style guide created
- SEO topic map created
- root sitemap.xml created
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

Recent completed website work:

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
    - View NeuroCore on GitHub
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

---

# CURRENT NOT COMPLETED

Not yet completed:

- full Argus Lab page
- Story index page
- Resources page
- About page
- Build Notes section
- Knowledge Base category pages
- Knowledge Base article pages
- old-site migration plan
- internal link checker script
- analytics decisions
- future install/download guidance for Argus ACLI
- deeper NeuroCore metadata / SEO pass after latest page expansion
- optional sitemap lastmod dates

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

Do not write full factual Argus ACLI, Argus Lab, NeuroCore, or Knowledge Base pages without the required source docs.

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

# FULL-FILE EDITING RULE

The user prefers full file replacements for accuracy.

Do not provide code snippets unless explicitly requested.

For HTML, CSS, Markdown docs, or planning files:

    provide the complete replacement file

If a change is tiny but affects an existing file:

    still provide the full file unless the user explicitly approves a command/script edit

For mechanical multi-file link corrections, command-based edits are acceptable only when the user approves the workflow.

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

Closeout docs usually include:

    docs/infrastructure/tensa_repository_map.txt
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md

Update only the docs actually impacted by the session.

---

# CURRENT NEXT BEST STEP

Recommended next website move:

    Build the full Argus Lab landing page.

Reason:

Argus Lab is still the remaining project placeholder page. It is already part of the public ecosystem flow and should become the next full project page after NeuroCore and Argus ACLI.

Argus Lab page should explain:

- real Linux troubleshooting practice
- controlled fault injection
- resettable lab environments
- mentor-style AI guidance
- training modes
- validation/tuning environment for Argus ACLI
- diagnostic regression testing
- relationship to NeuroCore and Argus ACLI

Do not build it without required source docs.

Likely source docs needed:

    docs/vision/argus_lab_vision.md
    docs/architecture/platform_ecosystem.md
    docs/planning/content_source_map.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    current projects/argus-lab.html
    current styles.css

Optional supporting docs:

    docs/architecture/neurocore_vision.md
    docs/distributions/argus/argus_distribution_and_deployment.md
    docs/architecture/system_architecture.md
    docs/ideas/platform/service_intelligence_layer.md or equivalent if Argus Lab validation scope is discussed

---

# NEXT PUBLIC BUILD OPTIONS

Possible next public work:

1. Build full Argus Lab page from source docs.
2. Create `/story/index.html`.
3. Create `/resources/index.html`.
4. Create `/about.html`.
5. Create first Knowledge Base category pages.
6. Add deeper SEO/metadata pass for updated NeuroCore page.
7. Add sitemap lastmod dates.
8. Create internal link checker script.

Recommended next full project page:

    /projects/argus-lab.html

Reason:

NeuroCore and Argus ACLI now have strong public pages. Argus Lab is the remaining major project page needed to complete the first coherent ecosystem story.

Do not build it without required source docs.

---

# FINAL PRINCIPLE

TENSA Engineering should become the public explanation layer for the ecosystem.

The repositories prove the work.

The social content tells the story and teaches the lessons.

The website organizes everything into a clear, trusted, expandable public hub.

Long-term goal:

    Teach the ideas.
    Explain the systems.
    Prove the work.
    Build trust.
    Convert attention into adoption.

Do not let the site grow faster than the documentation system that keeps it organized.
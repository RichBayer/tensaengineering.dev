# TENSA Engineering Website State

---

## Current Status

TENSA Engineering website foundation is live.

The site is transitioning from a small static site into a modular ecosystem knowledge platform.

Current phase:

    live public website foundation
    information architecture complete
    homepage refined
    Projects section created
    NeuroCore project page expanded into a stronger public platform page
    Argus ACLI project page upgraded into a full public product page
    Argus Lab full public project page created
    Story page created
    Glossary page created
    About page created
    Contact page created after email routing was configured and tested
    inline glossary tooltip system added for Knowledge Base articles
    branding asset hierarchy established
    consistent branding added across current public pages
    favicon assets added and wired across current public pages
    footer-only Contact navigation added across current public pages
    Knowledge Base index created and upgraded into a live article-path hub
    first eight Knowledge Base articles created
    focused AI Operations project-context article created
    focused AI Operations project-context article converted into the first prose-first Knowledge Base article standard / proof page
    Knowledge Base article template / creation guide created for future long-form articles
    Blog planning strategy created
    Blog reader-experience planning created
    Blog engagement / collaboration / attribution planning created
    structure-only Blog directory scaffold created
    structure-only Blog image asset scaffold created
    page inventory created and updated
    internal linking strategy created and updated
    repository map updated
    content source map created and updated
    content style guide created
    SEO topic map created
    search indexing strategy updated
    Claude website polish prompt created
    closeout verification workflow improved
    Python full-file writer rule added to closeout workflow
    local internal-link validation workflow added to closeout workflow
    public GitHub navigation removed from current public pages
    public repository-proof framing replaced with private-development / future-artifacts framing
    glossary strategy and search-answer optimization planning docs added
    Knowledge Base article reading-experience standard created on focused project-context guide

The site now functions as a modular ecosystem portal and teaching platform, not a single long page.

The homepage remains the front door.

Deeper explanations are moving into dedicated pages and Knowledge Base articles.

The Blog is planned and scaffolded internally, but it has not launched publicly.

---

## Current Closeout Snapshot

Latest completed planning branch:

    feature/blog-planning-foundation

Current Blog planning foundation state:

- `feature/blog-planning-foundation` contains Blog planning docs and structure-only scaffold directories
- local cleanup commit `2dfa282 Align blog strategy scaffold naming` is present on the branch
- local tree verified at 41 directories and 90 files
- current public HTML page count remains 19
- focused AI Operations project-context article remains the reference implementation for the prose-first Knowledge Base article standard
- Blog planning foundation updates are limited to internal planning / continuity docs and structure-only `.gitkeep` scaffold directories
- no public Blog pages, public article routes, sitemap entries, navigation links, RSS feed, newsletter signup, CSS changes, JavaScript changes, or public HTML files changed during the Blog planning foundation

Focused article:

    /knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html

Template / creation guide:

    docs/planning/knowledge_base_article_template.md

Blog planning docs:

    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md

Blog scaffold directories:

    blog/
    blog/ai-coding/
    blog/homelab/
    blog/tools-and-models/
    blog/local-ai/
    blog/build-lessons/
    blog/buying-guides/

Blog image scaffold directories:

    assets/images/blog/
    assets/images/blog/ai-coding/
    assets/images/blog/homelab/
    assets/images/blog/tools-and-models/
    assets/images/blog/local-ai/
    assets/images/blog/build-lessons/
    assets/images/blog/buying-guides/

Latest public-link validation from the reading-experience closeout:

    Public HTML files checked: 19
    Internal links checked: 579
    External/skipped links: 21
    Result: all checked internal links and anchors resolved successfully

Current boundary:

    The Blog planning foundation is internal documentation and structure-only scaffold work.
    Public Blog implementation should happen later on a separate reviewed branch.
    Deployment and indexing must not be claimed until live-site evidence confirms the relevant public pages and sitemap are deployed.

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
- about.html
- contact.html
- favicon.ico
- styles.css
- README.md
- CNAME
- robots.txt
- sitemap.xml
- assets/images/branding/tensa/
- assets/images/branding/tensa/favicon-32x32.png
- assets/images/branding/tensa/apple-touch-icon.png
- assets/images/branding/tensa/tensa-icon-512.png
- assets/images/branding/tensa/android-chrome-192x192.png
- assets/images/branding/tensa/android-chrome-512x512.png
- assets/images/branding/neurocore/
- assets/images/branding/argus-acli/
- assets/images/branding/argus-lab/
- assets/images/blog/
- assets/images/blog/ai-coding/
- assets/images/blog/homelab/
- assets/images/blog/tools-and-models/
- assets/images/blog/local-ai/
- assets/images/blog/build-lessons/
- assets/images/blog/buying-guides/
- assets/images/social/tensa-og-image.png
- assets/js/glossary-tooltips.js
- blog/
- blog/ai-coding/
- blog/homelab/
- blog/tools-and-models/
- blog/local-ai/
- blog/build-lessons/
- blog/buying-guides/
- projects/index.html
- projects/neurocore.html
- projects/argus-acli.html
- projects/argus-lab.html
- knowledge-base/index.html
- glossary/index.html
- knowledge-base/ai-operations/index.html
- knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html
- knowledge-base/persistent-ai-memory/index.html
- knowledge-base/controlled-ai-systems/index.html
- knowledge-base/local-first-ai/index.html
- knowledge-base/safe-tool-interaction/index.html
- knowledge-base/linux-diagnostics/index.html
- knowledge-base/troubleshooting-training/index.html
- knowledge-base/neurocore-architecture/index.html
- story/index.html
- docs/ai-operations/claude/claude_website_polish_resume_prompt.md
- docs/ai-operations/documentation_closeout_protocol.md
- docs/ai-operations/tensa_website_resume_prompt.md
- docs/infrastructure/tensa_repository_map.txt
- docs/planning/blog_strategy.md
- docs/planning/blog_reader_experience.md
- docs/planning/blog_engagement_strategy.md
- docs/planning/content_source_map.md
- docs/planning/content_style_guide.md
- docs/planning/documentation_strategy.md
- docs/planning/glossary_strategy.md
- docs/planning/internal_linking_strategy.md
- docs/planning/knowledge_base_article_template.md
- docs/planning/page_inventory.md
- docs/planning/search_answer_optimization_template.md
- docs/planning/search_indexing_strategy.md
- docs/planning/seo_topic_map.md
- docs/planning/website_information_architecture.md
- docs/website_state.md

Current repository size:

    41 directories, 90 files

Last verified by user-provided output during closeout:

    git status --short
    tree -a -I '.git|.obsidian|node_modules|__pycache__'
    find . -maxdepth 3 -name "*.html" -print
    grep -R "href=" -n index.html about.html projects/*.html knowledge-base/*.html knowledge-base/*/*.html glossary/*.html story/*.html
    temporary local Python internal-link validation

Latest local internal-link validation result:

    Public HTML files checked: 19
    Internal links checked: 579
    External/skipped links: 21
    Result: all checked internal links and anchors resolved successfully

---

## Current Connector Workflow

Repository connector access is now available for read-only source loading during website sessions.

Current default connector posture:

    read-only

Connector reads may be used to fetch current repository source files directly, reducing the need for manual upload bundles when the files are already committed and accessible through the connector.

Connector reads are appropriate for:

- current committed AI-operations docs
- current committed planning docs
- current committed website state files
- current committed public HTML/CSS/JS source files
- source-of-truth review before closeout

Connector reads do not replace local command output for:

- uncommitted working-tree changes
- `git status --short`
- local `tree` output
- browser preview
- internal-link validation results
- deployment checks

Even if write-capable connector tools are available in the future, the assistant must not create, update, delete, commit, or push repository content through connector tools unless Richard explicitly authorizes that specific write action in the current session.

Normal website workflow remains local-first:

    assistant reads and analyzes source docs
    assistant provides local commands or full-file replacement content
    Richard applies changes locally
    Richard reviews diffs
    Richard commits and pushes manually

Current additional workflow guardrails:

- Active repository boundary remains `RichBayer/tensaengineering.dev` unless Richard explicitly expands it.
- Connector access is read-only by default.
- Unknown source-of-truth documents must be loaded in full before being modified or summarized as current state.
- Local files, browser-preview observations, validation output, deployment evidence, and search-console evidence override connector-read committed state when those local or external facts matter.
- During workflow-only updates, do not change public page content, sitemap state, deployment state, indexing claims, branch closeout state, public page inventory, or next public build options unless Richard explicitly approves that website-state or public-content update.
- Use read-only local evidence or a context bundle before generating local editor scripts when local working-tree or validation state matters.

---

## Known Local Branch Repair Notes

Known local-only website repair state:

- Branch `content/knowledge-base-reading-experience` had uncommitted public-site reading-experience work before this AI-Ops guardrail update.
- That WIP was preserved locally in a Git stash named `WIP knowledge-base-reading-experience before ai-ops guardrail update`.
- The stash is local-only and will not be visible through the GitHub connector.
- A fresh AI session must ask for local Git evidence before trying to repair or continue that branch.
- Do not apply, pop, drop, or rewrite the stash until the branch repair scope is clear.

Before repairing that branch, inspect locally:

    git branch
    git stash list
    git checkout content/knowledge-base-reading-experience
    git status --short
    git stash show --stat "stash@{0}"

If the stash still exists and the branch is selected intentionally, review the stash contents before applying it:

    git stash show --stat "stash@{0}"
    git stash show --patch "stash@{0}"

Only apply or pop the stash after Richard approves the repair scope.

---

## Current Website Structure

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

Current internal planning / continuity docs:

    docs/ai-operations/claude/claude_website_polish_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md
    docs/planning/content_source_map.md
    docs/planning/content_style_guide.md
    docs/planning/documentation_strategy.md
    docs/planning/glossary_strategy.md
    docs/planning/internal_linking_strategy.md
    docs/planning/knowledge_base_article_template.md
    docs/planning/search_answer_optimization_template.md
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
    assets/images/blog/

Current TENSA branding assets:

    android-chrome-192x192.png
    android-chrome-512x512.png
    apple-touch-icon.png
    favicon-32x32.png
    tensa-horizontal-logo.png
    tensa-horizontal-logo-transparent.png
    tensa-horizontal-header-transparent.png
    tensa-icon-512.png
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

Current Blog image asset scaffold:

    assets/images/blog/
    assets/images/blog/ai-coding/
    assets/images/blog/homelab/
    assets/images/blog/tools-and-models/
    assets/images/blog/local-ai/
    assets/images/blog/build-lessons/
    assets/images/blog/buying-guides/

Current branding behavior:

- all current public pages use the TENSA header logo
- all current public pages include favicon link tags
- root favicon.ico provides browser favicon discovery
- homepage hero uses the TENSA stacked logo
- Projects page hero uses the TENSA stacked logo
- NeuroCore page hero uses the NeuroCore stacked logo
- Argus ACLI page hero uses the Argus ACLI stacked logo
- Argus Lab page hero uses the Argus Lab stacked logo
- Knowledge Base index hero uses the TENSA stacked logo
- Knowledge Base articles use TENSA site branding
- Story page hero uses the TENSA stacked logo
- Glossary page uses TENSA site branding
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
- reusable Knowledge Base article layout
- readable Knowledge Base index links with explicit styling
- glossary reference page layout
- inline glossary tooltip styling
- footer navigation styling
- simplified TENSA T-symbol favicon for small browser-tab readability
- reusable Knowledge Base diagram styling
- Knowledge Base FAQ styling
- Knowledge Base article metadata styling

---

## Current Navigation State

Current primary navigation:

    Home
    Projects
    Knowledge Base
    Glossary
    Story
    About

Current navigation targets:

    Home → /index.html
    Projects → /projects/
    Knowledge Base → /knowledge-base/
    Glossary → /glossary/
    Story → /story/
    About → /about.html

Current footer navigation targets:

    Contact → /contact.html
    About → /about.html
    Projects → /projects/
    Knowledge Base → /knowledge-base/
    Glossary → /glossary/

Important notes:

    Knowledge Base points to the real /knowledge-base/ page.
    Glossary points to the real /glossary/ page.
    Story points to the real /story/ page.
    About points to the standalone /about.html page.
    Contact is footer-only and intentionally not part of the primary header navigation.
    Public GitHub navigation has been removed from current public pages.
    Direct public links to private implementation repositories have been removed from current public pages.
    Knowledge Base index links to all eight foundation Knowledge Base articles.
    The foundation path links article-to-article and loops back to the start.
    AI Operations links to the focused project-context guide.
    Inline glossary terms in Knowledge Base articles point to /glossary/ entries.
    Blog does not appear in current public navigation.

Current public artifact strategy:

    TENSA Engineering is the umbrella engineering company and public home for the ecosystem.
    Active implementation repositories are private during current development and product maturation.
    Public technical artifacts may be added later when they are useful for users, builders, releases, examples, documentation, or selected open components.
    A Resources page remains deferred until there is enough public material to organize.
    A public Blog remains deferred until real Blog pages and proof content are created on a future public Blog implementation branch.

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
- https://tensaengineering.dev/about.html
- https://tensaengineering.dev/contact.html
- https://tensaengineering.dev/projects/
- https://tensaengineering.dev/projects/neurocore.html
- https://tensaengineering.dev/projects/argus-acli.html
- https://tensaengineering.dev/projects/argus-lab.html
- https://tensaengineering.dev/knowledge-base/
- https://tensaengineering.dev/glossary/
- https://tensaengineering.dev/knowledge-base/ai-operations/
- https://tensaengineering.dev/knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html
- https://tensaengineering.dev/knowledge-base/persistent-ai-memory/
- https://tensaengineering.dev/knowledge-base/controlled-ai-systems/
- https://tensaengineering.dev/knowledge-base/local-first-ai/
- https://tensaengineering.dev/knowledge-base/safe-tool-interaction/
- https://tensaengineering.dev/knowledge-base/linux-diagnostics/
- https://tensaengineering.dev/knowledge-base/troubleshooting-training/
- https://tensaengineering.dev/knowledge-base/neurocore-architecture/
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
    /story/ included in sitemap.xml
    /glossary/ included in sitemap.xml locally
    /contact.html included in sitemap.xml locally
    eight foundation Knowledge Base article URLs included in sitemap.xml locally
    focused project-context guide URL included in sitemap.xml locally
    current local sitemap contains 19 canonical URLs
    no Blog URLs are currently included in sitemap.xml

Known Search Console note:

    Google reported "Page with redirect" for alternate redirect versions:
        http://tensaengineering.dev/
        https://www.tensaengineering.dev/

This is expected and harmless because the intended canonical indexed URL is:

    https://tensaengineering.dev/

Future SEO work:

- After deployment, confirm the live sitemap includes `/contact.html`, all eight foundation Knowledge Base article URLs, and the focused project-context guide URL.
- Inspect the Knowledge Base index and important article URLs in Google Search Console if appropriate.
- Run a dedicated SEO/topic-map session for the first Knowledge Base article path.
- Add or verify richer Open Graph / Twitter / JSON-LD metadata on updated pages as needed.
- Keep sitemap.xml URL-only unless a reliable lastmod maintenance process is added later.
- Focus future search growth on useful Knowledge Base content and clean internal links, not metadata alone.
- Do not add Blog URLs to sitemap.xml until real public Blog HTML pages exist and are ready to be indexed.

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
- ecosystem public-home closing section
- private-development / future-public-artifacts framing
- navigation to Projects, Knowledge Base, Glossary, and Story
- footer navigation to Contact, About, Projects, Knowledge Base, and Glossary

The homepage treats TENSA Engineering as the single public hub for the ecosystem.

The homepage should remain concise.

It should stay a front door and navigation layer, not become a giant explanation page.

---

## Current About Page

Current path:

    about.html

Current status:

    Live

Current purpose:

- explain TENSA Engineering as the umbrella engineering company and public home for the ecosystem
- provide concise organizational identity
- support the public site without turning the homepage into a long About section
- route readers toward Projects, Knowledge Base, Glossary, and Story

Important note:

The About page should stay concise and professional.

The deeper origin story belongs in the Story section.

---

## Current Contact Page

Current path:

    contact.html

Current status:

    Live

Current purpose:

- provide a simple public contact route for TENSA Engineering
- support appropriate questions, website issues, and ecosystem inquiries
- keep contact expectations clear without implying paid support, public product support SLAs, public downloads, or a public issue tracker
- provide both a mailto link and visible email address

Current public contact address:

    contact@tensaengineering.dev

Current routing status:

    Cloudflare Email Routing was configured and tested before publishing the page.

Current navigation:

    Footer-only link across current public pages.

Important note:

The Contact page should stay simple.

It should not become a support portal, sales page, or public issue tracker unless those systems exist.

Contact should remain out of the primary header navigation unless the site strategy changes.

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
- explain the public website / private implementation repository boundary

Current project model:

    NeuroCore = platform
    Argus ACLI = first product / distribution
    Argus Lab = active early real-Linux troubleshooting, training, and validation environment

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
- privacy and local-first design framing
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
- controlled system awareness value proposition
- Argus ACLI as first product built on NeuroCore
- Argus Lab as early training and validation environment
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

- explain Argus ACLI as the first practical product built on NeuroCore
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

    Live full public project page

Current purpose:

- explain Argus Lab as an early real-Linux troubleshooting, training, and validation environment
- explain its origin as a personal Linux troubleshooting practice and portfolio project
- explain controlled failure scenarios and resettable lab sessions
- explain mentor-style AI guidance without implying the model gives away answers
- explain the validation role for NeuroCore, Argus ACLI, and model-guided troubleshooting
- keep current implementation status clear and honest
- route readers to Argus ACLI, NeuroCore, and the Projects page
- route to the Story page through primary navigation

Current branding:

- TENSA header logo
- Argus Lab stacked logo in hero

Current content includes:

- active early real-Linux troubleshooting, training, and validation positioning
- real troubleshooting skill through experience, not memorization
- real systems, controlled failures, and guided growth principles
- support-ticket-style troubleshooting scenarios
- safe repeatable training loop
- NeuroCore, Argus ACLI, and model guidance relationship
- independent, assisted, and guided resolution modes
- validation and regression-testing role
- planned small-business-style Linux environment shape
- early implementation status / not publicly available
- learner, diagnostics, and growth audiences
- clear explanation of what Argus Lab is not

Important note:

Argus Lab should remain clearly described as active early implementation until availability changes.

Argus Lab detailed scenario milestones remain tracked in the Argus Lab repository, not repeated in TENSA website copy.

Do not imply it is publicly available, downloadable, or a finished training product.

---

## Current Knowledge Base

Current index path:

    knowledge-base/index.html

Current index status:

    Live public article-path hub

Current purpose:

- establish the Knowledge Base as a top-level public site section
- move TENSA away from pure landing-page structure
- introduce major educational topic areas
- route readers through the first recommended eight-article path
- route to the Story page through primary navigation
- frame future public artifacts without implying public implementation repositories are currently available

Current branding:

- TENSA header logo
- TENSA stacked logo in hero

Current article path:

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

Current focused article:

    How to Keep AI From Losing Project Context
    /knowledge-base/ai-operations/how-to-keep-ai-from-losing-project-context.html

Current article-format standard:

    The focused project-context article is the current proof page for the prose-first Knowledge Base article format.
    The canonical internal template / creation guide is `docs/planning/knowledge_base_article_template.md`.
    The standard favors fuller paragraphs, natural section flow, fewer bullets, fewer numbered lists, and a small number of useful styled diagrams.
    Diagrams should look like explanatory article graphics, not terminal output, code blocks, file trees, or internal planning artifacts unless the subject actually requires code or file examples.

Current article-path behavior:

    Knowledge Base index links to all eight foundation articles.
    AI Operations links to the focused project-context guide.
    Articles link forward through the recommended reading path.
    NeuroCore Architecture links back to AI Operations to restart the path.
    Related links point only to real public pages.
    Inline glossary links provide compact definitions where helpful.
    Article pages preserve current-vs-future language where needed.

Planned AI Operations category direction:

    /knowledge-base/ai-operations/ should become a true AI Operations category / article index page in a future branch.
    The current long-form AI Operations landing-page content should move into a dedicated article, likely /knowledge-base/ai-operations/what-is-ai-operations.html or another approved article slug.
    The project-context article should remain a focused article under the AI Operations category.

Important note:

The Knowledge Base is public-facing.

It should not read like an internal writing guide.

Future articles should be created deliberately and tracked in:

    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/content_source_map.md

Future long-form Knowledge Base articles should use:

    docs/planning/knowledge_base_article_template.md

---

## Current Blog Planning

Current status:

    Planned / scaffold only

Current purpose:

- plan future timely, practical Blog content
- define Blog categories before public pages are created
- distinguish Blog posts from Knowledge Base articles
- define reader experience expectations for future posts
- define contact, reader-question, collaboration, attribution, outbound-link, affiliate, and sponsored-link boundaries
- reserve future route and image-asset structure without launching public pages

Current internal planning docs:

    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md

Current structure-only directories:

    blog/
    blog/ai-coding/
    blog/homelab/
    blog/tools-and-models/
    blog/local-ai/
    blog/build-lessons/
    blog/buying-guides/

Current structure-only image asset directories:

    assets/images/blog/
    assets/images/blog/ai-coding/
    assets/images/blog/homelab/
    assets/images/blog/tools-and-models/
    assets/images/blog/local-ai/
    assets/images/blog/build-lessons/
    assets/images/blog/buying-guides/

Future planned categories:

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

Future public Blog implementation should happen on a separate branch after loading:

    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md
    docs/planning/content_source_map.md
    docs/planning/content_style_guide.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/website_state.md

Recommended future branch:

    feature/blog-public-foundation

Recommended first proof post:

    /blog/ai-coding/why-ai-code-breaks-after-it-works-once.html

Recommended second proof post:

    /blog/homelab/what-is-a-homelab-actually-for.html

---

## Current Glossary Page

Current path:

    glossary/index.html

Current status:

    Live public glossary page

Current purpose:

- define important TENSA ecosystem terms in plain English
- support readers without bloating every project or Knowledge Base page
- provide compact reference definitions for recurring terminology
- serve as the destination for inline glossary tooltip links from Knowledge Base articles
- help explain NeuroCore, Argus ACLI, Argus Lab, AI Operations, Linux diagnostics, evidence, memory, continuity, control-plane, and tool-boundary terms

Current focused-article glossary addition:

    MCP-based tool definition added

Current implementation support:

    assets/js/glossary-tooltips.js
    docs/planning/glossary_strategy.md

Important note:

The Glossary should stay compact and useful.

Do not turn it into a full Knowledge Base replacement.

Longer explanations should stay in Knowledge Base articles or project pages.

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
- Argus ACLI as the first practical product
- Argus Lab as the active early real-Linux troubleshooting, training, and validation environment
- AI Operations as the disciplined way of working that made the system possible

Important note:

The Story page should remain human, grounded, and readable.

Do not turn it into:

- a technical architecture manual
- a Knowledge Base article
- a roadmap dump
- an internal planning document
- a hype-heavy marketing page

Deeper technical definitions belong in the Knowledge Base or Glossary, depending on whether the reader needs a full article or a compact reference definition.

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
- public home for NeuroCore, Argus ACLI, and Argus Lab
- educational resource for controlled AI systems
- educational resource for persistent AI memory
- educational resource for local-first AI
- educational resource for safe tool interaction
- educational resource for AI operations
- educational resource for Linux diagnostics and troubleshooting training
- future Blog for timely practical builder lessons, AI coding workflow, homelab planning, tool/model explanations, local AI notes, build lessons, and carefully governed buying-guide content
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
- ecosystem public home
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

- first product built on NeuroCore
- local-first read-only Linux diagnostics
- real telemetry
- structured findings
- severity classification
- recommendations
- raw evidence
- AI explanation grounded in structured evidence

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

Public technical artifacts:

- future release materials
- future examples
- future downloads
- future selected documentation
- future open technical components if appropriate
- future credibility layer when the public materials are ready

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
- Argus Lab full public project page created
- Story page created
- long-form article styling added
- Knowledge Base article layout styling added
- Knowledge Base index link styling corrected
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
- Argus Lab full public project page created and branded
- Story page branded
- Knowledge Base index page created
- Knowledge Base index upgraded into a live article-path hub
- first eight Knowledge Base articles created
- Knowledge Base navigation updated across current public pages
- Knowledge Base article path linked article-to-article
- local internal-link validation completed successfully for 210 internal links
- page inventory planning doc created
- internal linking strategy planning doc created
- TENSA website documentation closeout protocol created
- TENSA website documentation strategy created
- TENSA search indexing strategy created
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
- public GitHub navigation removed from current public pages
- direct public links to private implementation repositories removed from current public pages
- homepage repository-proof section replaced with public explanation / future public artifacts framing
- Knowledge Base repository-proof language replaced with public artifacts language
- NeuroCore business-safety wording softened into controlled system awareness and local-first design language
- Argus ACLI and Story wording standardized around Argus ACLI as the first practical product built on NeuroCore
- Glossary page created
- Glossary page added to primary navigation
- inline glossary tooltip JavaScript added
- glossary reference styling added
- inline glossary tooltip styling added
- Knowledge Base articles received inline glossary tooltip links
- sitemap.xml updated to include `/glossary/`
- local internal-link validation completed successfully for 346 internal links across 16 public HTML files
- About page created and added to sitemap.xml
- local internal-link validation completed successfully for 403 internal links/assets across 17 public HTML files
- glossary strategy planning doc created
- search-answer optimization template planning doc created
- Cloudflare Email Routing configured and tested for contact@tensaengineering.dev
- Contact page created
- Contact page added to sitemap.xml
- Contact page linked footer-only across current public pages
- simplified TENSA T-symbol favicon assets created and wired across current public pages
- root favicon.ico added
- footer navigation styling added
- repository map updated to 27 directories and 73 files
- local internal-link validation completed successfully for 546 internal links across 18 public HTML files
- focused AI Operations article created
- AI Operations discovery links added
- MCP-based tool glossary definition added
- sitemap.xml expanded to 19 canonical URLs
- closeout docs updated for the new article
- local validation passed for 579 internal links across 19 public HTML files
- focused AI Operations project-context article converted into the first prose-first Knowledge Base article standard / proof page
- `docs/planning/knowledge_base_article_template.md` created as the canonical long-form Knowledge Base article template / creation guide
- list-heavy project-context article structure replaced with fuller article prose
- raw/code-style diagrams reduced to three styled explanatory article diagrams
- article metadata changed from pill-style tags to a plain reader-context sentence
- reusable Knowledge Base article diagram, FAQ, and metadata styling added to styles.css
- local validation passed for 579 internal links across 19 public HTML files after the reading-experience pass
- local tree verified at 27 directories and 73 files after adding the Knowledge Base article template doc
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

---

## Not Yet Completed

- merge of the Blog planning foundation branch into `main`
- GitHub Pages live deployment verification after the KB reading-experience merge and docs-only template closeout
- live verification of the focused project-context article
- live verification that the AI Operations page still links to the focused article
- live verification that sitemap.xml still contains 19 canonical URLs
- Google Search Console indexing data review after processing
- Bing Webmaster Tools indexing data review after processing
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
- deeper NeuroCore metadata / SEO pass after latest page expansion
- dedicated SEO/topic-map session for the first Knowledge Base article path
- public technical artifact strategy
- public repository / open-component strategy

---

## Core Anti-Drift Context Pack

Use these docs at the start of future serious website sessions:

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
    docs/planning/knowledge_base_article_template.md
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

    blog_strategy.md
        future Blog strategy, categories, reader groups, first-post candidates, and public implementation boundaries

    blog_reader_experience.md
        future Blog article layout, reader features, quick-answer boxes, metadata, CTAs, RSS/newsletter planning, and launch boundaries

    blog_engagement_strategy.md
        future Blog contact CTA, reader-question workflow, guest posts, collaboration, attribution, outbound-link, and affiliate/sponsored-link boundaries

    content_source_map.md
        required source docs before writing factual pages

    content_style_guide.md
        public writing voice, tone, formatting, and page-copy standards

    documentation_strategy.md
        documentation ownership, update triggers, and overlap boundaries

    glossary_strategy.md
        glossary purpose, term-selection rules, tooltip behavior, and expansion guardrails

    knowledge_base_article_template.md
        reusable Knowledge Base article structure, pacing, diagram, FAQ, metadata, source-doc, and internal-link guidance

    page_inventory.md
        page existence, status, purpose, and next-action tracker

    internal_linking_strategy.md
        logical linking map, preferred destinations, temporary links, and link-audit expectations

    search_indexing_strategy.md
        sitemap, robots.txt, search engine registration, indexing workflow, and local link validation expectations

    search_answer_optimization_template.md
        future search-and-answer optimization workflow for page clarity and search-answer usefulness

    seo_topic_map.md
        future SEO topic planning and Knowledge Base search strategy

---

## Build-Start Checks

At the beginning of serious website build sessions, run:

    git status --short
    tree -a -I '.git|.obsidian|node_modules|__pycache__'
    find . -maxdepth 3 -name "*.html" -print
    grep -R "href=" -n index.html about.html projects/*.html knowledge-base/*.html knowledge-base/*/*.html glossary/*.html story/*.html

When public links, navigation, or routes matter, prefer real local internal-link validation over grep-only review.

Future recommended permanent script:

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
    grep -n "41 directories, 90 files\|blog_strategy.md\|blog_reader_experience.md\|blog_engagement_strategy.md\|assets/images/blog" docs/infrastructure/tensa_repository_map.txt
    grep -n "https://tensaengineering.dev/knowledge-base/neurocore-architecture/" sitemap.xml

This rule exists to catch:

- paste mistakes
- missed saves
- wrong-file edits
- stale snippets
- unintended partial replacements
- accidental edits to the wrong file

---

## Python Full-File Writer Rule

Python-based file writing is allowed and often preferred for closeout documentation delivery, but only under the right conditions.

Use Python as a delivery mechanism when:

- the current full file context has been loaded or otherwise verified
- the complete intended replacement has been decided
- the assistant is writing the whole file, not guessing at a hidden section
- the command is easier and safer than manual copy/paste
- the replacement can be verified immediately afterward

Do not use Python as a shortcut to:

- inspect only partial file context
- make blind surgical patches from incomplete information
- guess what a hidden section probably says
- rewrite unrelated content without approval
- bypass the user's review expectations

Preferred safe pattern:

    full context first
    define intended changes
    write the complete file
    run targeted verification
    wait for user output

---

## Next Recommended Steps

Immediate branch review:

1. Review the Blog planning foundation diffs.
2. Confirm only Blog planning / scaffold documentation changed.
3. Confirm no public HTML, sitemap, robots, navigation, CSS, or JavaScript files changed.
4. Merge `feature/blog-planning-foundation` only after review.
5. After merge, keep public Blog implementation on a separate future branch.

Next Blog build option:

    Start a future `feature/blog-public-foundation` branch.
    Load the three Blog planning docs plus source map, style guide, page inventory, internal linking strategy, and website state.
    Create only the Blog index, one category index, and one proof post first.
    Do not add Blog routes to sitemap.xml or public navigation until real public Blog HTML pages exist and are ready to be indexed.

Recommended first proof post:

    /blog/ai-coding/why-ai-code-breaks-after-it-works-once.html

Recommended second proof post:

    /blog/homelab/what-is-a-homelab-actually-for.html

Separate non-Blog website work:

    Start a fresh branch for the AI Operations category / article index conversion.
    Convert /knowledge-base/ai-operations/ into a true category / article index page.
    Move the current long-form AI Operations landing-page content into a dedicated article page.
    Keep the project-context article as a focused article under that category.
    Use docs/planning/knowledge_base_article_template.md when creating or rewriting future long-form Knowledge Base articles.

---

## Source Docs Used Recently

Recent Blog planning work used context from:

- docs/planning/blog_strategy.md
- docs/planning/blog_reader_experience.md
- docs/planning/blog_engagement_strategy.md
- docs/planning/documentation_strategy.md
- docs/planning/page_inventory.md
- docs/planning/content_source_map.md
- docs/planning/website_information_architecture.md
- docs/infrastructure/tensa_repository_map.txt
- docs/website_state.md
- docs/ai-operations/documentation_closeout_protocol.md
- local branch status, tree output, public HTML count, and diff verification output

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

Recent Knowledge Base article path work used context from:

- AI Operations article draft and Claude-polished copy
- Persistent AI Memory article draft and Claude-polished copy
- Controlled AI Systems article draft and rewritten report-style version
- Local-First AI article draft and Claude-polished copy
- Safe Tool Interaction article draft and Claude-polished copy
- Linux Diagnostics article draft and Claude-polished copy
- Troubleshooting Training article draft and Claude-polished copy
- NeuroCore Architecture article draft and Claude-polished copy
- current public project pages
- current Knowledge Base index
- current `styles.css`
- content style guide
- page inventory
- internal linking strategy
- content source map
- search indexing strategy
- documentation closeout protocol

Recent Knowledge Base article-template work used context from:

- focused AI Operations project-context article reference implementation
- Knowledge Base article reading-experience standard
- content style guide
- page inventory
- internal linking strategy
- content source map
- documentation closeout protocol

Recent Glossary and inline tooltip work used context from:

- current public project pages
- current Knowledge Base articles
- glossary strategy planning
- internal linking strategy
- page inventory
- content source map
- search indexing strategy
- repository map
- current `styles.css`
- local browser review
- local internal-link validation

Recent GitHub/private-repository public-page cleanup used context from:

- current public HTML pages
- Claude public-page review packet
- ChatGPT factual alignment review
- current website strategy discussion
- user decision to keep implementation repositories private during active development
- user decision to defer Resources page until useful public artifacts exist

Important:

Old build logs may contain former project names.

Public website copy should use NeuroCore unless explicitly discussing historical renaming.

---

## Working Rules

Use full file replacements only unless explicitly requested otherwise.

Do not provide snippets unless explicitly requested.

Python full-file writers are allowed when full context is loaded and the complete intended replacement is known.

Do not use Python to blindly patch unknown sections from partial context.

After each full-file replacement, run a targeted verification check before moving to the next file.

When public links, navigation, or routes changed, run real local internal-link validation when practical.

Do not make hidden changes.

No changes the user does not know about.

Before replacing a file, inspect or request the current full file contents unless it was generated in the same session and not changed afterward.

Do not guess.

Connector reads may load committed repo files, but they do not replace local working-tree output when uncommitted changes exist.

If more context is needed, ask for the exact file or doc.

Use source docs before writing factual project pages.

Check the content source map before writing or significantly rewriting factual project pages:

    docs/planning/content_source_map.md

Check page inventory before creating or changing public pages:

    docs/planning/page_inventory.md

Check the Knowledge Base article template before creating or rewriting long-form Knowledge Base articles:

    docs/planning/knowledge_base_article_template.md

Check Blog planning docs before creating or rewriting public Blog pages or posts:

    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md

Check internal linking strategy before adding or changing major links:

    docs/planning/internal_linking_strategy.md

Keep the information architecture top-down and coherent.

Avoid turning every page into an encyclopedia.

TENSA site should organize the ecosystem and teach the public.

Private implementation repositories and internal source docs preserve the engineering source of truth during active development.

Public technical artifacts should be added later only when they are useful and intentional.

Argus ACLI page explains the product.

Argus Lab page explains training and validation.

Story explains origin and philosophy.

Knowledge Base teaches the philosophy, architecture, and methods.

Blog should eventually answer timely practical questions and route readers toward deeper Knowledge Base or Project pages when useful.

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

Keep public pages honest about what exists now, what is being built, what is publicly available, and what remains future-phase.

---

## Guiding Rule

Do not expand the website randomly.

Plan the information architecture first, then build the site structure around that plan.

Build one page at a time.

The homepage is the front door.

Project pages explain the major systems.

Story pages explain origin and philosophy.

Knowledge Base pages teach individual concepts.

Blog pages should answer timely practical questions and point readers toward deeper source-grounded pages when useful.

Build Notes explain how the system evolved.

Private implementation repositories and internal documentation preserve the engineering source of truth during active development.

TENSA Engineering is the umbrella engineering company and public home for the ecosystem.

Public technical artifacts can be added later when they are ready and useful.

The site should never grow faster than the documentation system that keeps it organized.
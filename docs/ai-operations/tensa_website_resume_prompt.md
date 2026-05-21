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

    17 directories, 51 files

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
- After each full-file replacement, run a targeted verification check before moving to the next file.
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
    docs/ai-operations/claude/claude_website_polish_resume_prompt.md
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
    grep -R "href=" -n index.html projects/*.html knowledge-base/*.html story/*.html

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
    /projects/argus-lab.html    Live full Argus Lab public landing page
    /knowledge-base/            Structure-only Knowledge Base index
    /story/                     Live full public Story page

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
    https://tensaengineering.dev/story/

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
    /story/ added to sitemap locally during Story page closeout

Known Search Console status:

    Google reported "Page with redirect" for:
        http://tensaengineering.dev/
        https://www.tensaengineering.dev/

This is expected and harmless because those are alternate redirect versions. The intended canonical indexed version is:

    https://tensaengineering.dev/

Post-deploy search checks after the Story page closeout:

- Confirm the live Story page loads:

      https://tensaengineering.dev/story/

- Confirm the live sitemap includes:

      https://tensaengineering.dev/story/

- Inspect the Story URL in Google Search Console if appropriate.

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

    Story
        origin and philosophy

    Knowledge Base
        educational concept pages

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

GitHub:

- engineering proof
- implementation history
- source-of-truth documentation
- public credibility

Knowledge Base:

- public teaching layer for philosophy, architecture, AI operations, diagnostics, training systems, memory/context systems, and long-term platform vision

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
- Story page hero uses the TENSA stacked logo
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
    Story → /story/
    GitHub → /index.html#proof or GitHub repo depending on page

Knowledge Base now points to the real `/knowledge-base/` page.

Story now points to the real `/story/` page.

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
- Argus Lab full public landing page created
- Knowledge Base index created
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
- root sitemap.xml created
- `/story/` added to sitemap.xml
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

- `story/index.html` created as a full public Story page.
- Story page explains:
    - the day the AI forgot everything
    - AI memory failure as a project continuity problem
    - documentation becoming project memory
    - workflow discipline beginning to mirror architecture discipline
    - local AI changing the direction
    - real systems requiring control
    - NeuroCore as the platform
    - Argus ACLI as the first practical proof
    - Argus Lab as the future training and validation environment
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
- live sitemap confirmation after Story deployment
- Google Search Console inspection of Story URL after deployment if appropriate

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

# FULL-FILE EDITING RULE

The user prefers full file replacements for accuracy.

Do not provide code snippets unless explicitly requested.

For HTML, CSS, Markdown docs, or planning files:

    provide the complete replacement file

If a change is tiny but affects an existing file:

    still provide the full file unless the user explicitly approves a command/script edit

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
    grep -n "17 directories, 51 files\|story/index.html" docs/infrastructure/tensa_repository_map.txt
    grep -n "https://tensaengineering.dev/story/" sitemap.xml

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

Recommended next website move:

    Complete this closeout, commit, push, and verify the live Story page and sitemap after deployment.

After deployment, confirm:

    https://tensaengineering.dev/story/
    https://tensaengineering.dev/sitemap.xml
    https://tensaengineering.dev/robots.txt

Recommended next public-page options after this closeout:

    /resources/index.html
    /about.html
    first Knowledge Base category pages
    /build-notes/index.html

Reason:

NeuroCore, Argus ACLI, Argus Lab, Knowledge Base, and Story now all have public site structure. The next major website step should either organize public resources, add concise organizational identity, or begin focused teaching articles.

Likely next direction:

- create Resources if organizing GitHub, future videos, downloads, and public links is the priority
- create About if a concise TENSA mission/builder page is needed
- create Knowledge Base categories if the teaching layer becomes the next focus
- create Build Notes if public development history becomes the next content lane

---

# NEXT PUBLIC BUILD OPTIONS

Possible next public work:

1. Create `/resources/index.html`.
2. Create `/about.html`.
3. Create first Knowledge Base category pages.
4. Create `/build-notes/index.html`.
5. Add deeper SEO/metadata pass for updated NeuroCore page.
6. Add sitemap lastmod dates.
7. Create internal link checker script.

Recommended next direction:

    Expand the site structure around the completed project pages and completed Story page.

Reason:

The core project pages now exist for NeuroCore, Argus ACLI, and Argus Lab, and the Story page now preserves the origin/philosophy layer. Future work should add supporting public sections, teaching pages, resource organization, and public development history.

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
# TENSA Engineering Website Documentation Strategy

---

## Purpose

This document defines the long-term documentation strategy for the TENSA Engineering website repository.

TENSA Engineering is growing from a small static website into a modular public ecosystem hub, knowledge platform, product funnel, and public home for NeuroCore, Argus ACLI, and Argus Lab.

As the site grows, its internal documentation must stay organized enough to prevent:

- stale planning docs
- overlapping responsibilities
- outdated page inventories
- broken internal links
- source-doc confusion
- public pages expanding without factual grounding
- strategy documents turning into state documents
- state documents turning into planning documents
- AI-assisted build sessions drifting from the real repository
- AI polish workflows changing tone or facts without review
- copy/paste replacement mistakes going undetected
- reusable Knowledge Base article standards drifting between pages

The goal of this document is to define what each internal documentation file is responsible for, when it should be updated, and how the documentation system should scale as the public site grows.

This is an internal planning document.

It is not a public website page.

---

## Core Principle

Documentation exists to keep the website honest, organized, and scalable.

The public website explains the ecosystem.

The repositories prove the engineering.

The internal TENSA website docs keep the public site aligned with real project state, real source documents, real page inventory, real navigation, reusable content standards, and real workflow rules.

If the documentation system becomes confusing, stale, or overlapping, the website will eventually drift.

The documentation system should grow deliberately, not randomly.

---

## Documentation Responsibility Model

---

## Connector Access Documentation Rule

Repository connector access may be used as the first-pass read-only source-loading mechanism for website build sessions when the needed files are committed and accessible through the connector.

The goal is to reduce manual upload friction without weakening source-of-truth discipline.

This affects documentation workflow ownership as follows:

- `tensa_website_resume_prompt.md` owns the startup rule that connector reads should be attempted first for committed core context docs when connector access is available.
- `documentation_closeout_protocol.md` owns the closeout rule that connector reads are allowed, but connector writes are disabled by default.
- `website_state.md` summarizes the current connector workflow for future sessions.
- `documentation_strategy.md` owns the distinction between connector-readable committed files and local working-tree truth.
- Local repository output remains required for uncommitted changes, git status, tree verification, browser review, and link validation.

Default connector posture:

    read-only

If write-capable connector tools become available later, the documentation system must treat those capabilities as disabled-by-policy unless Richard explicitly authorizes a specific write action in the current session.

The normal repository-editing workflow remains local-first:

    assistant reads and analyzes source docs
    assistant provides local commands or replacement content
    Richard applies changes locally
    Richard reviews diffs
    Richard commits and pushes manually

Do not update this documentation model to assume connector write authority unless Richard deliberately changes that operating rule.

Large-file connector write boundary:

- connector full-file replacement must not be used for files over 1,000 lines
- files over 1,000 lines should use connector reads for committed context and verification, with surgical edits performed locally
- do not rebuild large files from connector chunks to bypass the full-file replacement limitation
- files at or under 1,000 lines may use connector replacement only after full current context is reviewed and the specific write is authorized

---

## Hybrid Source Loading Rule

Future serious website sessions should use a hybrid source-loading model:

1. Use connector reads for committed repository files when available.
2. Ask Richard for local command output for current working-tree state.
3. Ask Richard for full local file contents when a file may have uncommitted changes that differ from the connector version.
4. Avoid giant all-doc upload bundles unless the connector is unavailable or many local-only changes must be reviewed together.
5. Prefer targeted single-file full-context requests when editing closeout or planning docs.

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

This rule exists to avoid regressing back to manual-upload overhead while also avoiding stale connector reads or grep-marker patching.

Each documentation file should have one primary responsibility.

A document may reference related areas, but it should not duplicate entire sections from other docs unless a compressed summary is required for restart context.

The internal documentation system should be organized around these responsibilities:

- session continuity
- live website state
- repository structure
- information architecture
- page inventory
- source-doc requirements
- internal linking
- documentation closeout
- search indexing
- public content style
- Knowledge Base article template ownership
- Blog strategy and reader-experience planning
- Blog engagement, attribution, and link-safety planning
- Claude polish workflow
- SEO planning
- old-site migration
- future scripts and validation

---

## Workflow Guardrail Ownership Rule

TENSA website workflow guardrails are owned across the internal documentation system as follows:

- `tensa_website_resume_prompt.md` owns fresh-session startup behavior, current operating rules, source loading, and the compact continuation handoff.
- `documentation_closeout_protocol.md` owns end-of-session workflow, repository-boundary discipline, unknown-authority handling, local evidence requirements, local editor rules, and completion gates.
- `documentation_strategy.md` owns which internal document is responsible for each workflow rule and when each doc should be updated.
- `website_state.md` summarizes current workflow behavior only when future sessions need to know it.

The active writable repository remains locked to `RichBayer/tensaengineering.dev` unless Richard explicitly expands the boundary.

External repositories may be read as source context when required, but they must not be modified from a TENSA website workflow session.

Workflow-only updates must not rewrite public page content, sitemap state, deployment state, indexing claims, branch closeout state, public page inventory, or next public build options unless Richard explicitly approves that website-state or public-content update.

Any source-of-truth document not loaded or bundled in full during the current session is an unknown authority document and must not be modified or summarized as current state from memory.

---

## Current Core Documentation Set

The current core documentation set is:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/ai-operations/claude/claude_website_polish_resume_prompt.md
    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/documentation_strategy.md
    docs/planning/glossary_strategy.md
    docs/planning/content_style_guide.md
    docs/planning/knowledge_base_article_template.md
    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md
    docs/planning/search_answer_optimization_template.md
    docs/planning/search_indexing_strategy.md
    docs/planning/seo_topic_map.md

These docs form the anti-drift system for website build sessions.

---

## Document Roles

### docs/ai-operations/tensa_website_resume_prompt.md

Primary role:

    Fresh-thread startup context.

This document should help a new AI session restart website work safely and quickly.

It should include compressed summaries of:

- current public site state
- current repo path
- current public pages
- branding structure
- operating rules
- source-doc rules
- build-start checks
- next recommended work

It should not become:

- a complete website state document
- a full information architecture document
- a full page inventory
- a full link strategy
- a full source-doc map

Update when:

- the public page set changes
- the repo size or core structure changes
- core operating rules change
- current next steps change
- major completed / incomplete work changes
- new core context docs are added

Keep it compressed.

---

### docs/ai-operations/documentation_closeout_protocol.md

Primary role:

    End-of-session documentation workflow.

This document defines what must happen before a serious website build session is considered complete.

It should include:

- when closeout is triggered
- required build-start or build-end checks
- impacted-doc detection rules
- closeout update order
- completion gates
- commit gates
- full-file replacement rules
- targeted verification after full-file replacements
- public vs internal language rules

It should not become:

- a current website state document
- a page inventory
- a link strategy
- a source-doc map
- a content planning document

Update when:

- closeout workflow changes
- required build-start or build-end checks change
- documentation update rules change
- completion gates change
- commit/review workflow changes
- full-file replacement or verification rules change

Do not update it just because a public page was added unless the closeout workflow itself changed.

---

### docs/ai-operations/claude/claude_website_polish_resume_prompt.md

Primary role:

    Claude prose-polish handoff workflow.

This document defines how Claude should be used as a limited website prose-polish layer.

It should include:

- Claude’s role boundaries
- TENSA ecosystem context
- base voice and tone rules
- page-type style modifiers
- factual boundary rules
- current-vs-future rules
- HTML and Markdown preservation rules
- standard Claude handoff prompt
- optional add-ons for page types
- required handoff back to ChatGPT for factual proofing

It should not become:

- the TENSA source of truth
- a project architecture document
- a public content style guide replacement
- a website state document
- a page inventory
- a place for unverified project claims

Update when:

- Claude workflow changes
- page-type modifier rules change
- public tone/cadence polish rules change
- factual drift problems are discovered in Claude output
- HTML/Markdown preservation rules need refinement
- new page types require Claude-specific add-ons

Claude improves readability.

ChatGPT verifies alignment.

Richard performs final local review and publishes.

---

### docs/website_state.md

Primary role:

    Live-current-state record.

This document describes what is true about the website right now.

It should include:

- current public pages
- current page statuses
- current repo size
- current branding system
- current navigation state
- completed work
- not-yet-completed work
- next recommended steps
- source docs used recently
- working rules
- current anti-drift context pack

It should not become:

- the full long-term information architecture
- the full page inventory
- the full content source map
- the full internal linking strategy
- a build log
- a style guide
- a reusable Knowledge Base article template

Update when:

- serious website sessions change public pages
- navigation changes
- branding changes
- repo structure changes
- page statuses change
- major planning docs are added
- next recommended steps change
- workflow rules change in a way future sessions need to know

The website state document should reflect reality, not intention.

---

### docs/planning/website_information_architecture.md

Primary role:

    Long-term website structure and strategy.

This document defines how the website should grow.

It should include:

- website role
- ecosystem model
- content pillars
- top-level navigation
- page hierarchy
- project page strategy
- Knowledge Base strategy
- Story strategy
- Build Notes strategy
- Resources strategy
- repository boundary rules
- product funnel strategy
- old Argus ACLI site retirement strategy
- open strategic questions

It should not become:

- a live-current-state tracker
- a page-by-page inventory
- a link audit
- a closeout checklist
- a build log
- an article-format template

Update when:

- long-term site architecture changes
- major new sections are added to the long-term plan
- top-level navigation strategy changes
- content pillar strategy changes
- product funnel strategy changes

Do not update it for every small page edit.

---

### docs/infrastructure/tensa_repository_map.txt

Primary role:

    Repository structure and file map.

This document maps the real repository tree and describes the purpose of key files and directories.

It should include:

- current tree output
- root file descriptions
- asset directory descriptions
- public page paths
- internal documentation paths
- missing/planned directories
- recommended future structure
- source-of-truth rules
- build-start checks

It should not become:

- a full website state document
- a full strategy document
- a page inventory table
- a content source map
- a Knowledge Base article template

Update when:

- files are added
- files are removed
- directories are added
- directories are removed
- assets are added
- major files are renamed or moved
- repo structure changes enough that future AI sessions could drift

Use the actual command output:

    tree -a -I '.git|.obsidian|node_modules|__pycache__'

Do not update it from memory.

---

### docs/planning/content_source_map.md

Primary role:

    Source-doc requirements before writing factual pages.

This document defines what source material must be loaded before writing, rewriting, or significantly expanding public pages.

It should include:

- page paths
- page role
- required source docs
- special factual cautions
- project-specific source requirements
- future page source requirements

It should not become:

- a page inventory
- a content style guide
- a link strategy
- a full project explainer
- a public copy draft
- an article-format template

Update when:

- new factual page types are planned or created
- source requirements change
- new source docs become available
- a page’s factual scope changes
- old source requirements become obsolete

Before writing factual project pages, check this document first.

If source docs are missing, stop and request them.

---

### docs/planning/page_inventory.md

Primary role:

    Page existence, status, and next-action tracker.

This document tracks what public and important internal pages exist, what state they are in, and what should happen next.

It should include:

- public page paths
- page titles
- page types
- statuses
- purpose
- source-doc requirements summary
- navigation status
- next action
- planned public pages
- planned Knowledge Base categories
- relevant internal docs

It should not become:

- a full information architecture document
- a full source-doc map
- a full link strategy
- a website state narrative
- a reusable article template

Update when:

- public pages are created
- public pages are removed
- public pages are renamed
- page status changes
- new planned public pages are added
- new Knowledge Base categories are added
- important internal docs are added or retired

If a public page exists, it must be tracked here.

---

### docs/planning/internal_linking_strategy.md

Primary role:

    Link destination strategy and reader-flow map.

This document defines preferred internal destinations for major topics and how readers should move through the site.

It should include:

- current active public pages
- current navigation targets
- topic-to-destination map
- temporary links
- future preferred destinations
- reader-flow strategies
- planned link upgrades
- dead-link prevention rules

It should not become:

- a page inventory
- a source-doc map
- a content style guide
- a full SEO topic map
- a reusable article template

Update when:

- major navigation changes
- new public sections are created
- new Knowledge Base categories are created
- topic destination preferences change
- temporary links are replaced by real pages
- pages are renamed or moved

If a topic becomes important enough to appear across the site, define its preferred destination here.

---

### docs/planning/documentation_strategy.md

Primary role:

    Documentation ownership and scaling rules.

This document defines what each internal documentation file is responsible for and when each one should be updated.

It should include:

- documentation responsibility model
- current core documentation set
- document ownership rules
- overlap prevention rules
- update triggers
- future documentation plan
- documentation closeout relationship
- anti-drift rules

It should not become:

- a live website state document
- a page inventory
- a link strategy
- a source-doc map
- a content style guide
- a build log
- a Knowledge Base article template

Update when:

- new internal planning docs are added
- documentation responsibilities change
- documentation overlap problems are discovered
- closeout workflow reveals recurring confusion
- the documentation system needs restructuring

This document should change rarely but should remain authoritative.

---

### docs/planning/glossary_strategy.md

Primary role:

    Glossary scope, term-selection rules, and inline tooltip behavior.

This document defines how the public Glossary page and inline glossary tooltip system should be maintained.

It should include:

- glossary purpose
- term-selection rules
- definition length and tone rules
- inline tooltip usage rules
- guidance for when a term needs a full Knowledge Base article instead
- expansion guardrails

It should not become:

- a full Knowledge Base article plan
- a public copy draft for every definition
- a general content style guide
- a replacement for internal linking strategy
- a reusable long-form article template

Update when:

- glossary scope changes
- glossary term-selection rules change
- inline tooltip behavior changes
- glossary links become noisy or need tighter rules
- the Glossary starts overlapping with Knowledge Base articles

---

### docs/planning/content_style_guide.md

Primary role:

    Public writing voice, tone, and formatting rules.

This document defines how public-facing TENSA pages should sound and read.

It should include:

- public voice
- tone
- page structure patterns
- current-vs-future wording rules
- hype avoidance
- plain-English technical explanation rules
- story-page style guidance
- project-page style guidance
- Knowledge Base style guidance
- product maturity wording rules

It should not become:

- a source-doc map
- a page inventory
- a link strategy
- a current website state document
- a detailed reusable HTML article template

Update when:

- public writing standards change
- page-copy conventions change
- recurring tone/cadence problems are found
- public page types need clearer writing rules
- Claude/ChatGPT polish workflows reveal a style gap

This is the general TENSA public writing standard.

Claude-specific handoff behavior belongs in:

    docs/ai-operations/claude/claude_website_polish_resume_prompt.md

Reusable long-form Knowledge Base article structure belongs in:

    docs/planning/knowledge_base_article_template.md

---

### docs/planning/knowledge_base_article_template.md

Primary role:

    Reusable Knowledge Base article structure and creation guide.

This document defines how future long-form focused Knowledge Base articles should be built.

It should include:

- article structure
- prose-first article flow
- diagram guidance
- list and bullet rules
- callout and FAQ guidance
- SEO and schema expectations
- source-doc checks
- internal-link checks
- HTML/CSS reuse guidance
- article creation workflow

It should not become:

- a live website state document
- a page inventory
- a content source map
- a full public writing voice guide
- a public article draft
- a replacement for browser review or local validation

Update when:

- the preferred Knowledge Base article structure changes
- recurring article-format problems are found
- new reusable article diagram, FAQ, metadata, or schema patterns are adopted
- the reference implementation changes
- future article creation workflows need tighter guidance

Relationship to other docs:

- `content_style_guide.md` owns overall public voice, tone, and writing standards.
- `knowledge_base_article_template.md` owns the reusable article skeleton, pacing, diagrams, FAQ, metadata, source checks, and creation workflow.
- `page_inventory.md` owns whether an article exists, its status, and its next action.
- `content_source_map.md` owns required factual source context before writing or rewriting an article.
- `internal_linking_strategy.md` owns preferred destinations and reader-flow logic.
- `website_state.md` records the current state of the site and notes that this template exists as part of the anti-drift context pack.

---

### docs/planning/blog_strategy.md

Primary role:

    Future Blog strategy and category planning.

This document defines the planned TENSA Engineering Blog role, reader groups, categories, article positioning, SEO/content boundaries, and first public build direction.

It should include:

- blog purpose
- relationship between Blog, Knowledge Base, Build Notes, and Project Pages
- target reader groups
- initial blog categories
- candidate post ideas
- first public blog implementation recommendations
- current planning boundary

It should not become:

- a public article draft
- a page inventory
- a content source map
- an engagement/collaboration policy
- a visual/article layout template
- a live website state record

Update when:

- the blog category model changes
- first-post strategy changes
- public blog implementation scope changes
- blog positioning relative to Knowledge Base, Build Notes, or Projects changes

---

### docs/planning/blog_reader_experience.md

Primary role:

    Future Blog article reader-experience planning.

This document defines how future Blog articles and Blog index/category pages should feel and function for readers.

It should include:

- standard Blog article components
- quick-answer box guidance
- metadata expectations
- related-reading patterns
- contact CTA placement
- optional table-of-contents guidance
- visual/image guidance
- RSS and newsletter planning boundaries
- features to avoid at launch

It should not become:

- the Blog strategy document
- a public page
- a specific article draft
- the general site style guide
- a search indexing operations document

Update when:

- the planned Blog article layout changes
- reader-facing Blog components change
- RSS/newsletter expectations change
- future Blog template decisions are made

---

### docs/planning/blog_engagement_strategy.md

Primary role:

    Future Blog reader contact, collaboration, and link-safety planning.

This document defines how future Blog posts should invite useful contact and handle collaboration without creating comment spam, support promises, or unsafe backlink behavior.

It should include:

- Blog contact CTA direction
- reader-question workflow
- comment-system boundary
- guest-post standards
- cross-site collaboration rules
- attribution expectations
- outbound-link rules
- affiliate/sponsored-link boundaries

It should not become:

- a public collaboration page
- a comment policy for a system that does not exist
- an affiliate program plan
- a replacement for content source requirements
- a public support policy

Update when:

- Blog contact CTA strategy changes
- guest-post or collaboration rules change
- affiliate/sponsored-link policy changes
- a public collaboration or submission page is created

---

### docs/planning/search_answer_optimization_template.md

Primary role:

    Future page-level search-answer clarity and reader-intent optimization template.

This document defines a reusable future workflow for improving pages so they answer likely reader/search questions clearly.

It should include:

- answer-focused page review prompts
- reader-intent checks
- heading and summary improvement patterns
- concise explanation opportunities
- internal-link opportunities
- search-result usefulness considerations

It should not become:

- the technical sitemap/indexing operations doc
- the SEO topic map
- a keyword-stuffing checklist
- a replacement for content style guide
- a page inventory
- a reusable article structure template

Update when:

- the search-answer optimization workflow changes
- recurring page clarity issues are found
- search-answer improvement patterns become reusable
- future SEO/content sessions refine the template

Technical search discoverability belongs in:

    docs/planning/search_indexing_strategy.md

SEO content cluster planning belongs in:

    docs/planning/seo_topic_map.md

---

### docs/planning/search_indexing_strategy.md

Primary role:

    Search discovery, sitemap, robots.txt, and webmaster-tool indexing workflow.

This document defines how the TENSA Engineering site is prepared for search engine discovery.

It should include:

- sitemap.xml rules
- robots.txt rules
- canonical URL rules
- Google Search Console setup status
- Bing Webmaster Tools setup status
- sitemap submission workflow
- indexing expectations
- sitemap update triggers
- relationship to future SEO planning

It should not become:

- a full SEO topic map
- a page inventory
- a content style guide
- a public copy draft
- a general marketing strategy document
- a reusable article template

Update when:

- sitemap.xml is created or changed
- robots.txt is created or changed
- Google Search Console setup status changes
- Bing Webmaster Tools setup status changes
- sitemap submission status changes
- indexing workflow changes
- canonical URL rules change

This document owns technical search discoverability.

Future SEO content strategy belongs in:

    docs/planning/seo_topic_map.md

---

### docs/planning/seo_topic_map.md

Primary role:

    SEO topic planning and article cluster strategy.

This document supports future public content expansion and search-focused educational pages.

It should include:

- topic clusters
- target reader intent
- likely article titles
- internal link targets
- relationship to project pages
- relationship to social content
- priority order

It should not become:

- a keyword-stuffing document
- a public copy draft
- a page inventory replacement
- a search-indexing operations document
- a reusable article template

Update when:

- SEO content strategy changes
- search targets change
- planned Knowledge Base topics change
- content cluster priorities change
- future public article plans change

Technical search discoverability belongs in:

    docs/planning/search_indexing_strategy.md

---

## Future Planning Docs

The following docs are recommended future additions.

They should not be created randomly.

Create them when the site has enough real need.

---

### docs/planning/old_site_migration_plan.md

Purpose:

    Migration and retirement plan for the old Argus ACLI landing page.

Create when:

- TENSA has enough Argus ACLI content to replace the old site
- redirect decisions are ready
- old-site content needs audit and migration
- public links need consolidation

Should define:

- current old-site content
- content worth migrating
- content to retire
- redirect plan
- link update plan
- timing
- risks

Should not be created before there is enough replacement content on TENSA.

---

### scripts/check_internal_links.py

Purpose:

    Automated internal link checker.

Create when:

- manual grep checks become tedious
- more public pages exist
- Knowledge Base categories are added
- Story / Resources / Build Notes sections are added

Should check:

- public HTML files
- internal href targets
- relative links
- anchor bases
- missing destination files
- external links ignored or separately reported

This script should eventually replace manual link-grep checks during closeout.

---

## Documentation Update Categories

Documentation updates should be grouped by change type.

### Public page changes

If public pages are created, removed, renamed, or change status, update:

    docs/planning/page_inventory.md
    docs/website_state.md
    docs/infrastructure/tensa_repository_map.txt

Also update:

    docs/planning/internal_linking_strategy.md

if navigation or major topic destinations changed.

---

### Navigation changes

If primary navigation or major internal links change, update:

    docs/planning/internal_linking_strategy.md
    docs/planning/page_inventory.md
    docs/website_state.md

Also update affected HTML pages.

---

### New public section

If a new public section is created, update:

    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/content_source_map.md
    docs/website_state.md
    docs/infrastructure/tensa_repository_map.txt

If the new section changes long-term strategy, also update:

    docs/planning/website_information_architecture.md

---

### Factual project page expansion

If a factual project page is significantly expanded, first check:

    docs/planning/content_source_map.md

Then update:

    docs/planning/page_inventory.md
    docs/website_state.md
    docs/planning/internal_linking_strategy.md

Update source map only if source requirements changed.

---

### Branding or asset changes

If branding assets or asset directories change, update:

    docs/infrastructure/tensa_repository_map.txt
    docs/website_state.md

Update the resume prompt if the branding change affects future session continuity.

---

### Workflow changes

If build-start, closeout, full-file replacement, replacement verification, connector-read workflow, local-context loading, Claude polish workflow, or AI-session operating rules change, update:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md

Also update:

    docs/ai-operations/claude/claude_website_polish_resume_prompt.md

if the workflow change affects Claude handoff, prose polish rules, page-type modifiers, or factual proofing.

Also update:

    docs/website_state.md

if the workflow change affects future build sessions.

---

### Strategy changes

If long-term site direction changes, update:

    docs/planning/website_information_architecture.md
    docs/website_state.md

Update the resume prompt only if the change is important for fresh-session continuity.

---

### New internal planning docs

If a new internal planning doc is created, update:

    docs/infrastructure/tensa_repository_map.txt
    docs/planning/documentation_strategy.md

Also update:

    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md

if the new doc becomes part of the core anti-drift context pack or future sessions must load it.

Also update:

    docs/planning/page_inventory.md

if the new internal doc is important enough to track in the internal continuity inventory.

Do not update public pages, sitemap.xml, search indexing claims, or public navigation just because an internal planning doc was created.

---

### Knowledge Base article template changes

If the reusable long-form Knowledge Base article structure changes, update:

    docs/planning/knowledge_base_article_template.md
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md

Also update:

    docs/planning/content_style_guide.md

only if public voice, tone, cadence, or general writing standards changed.

Also update:

    docs/planning/content_source_map.md
    docs/planning/internal_linking_strategy.md
    docs/planning/page_inventory.md

only if source requirements, link destinations, page status, or planned article tracking changed.

The template document owns reusable article structure.

It does not automatically change the public page inventory, sitemap, search indexing strategy, or live website state unless actual public pages changed.

---

## Replacement Verification Rule

After each full-file replacement during closeout or live website editing, run a targeted verification check before moving to the next file.

The verification should confirm the intended change actually landed and that old/stale text or links were removed when applicable.

This rule belongs operationally in:

    docs/ai-operations/documentation_closeout_protocol.md

It should also be summarized in:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/website_state.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/content_source_map.md

The rule exists to catch:

- paste mistakes
- missed saves
- wrong-file edits
- stale snippets
- unintended partial replacements

---

## Overlap Prevention Rules

Do not let internal docs compete for ownership.

Use these boundaries:

- Current reality belongs in `website_state.md`.
- Long-term structure belongs in `website_information_architecture.md`.
- File tree belongs in `tensa_repository_map.txt`.
- Page status belongs in `page_inventory.md`.
- Source requirements belong in `content_source_map.md`.
- Link destinations belong in `internal_linking_strategy.md`.
- Search indexing belongs in `search_indexing_strategy.md`.
- SEO topic planning belongs in `seo_topic_map.md`.
- Public content style belongs in `content_style_guide.md`.
- Knowledge Base article structure and creation workflow belong in `knowledge_base_article_template.md`.
- Blog category strategy and first-post direction belong in `blog_strategy.md`.
- Blog article reader experience, quick-answer boxes, article metadata, CTAs, RSS/newsletter planning, and future article layout belong in `blog_reader_experience.md`.
- Blog contact CTAs, reader-question handling, guest-post rules, collaboration, attribution, outbound-link, and affiliate/sponsored-link boundaries belong in `blog_engagement_strategy.md`.
- Claude prose-polish workflow belongs in `claude_website_polish_resume_prompt.md`.
- Session restart context belongs in `tensa_website_resume_prompt.md`.
- Closeout workflow belongs in `documentation_closeout_protocol.md`.
- Documentation ownership belongs in `documentation_strategy.md`.
- Glossary scope and tooltip behavior belongs in `glossary_strategy.md`.
- Search-answer optimization workflow belongs in `search_answer_optimization_template.md`.
- Connector/local source loading workflow belongs in `documentation_strategy.md`, `documentation_closeout_protocol.md`, and `tensa_website_resume_prompt.md`.

If a document begins duplicating another document too heavily, trim it back to summary-level references.

---

## Closeout Relationship

This strategy document does not replace the closeout protocol.

The closeout protocol defines the workflow.

This documentation strategy defines the document ownership model.

During closeout:

1. Use the closeout protocol to determine what needs to be checked.
2. Use this documentation strategy to determine which document owns each update.
3. Update only the docs impacted by the actual session.
4. Avoid broad cleanup unless explicitly approved.
5. Keep documentation aligned with real repo state.

---

## Public vs Internal Documentation Boundary

The `docs/` directory is internal website development documentation.

It is not the public Knowledge Base.

Public Knowledge Base content belongs under:

    knowledge-base/

Internal planning and operations content belongs under:

    docs/

Do not link public pages to internal planning docs.

Public pages should speak to visitors.

Internal docs may contain instructions, rules, source requirements, reusable templates, and operational warnings.

---

## Documentation Growth Rule

Do not create a new planning doc just because a topic exists.

Create a new planning doc only when:

- the topic needs ongoing tracking
- the topic affects multiple pages
- the topic needs repeated future decisions
- the existing docs do not already own it
- keeping it inside another doc would cause bloat or overlap

When adding a new planning doc:

1. Define its purpose.
2. Define what it owns.
3. Define what it does not own.
4. Add it to the repository map.
5. Add it to website state if it becomes part of core context.
6. Add it to the resume prompt if future sessions must load it.
7. Add it to page inventory if it is an important internal continuity doc.
8. Add connector/local-context loading notes if the new doc affects startup or closeout behavior.

---

## Current Recommended Documentation Roadmap

Current active documentation system now includes:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md
    docs/ai-operations/claude/claude_website_polish_resume_prompt.md
    docs/website_state.md
    docs/planning/website_information_architecture.md
    docs/infrastructure/tensa_repository_map.txt
    docs/planning/content_source_map.md
    docs/planning/page_inventory.md
    docs/planning/internal_linking_strategy.md
    docs/planning/documentation_strategy.md
    docs/planning/glossary_strategy.md
    docs/planning/content_style_guide.md
    docs/planning/knowledge_base_article_template.md
    docs/planning/blog_strategy.md
    docs/planning/blog_reader_experience.md
    docs/planning/blog_engagement_strategy.md
    docs/planning/search_answer_optimization_template.md
    docs/planning/search_indexing_strategy.md
    docs/planning/seo_topic_map.md

Next planning doc, when needed:

    docs/planning/old_site_migration_plan.md

Next utility script, when needed:

    scripts/check_internal_links.py

Do not create these until there is enough real need.

---

## Immediate Impact of This Document

When this file changes, update related docs only if the documentation responsibility model, workflow rules, or current core documentation set changed.

For this Blog planning closeout, impacted docs include:

    docs/infrastructure/tensa_repository_map.txt
    docs/planning/website_information_architecture.md
    docs/planning/page_inventory.md
    docs/planning/content_source_map.md
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md

Do not update:

    public HTML files
    sitemap.xml
    robots.txt
    public navigation
    CSS
    JavaScript

unless real public Blog pages or public Blog links are created.

The current Blog planning closeout created internal planning docs and structure-only scaffold directories.

It does not create:

- a public Blog page
- a public Blog article route
- a sitemap entry
- a navigation target
- an RSS feed
- a newsletter signup
- a live search-indexing claim

---

## Final Rule

The website should not grow faster than the documentation system that keeps it organized.

The documentation system should not grow faster than the website needs.

Keep both in balance.

Build deliberately.

Track reality.

Avoid drift.
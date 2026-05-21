# TENSA Engineering Website Documentation Strategy

---

## Purpose

This document defines the long-term documentation strategy for the TENSA Engineering website repository.

TENSA Engineering is growing from a small static website into a modular public ecosystem hub, knowledge platform, product funnel, and public explanation layer for NeuroCore, Argus ACLI, and Argus Lab.

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

The goal of this document is to define what each internal documentation file is responsible for, when it should be updated, and how the documentation system should scale as the public site grows.

This is an internal planning document.

It is not a public website page.

---

## Core Principle

Documentation exists to keep the website honest, organized, and scalable.

The public website explains the ecosystem.

The repositories prove the engineering.

The internal TENSA website docs keep the public site aligned with real project state, real source documents, real page inventory, real navigation, and real workflow rules.

If the documentation system becomes confusing, stale, or overlapping, the website will eventually drift.

The documentation system should grow deliberately, not randomly.

---

## Documentation Responsibility Model

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
- Claude polish workflow
- SEO planning
- old-site migration
- future scripts and validation

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
    docs/planning/content_style_guide.md
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
- required build-end checks
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
- long-term navigation
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

Update when:

- new internal planning docs are added
- documentation responsibilities change
- documentation overlap problems are discovered
- closeout workflow reveals recurring confusion
- the documentation system needs restructuring

This document should change rarely but should remain authoritative.

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

Update when:

- public writing standards change
- page-copy conventions change
- recurring tone/cadence problems are found
- public page types need clearer writing rules
- Claude/ChatGPT polish workflows reveal a style gap

This is the general TENSA public writing standard.

Claude-specific handoff behavior belongs in:

    docs/ai-operations/claude/claude_website_polish_resume_prompt.md

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

If build-start, closeout, full-file replacement, replacement verification, Claude polish workflow, or AI-session operating rules change, update:

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
- Claude prose-polish workflow belongs in `claude_website_polish_resume_prompt.md`.
- Session restart context belongs in `tensa_website_resume_prompt.md`.
- Closeout workflow belongs in `documentation_closeout_protocol.md`.
- Documentation ownership belongs in `documentation_strategy.md`.

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

Internal docs may contain instructions, rules, source requirements, and operational warnings.

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
    docs/planning/content_style_guide.md
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

For this closeout, impacted docs include:

    docs/infrastructure/tensa_repository_map.txt
    docs/planning/page_inventory.md
    docs/website_state.md
    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/documentation_closeout_protocol.md

Potentially update:

    docs/planning/internal_linking_strategy.md

only if this document changes link strategy.

Potentially update:

    docs/planning/content_source_map.md

only if this document changes source requirements.

---

## Final Rule

The website should not grow faster than the documentation system that keeps it organized.

The documentation system should not grow faster than the website needs.

Keep both in balance.

Build deliberately.

Track reality.

Avoid drift.
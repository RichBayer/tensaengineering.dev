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
- workflow and closeout
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

## Connector Access Documentation Rule

When and how the GitHub connector may be used is set in `docs/ai-operations/operating_rules.md`, under "Editing through the GitHub connector". No other document owns a connector rule.

---

## Hybrid Source Loading Rule

What a session loads at the start, and when local output from Rich is needed, is set in `docs/ai-operations/operating_rules.md`, under "Resuming".

---

## Workflow Guardrail Ownership Rule

Every workflow rule is owned by `docs/ai-operations/operating_rules.md`: resuming, edits and commits, commands, connector use, public content checks, publishing and closeout. This document owns only which document is responsible for which subject.

---

## Current Core Documentation Set

The current core documentation set is:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/operating_rules.md
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

None of these is loaded by default. A session reads the note, the operating rules and only the docs its task names.

---

## Document Roles

### docs/ai-operations/tensa_website_resume_prompt.md

Primary role:

    The live note.

This is the first file a fresh session reads. It lives on `main`.

It should include:

- the date it was last updated
- the two lanes, website work and Blog work
- each lane's branch, active work and next step
- the docs each lane's next step needs
- parked items

It should not become:

- a rule book
- a website state document
- a page list
- a log of completed work

Update when:

- active work, a next step or a parked item changes

Cap: 40 lines.

---

### docs/ai-operations/operating_rules.md

Primary role:

    Every workflow rule, stated once.

It should include:

- resuming
- edits and commits
- commands given to Rich
- editing through the GitHub connector
- what to check before writing public content
- publishing
- closeout

It should not become:

- a website state document
- a tracker of next steps
- a content planning document

Update when:

- a real incident shows a rule is missing or wrong, by the one-in-one-out rule in `README.md`

Where a planning doc and the operating rules disagree about workflow, the operating rules win.

Cap: 150 lines.

---

### docs/ai-operations/documentation_closeout_protocol.md

Primary role:

    A pointer to the "Closeout" section of the operating rules.

It exists so older references to this path still resolve. It holds no rules and should not grow.

Cap: 5 lines.

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

    The facts no other document owns.

It should include:

- branding and asset use
- deployment and exposure facts
- open decisions that have no other tracker

It should not become:

- a status report
- a page list
- a file tree
- a log of completed work
- a rule book
- a list of next steps

Update when:

- a branding choice changes
- a deployment fact changes
- an open decision is made or added

Cap: 120 lines.

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

    What each top-level directory is for.

It should include:

- the published directories and what each holds
- the directories and files kept off the site
- planned directories that do not exist yet

It should not become:

- a file tree
- a file count
- a per-file description list
- a website state document
- a page inventory

Update when:

- a top-level directory is added, removed or changes purpose

For a current file list, use `git ls-files`.

Cap: 60 lines.

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

This script would be the real link check the operating rules call for when links, routes or navigation change.

---

## Documentation Update Categories

What to update at the end of a session is set in `docs/ai-operations/operating_rules.md`, under "Closeout". A planning doc is updated only when its own subject changed. The roles above say what each subject is.

---

## Replacement Verification Rule

How edits are verified is set in `docs/ai-operations/operating_rules.md`, under "Edits and commits".

---

## Overlap Prevention Rules

Do not let internal docs compete for ownership.

Use these boundaries:

- Branding and asset use, deployment and exposure facts, and open decisions belong in `website_state.md`.
- Long-term structure belongs in `website_information_architecture.md`.
- The file tree belongs to the repository itself (`git ls-files`). What each top-level directory is for belongs in `tensa_repository_map.txt`.
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
- Active work and the next step for each lane belong in `tensa_website_resume_prompt.md`, the note.
- Workflow, closeout, and connector or local source loading belong in `operating_rules.md`.
- Documentation ownership belongs in `documentation_strategy.md`.
- Glossary scope and tooltip behavior belongs in `glossary_strategy.md`.
- Search-answer optimization workflow belongs in `search_answer_optimization_template.md`.

If a document begins duplicating another document too heavily, trim it back to summary-level references.

---

## Closeout Relationship

The closeout steps are in `docs/ai-operations/operating_rules.md`. This document says only which document owns a subject.

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
4. Add it to the Current Core Documentation Set and the Document Roles in this document.
5. Name it in the note, or in the operating rules' check-before-you-write list, only if a task must read it.
6. Add it to page inventory if it is an important internal continuity doc.

A new planning doc never sets workflow. If it would change how a session starts or closes, that change goes through the operating rules.

---

## Current Recommended Documentation Roadmap

The current documentation set is:

    docs/ai-operations/tensa_website_resume_prompt.md
    docs/ai-operations/operating_rules.md
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

When this file changes, update another document only if what that document owns has changed.

A change here never touches public HTML, `sitemap.xml`, `robots.txt`, navigation, CSS or JavaScript.

---

## Final Rule

The website should not grow faster than the documentation system that keeps it organized.

The documentation system should not grow faster than the website needs.

Keep both in balance.

Build deliberately.

Track reality.

Avoid drift.
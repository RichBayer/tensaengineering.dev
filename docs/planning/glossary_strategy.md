# TENSA Engineering Glossary Strategy

---

## Purpose

This document defines the strategy for building and maintaining the TENSA Engineering public glossary.

The glossary exists to make the public website easier to understand for:

- technical builders
- Linux learners
- AI systems readers
- non-specialist visitors
- search engines
- AI answer systems

The glossary should help readers understand important technical terms used on public TENSA pages without forcing every page to re-explain every concept from scratch.

The glossary should support:

- human readability
- consistent terminology
- internal linking
- Knowledge Base navigation
- search visibility
- AI answer clarity
- source-grounded public explanations

---

## Core Rule

A term belongs in the public glossary only when it appears on a public page or is needed to understand a public page.

Do not add terms to the public glossary only because they appear in:

- internal planning docs
- source maps
- closeout protocols
- build logs
- repository maps
- AI working notes
- unpublished drafts
- website implementation strategy docs

Planning-only terms should stay in planning docs unless they become public-facing content.

---

## Core Principle

Any technical term used across the public TENSA website that a smart non-specialist reader might not know should either be:

1. briefly defined in context,
2. linked to a relevant Knowledge Base article,
3. linked to a glossary definition,
4. linked to a project page,
5. or captured as a future glossary candidate.

The glossary is not only for TENSA-specific language.

It should cover public-facing terms related to:

- TENSA ecosystem concepts
- AI systems
- Linux and infrastructure
- diagnostics and troubleshooting
- training and learning
- website/search terms only if those terms become public-facing

The glossary should make the site more understandable without making public pages feel slow, over-explained, or cluttered.

---

## What the Glossary Is

The glossary is a public reference layer for technical terms used across the TENSA Engineering website.

It should provide:

- short definitions
- plain-English explanations
- technical context where useful
- TENSA-specific usage notes where relevant
- related terms
- related public pages
- consistent language across the site

The glossary should help readers keep moving.

When a reader hits an unfamiliar term, they should be able to quickly understand it and return to the page they were reading.

---

## What the Glossary Is Not

The glossary is not:

- a replacement for Knowledge Base articles
- a full technical manual
- a Linux textbook
- a generic dictionary
- a marketing keyword list
- an SEO spam page
- a dump of internal planning terminology
- a list of every word used in the repo
- a place to invent public maturity claims
- a place to expose internal implementation details
- a place to define private scenario truth or operational secrets

Glossary entries should be useful, concise, and connected to actual public website content.

---

## Public Glossary Scope

The public glossary should include terms that appear on current public pages or near-term public pages.

Current public glossary scope includes terms from:

- homepage
- Projects index
- NeuroCore page
- Argus ACLI page
- Argus Lab page
- Knowledge Base index
- AI Operations article
- Persistent AI Memory article
- Controlled AI Systems article
- Local-First AI article
- Safe Tool Interaction article
- Linux Diagnostics article
- Troubleshooting Training article
- NeuroCore Architecture article
- Story page

Future public glossary scope may expand when new public pages are added, such as:

- Resources
- Build Notes
- About
- public glossary page
- AI-assisted website building article
- search and answer optimization article
- public product documentation
- install or usage pages

---

## Internal-Only / Deferred Terms

Some terms are useful for planning but should not appear in the public glossary yet.

These terms should be deferred unless they appear on a public page or become part of a public article.

Examples:

- AEO
- AI Search & Answer Optimization
- canonical URL
- crawlability
- DefinedTerm
- DefinedTermSet
- FAQPage schema
- GEO
- JSON-LD
- meta description
- Open Graph
- robots.txt
- Schema.org
- SEO
- sitemap
- structured data
- TechArticle schema
- Twitter card
- WebPage schema

These terms may become public later if TENSA publishes content about:

- AI-assisted website building
- search optimization
- AI answer systems
- structured web publishing
- documentation systems
- website architecture

Until then, keep them in internal planning docs.

---

## Glossary Relationship to Knowledge Base

The glossary and Knowledge Base have different jobs.

### Glossary

The glossary answers:

> What does this term mean?

Glossary entries should be short and direct.

They should define the term and briefly explain how TENSA uses it.

### Knowledge Base

The Knowledge Base answers:

> Why does this concept matter, and how does it work?

Knowledge Base articles should teach ideas more deeply.

They should include examples, reasoning, ecosystem connections, and practical implications.

---

## Glossary vs Knowledge Base Rule

Use a glossary entry when the reader needs a quick definition.

Use a Knowledge Base article when the reader needs a deeper explanation.

Example:

- control plane glossary entry: short definition of what a control plane is.
- Controlled AI Systems Knowledge Base article: deeper explanation of why AI can reason but authority must be governed.

Example:

- raw evidence glossary entry: short definition of original diagnostic signal.
- Linux Diagnostics Knowledge Base article: deeper explanation of evidence-first troubleshooting.

Example:

- local-first AI glossary entry: short definition.
- Local-First AI Knowledge Base article: deeper explanation of trust boundaries, tradeoffs, and TENSA’s design direction.

---

## Public Glossary Location

Recommended public path:

- /glossary/

Recommended file path:

- glossary/index.html

Future optional paths:

- /glossary/ai-systems/
- /glossary/linux-infrastructure/
- /glossary/diagnostics/
- /glossary/training/

The initial version should probably start as one page.

Split into category pages only if the glossary becomes too large for comfortable reading and maintenance.

---

## Glossary Page Goals

The public glossary page should:

1. Explain what the glossary is for.
2. Provide an alphabetized term index.
3. Provide category navigation.
4. Define important technical terms used across public pages.
5. Link terms to related Knowledge Base pages.
6. Link terms to related project pages where appropriate.
7. Use plain English before deeper technical detail.
8. Support future structured data only when appropriate.
9. Avoid turning into a bloated encyclopedia.
10. Help readers understand the TENSA ecosystem more clearly.

---

## Glossary Term Categories

Initial categories:

1. TENSA Ecosystem
2. AI Systems
3. Linux & Infrastructure
4. Diagnostics & Troubleshooting
5. Training & Learning
6. Deferred Search & Web Publishing Terms

Categories are for reader navigation and planning.

The public glossary should only show categories that contain public-facing terms.

The deferred search/web category is primarily an internal planning category until those terms become public-facing.

---

## Category: TENSA Ecosystem

This category covers project names, ecosystem concepts, and TENSA-specific terminology that appears on public pages.

Initial public candidates:

- TENSA Engineering
- NeuroCore
- Argus ACLI
- Argus Lab
- AI Operations
- Knowledge Base
- Story
- controlled AI system
- local-first AI
- operational continuity
- source-of-truth
- source grounding
- context loading
- build log
- resume prompt
- anti-drift
- human authority
- authority boundary

---

## Category: AI Systems

This category covers public-facing AI architecture, model behavior, memory, retrieval, and governance terms.

Initial public candidates:

- AI model
- AI reasoning
- auditability
- CAG-style context assembly
- capability
- context
- context architecture
- context-aware memory
- context pack
- continuity
- control plane
- controlled execution
- execution authority
- execution engine
- governed authority
- governed execution
- hallucination
- local inference
- memory architecture
- model authority
- model explanation
- persistent AI memory
- policy check
- RAG
- reasoning layer
- retrieval
- retrieval-augmented generation
- runtime
- runtime manager
- safe tool interaction
- source grounding
- structured knowledge
- system awareness
- telemetry
- tool boundary
- tool interaction
- tool registry
- traceability
- workflow discipline

---

## Category: Linux & Infrastructure

This category covers Linux, system administration, networking, services, and lab infrastructure terms used on public pages.

Initial public candidates:

- ACLI
- CLI
- command output
- daemon
- default diagnostics
- disk usage
- DNS
- filesystem
- kernel messages
- Linux
- logs
- memory usage
- mounts
- network connections
- network interfaces
- nginx
- package state
- permissions
- ports
- processes
- raw command output
- read-only system inspection
- service
- service status
- system state
- systemd
- terminal output
- unit file
- VM

---

## Category: Diagnostics & Troubleshooting

This category covers troubleshooting concepts, diagnostic process, failure scenarios, and validation language.

Initial public candidates:

- diagnostic intelligence
- diagnostic reasoning
- diagnostics
- evidence
- evidence-backed
- evidence-first troubleshooting
- failed service
- fault
- finding
- investigation
- Linux diagnostics
- raw evidence
- raw output
- read-only diagnostics
- recommendation
- recovery
- root cause
- severity
- signal
- structured diagnostics
- structured evidence
- structured findings
- symptom
- troubleshooting
- validation
- validation environment
- verification
- verification steps

---

## Category: Training & Learning

This category covers Argus Lab’s training model, learning philosophy, progression, and future evaluation direction.

Initial public candidates:

- adaptive difficulty
- assisted mode
- controlled failure
- controlled scenario
- fault injection
- guided resolution
- hint
- independent mode
- mentor-style guidance
- model-guided troubleshooting
- progressive guidance
- real failure scenario
- resettable scenario
- scenario
- support-ticket-style scenario
- troubleshooting training

---

## Category: Deferred Search & Web Publishing Terms

This category is internal-only until these terms become public-facing.

Deferred candidates:

- AEO
- AI answer system
- AI Search & Answer Optimization
- canonical URL
- crawlability
- DefinedTerm
- DefinedTermSet
- FAQPage schema
- GEO
- indexing
- JSON-LD
- meta description
- Open Graph
- robots.txt
- Schema.org
- search snippet
- semantic HTML
- SEO
- sitemap
- structured data
- TechArticle schema
- title tag
- Twitter card
- WebPage schema

These terms should not appear in the public glossary unless the site publishes pages that use or explain them.

---

## Standard Glossary Entry Format

Each glossary term should use this structure:

- Term
- Short definition
- Plain-English explanation
- Technical context
- How TENSA uses it
- Related terms
- Related pages

Not every entry needs every field, but the standard format should be consistent.

---

## Writing Style for Glossary Entries

Glossary entries should be:

- plainspoken
- technically accurate
- concise
- useful
- connected to public site content
- non-hype
- non-academic unless needed
- friendly to readers who are learning

Write plain English first.

Add technical depth second.

Avoid definitions that only make sense to someone who already knows the answer.

Bad:

> RAG is a retrieval pipeline that augments LLM context using embedded vector representations.

Better:

> Retrieval-augmented generation, or RAG, is a way to let an AI model answer using information retrieved from a specific knowledge source instead of relying only on what the model already knows.

Then technical context can explain embeddings, vector databases, retrieval, and context assembly if needed.

---

## Definition Length Rules

Short definition:

- 1 sentence
- usually 15 to 35 words

Plain-English explanation:

- 1 to 3 short paragraphs

Technical context:

- optional
- 1 to 2 short paragraphs

How TENSA uses it:

- 1 short paragraph
- required for TENSA-specific or heavily used terms
- optional for generic terms

Related terms:

- 2 to 6 terms

Related pages:

- 1 to 5 pages

Avoid turning one glossary term into a full Knowledge Base article.

If a term needs more than a few paragraphs, create or link a Knowledge Base article.

---

## Glossary Link Rules

When the public glossary exists:

1. Link the first meaningful mention of a glossary term on a page.
2. Do not link every repeated occurrence.
3. Do not overload a paragraph with glossary links.
4. Prefer a Knowledge Base link when deeper explanation is more useful.
5. Prefer a glossary link when a short definition is enough.
6. Prefer a project page link when the term names a TENSA project.
7. Avoid linking headings unless it helps.
8. Avoid linking common words unless used as technical terms.
9. Do not create links to terms that do not exist yet.
10. Track missing terms for later glossary updates.

The goal is to help the reader, not decorate every noun with an anchor tag.

---

## Preferred Link Destination Rule

A term should have one preferred destination.

Examples:

- NeuroCore -> project page
- Argus ACLI -> project page
- Argus Lab -> project page
- AI Operations -> Knowledge Base article
- Controlled AI Systems -> Knowledge Base article
- control plane -> glossary term or NeuroCore Architecture article depending on context
- raw evidence -> glossary term or Linux Diagnostics article depending on context
- local-first AI -> Knowledge Base article
- systemd -> glossary term
- daemon -> glossary term
- known-good snapshot -> glossary term only after it becomes public-facing

Use the internal linking strategy as the authority for preferred public destinations.

Update the internal linking strategy when glossary destinations become active.

---

## Avoid Over-Linking

Do not link the same glossary term repeatedly on the same page unless the later mention is in a separate major section where the reader may reasonably need the link again.

Only the first meaningful instance of a term should usually link.

---

## Glossary Entry Status Labels

Use internal status labels while building the glossary.

Recommended labels:

- Planned
- Drafted
- Live
- Needs Review
- Needs Source Check
- Needs Related Links
- Needs JSON-LD
- Retired

These labels belong in internal planning docs, not necessarily on the public glossary page.

---

## Public Term Harvesting Rule

When public website pages are created or significantly edited, perform a terminology audit.

The audit should scan public HTML files, not only internal planning docs.

The goal is to identify:

- new public-facing technical terms
- terms already defined in context
- terms that should link to existing glossary entries
- terms that should become new glossary entries
- terms that should link to Knowledge Base articles instead
- terms that should link to project pages instead
- repeated terms that should not be over-linked
- planning-only terms accidentally exposed on public pages

The public glossary should grow from the public site, not from internal planning noise.

---

## Manual Term Harvesting Process

During content closeout:

1. Identify changed public HTML files.
2. Scan page headings, hero text, body copy, cards, FAQ blocks, and CTA sections.
3. Extract technical terms.
4. Compare terms against existing glossary entries.
5. Compare terms against Knowledge Base pages.
6. Compare terms against project page destinations.
7. Mark new glossary candidates.
8. Mark terms that need inline definitions.
9. Mark terms that should not be added because they are planning-only or too generic.
10. Record unresolved terms in a glossary backlog.

---

## Future Automated Term Harvesting

A future script may automate part of the terminology audit.

Possible script path:

- tools/audit_public_terms.py

Potential scan targets:

- index.html
- projects/**/*.html
- knowledge-base/**/*.html
- story/**/*.html
- glossary/**/*.html

Potential output:

- Possible new glossary terms
- Known glossary terms not linked
- Repeated over-linked terms
- Terms appearing across multiple pages
- Planning-only terms accidentally exposed
- Terms needing Knowledge Base links
- Terms needing project-page links

The script should support human review.

It should not automatically rewrite public pages.

It should not automatically add terms to the glossary.

It should produce reviewable output only.

---

## Initial Glossary Build Strategy

Build the glossary in waves.

### Wave 1: Current public-site core terms

Focus:

- AI Operations
- Argus ACLI
- Argus Lab
- authority boundary
- control plane
- controlled AI system
- diagnostic intelligence
- evidence-first troubleshooting
- governed execution
- Linux diagnostics
- local-first AI
- model authority
- NeuroCore
- operational continuity
- persistent AI memory
- raw evidence
- read-only diagnostics
- safe tool interaction
- severity
- source-of-truth
- structured findings
- system awareness
- telemetry
- tool boundary
- troubleshooting training
- verification

Goal:

Support the current homepage, project pages, and existing Knowledge Base articles.

---

### Wave 2: Linux and diagnostics terms

Focus:

- ACLI
- CLI
- daemon
- disk usage
- DNS
- failed service
- filesystem
- kernel messages
- logs
- memory usage
- network connections
- network interfaces
- nginx
- permissions
- ports
- processes
- service
- service status
- system state
- systemd
- unit file
- VM

Goal:

Support Argus ACLI, Linux Diagnostics, Troubleshooting Training, and Argus Lab pages.

---

### Wave 3: Training and Lab terms

Focus:

- adaptive difficulty
- assisted mode
- controlled failure
- controlled scenario
- fault injection
- guided resolution
- independent mode
- mentor-style guidance
- model-guided troubleshooting
- progressive guidance
- real failure scenario
- resettable scenario
- scenario
- support-ticket-style scenario
- validation environment

Goal:

Support Argus Lab and troubleshooting-training content as the Lab page becomes more current and detailed.

---

### Wave 4: Advanced AI architecture terms

Focus:

- CAG-style context assembly
- context architecture
- context pack
- context-aware memory
- execution engine
- local inference
- memory architecture
- policy check
- RAG
- retrieval
- retrieval-augmented generation
- runtime
- runtime manager
- structured knowledge
- tool registry

Goal:

Support NeuroCore, Persistent AI Memory, and NeuroCore Architecture pages.

---

### Wave 5: Search and web publishing terms, if public

Focus only if TENSA publishes public content about website building, AI-assisted publishing, SEO, GEO, AEO, structured data, or AI answer systems.

Deferred examples:

- AEO
- AI Search & Answer Optimization
- canonical URL
- crawlability
- DefinedTerm
- DefinedTermSet
- FAQPage schema
- GEO
- JSON-LD
- Open Graph
- Schema.org
- SEO
- sitemap
- structured data
- TechArticle schema

Goal:

Support future public content about AI-assisted website building or search / answer optimization.

Do not publish this wave until those terms appear in public content.

---

## First Public Glossary Term List

Recommended first public version:

- AI Operations
- Argus ACLI
- Argus Lab
- authority boundary
- control plane
- controlled AI system
- diagnostic intelligence
- evidence-first troubleshooting
- governed execution
- Linux diagnostics
- local-first AI
- model authority
- NeuroCore
- operational continuity
- persistent AI memory
- raw evidence
- read-only diagnostics
- safe tool interaction
- severity
- source-of-truth
- structured findings
- system awareness
- telemetry
- tool boundary
- troubleshooting training
- verification

This is enough to support the current site without trying to define the entire universe on day one.

---

## Terms to Capture But Possibly Defer

These terms should be tracked but may not need public definitions immediately:

- CAG-style context assembly
- context window
- embedding
- vector database
- runtime manager
- tool registry
- execution engine
- known-good snapshot
- VMnet1
- web01
- AL-T1-0001
- guided resolution
- adaptive difficulty
- proficiency level
- certification based on demonstrated ability

Defer terms that are too implementation-specific until they appear naturally in public pages.

---

## Public Glossary Page Structure

Recommended structure:

1. metadata
2. header
3. hero
4. purpose
5. how to use this glossary
6. category navigation
7. alphabetized term index
8. terms by category
9. related Knowledge Base links
10. footer

The glossary should include anchor IDs for each term.

Anchor IDs should be:

- lowercase
- hyphen-separated
- stable
- human-readable
- not dependent on implementation version

---

## Glossary Metadata Guidance

The public glossary page should include:

- title
- meta description
- canonical URL
- Open Graph metadata
- Twitter card metadata
- structured data only when appropriate

Suggested title:

- Glossary | TENSA Engineering

Suggested meta description:

- Plain-English definitions for controlled AI systems, Linux diagnostics, safe tool interaction, troubleshooting training, and TENSA Engineering ecosystem terms.

---

## Structured Data Strategy

The glossary may eventually use structured data.

Recommended type:

- DefinedTermSet

Each term may be represented as:

- DefinedTerm

Structured data should match visible content.

Do not include terms in structured data that are not visible on the page.

Do not use structured data to add hidden keyword lists.

Do not exaggerate page meaning through structured data.

Structured data implementation should wait until the public glossary content is stable.

---

## Glossary Maintenance Rules

Update the glossary strategy when:

- new public terms become important
- new Knowledge Base articles are added
- new project pages introduce technical concepts
- existing terms change meaning
- preferred link destinations change
- public terminology needs standardization
- search / answer optimization strategy changes

Update the public glossary page when:

- a term appears repeatedly across public pages
- readers are likely to need a definition
- a Knowledge Base article depends on the term
- a project page uses the term in a central way
- internal linking opportunities justify the addition

Do not add terms only because they sound impressive.

A term belongs in the glossary because it helps readers.

---

## Glossary Audit Process

When auditing a public page:

1. Identify technical terms.
2. Mark terms already defined in context.
3. Mark terms that should link to project pages.
4. Mark terms that should link to Knowledge Base pages.
5. Mark terms that need glossary definitions.
6. Avoid linking repeated terms excessively.
7. Check that glossary usage does not interrupt readability.
8. Update missing-term backlog if needed.

---

## Missing-Term Backlog Format

Use this format for future glossary backlog tracking:

- Term:
- Category:
- Appears on:
- Suggested destination:
- Needs source check:
- Priority:
- Notes:

Example:

- Term: known-good snapshot
- Category: Linux & Infrastructure / Diagnostics
- Appears on: Argus Lab page
- Suggested destination: Glossary
- Needs source check: Argus Lab web01 baseline docs
- Priority: High
- Notes: Important for explaining current Argus Lab implementation state once the public Argus Lab page describes the implemented web01 baseline.

---

## Privacy and Safety Rules

Do not include glossary terms that expose:

- private scenario truth
- answer keys
- credentials
- internal-only operational paths that should not be public
- security-sensitive details
- unreleased implementation mechanisms that should remain private
- exact internal workflows that could weaken scenario integrity

Some terms can be public at a conceptual level while details remain private.

Example:

Private truth can be defined conceptually if needed, but actual private truth files, paths, or answers must not be exposed.

---

## Initial Internal-Linking Updates Needed

When the public glossary exists, update:

- docs/planning/internal_linking_strategy.md
- docs/planning/page_inventory.md
- docs/planning/content_source_map.md
- docs/planning/search_answer_optimization_template.md
- docs/website_state.md

Also update sitemap.xml if the public glossary route is added.

---

## Documentation Closeout Integration

The terminology audit should become part of website documentation closeout.

Recommended closeout addition:

### Glossary and Terminology Closeout Check

When public HTML pages are created or significantly edited, scan the changed public pages for technical terms.

Identify:

- new terms that need inline definition
- terms that should link to existing glossary entries
- terms that should become new glossary entries
- terms that should link to a Knowledge Base article instead
- terms that should link to a project page instead
- repeated terms that should not be over-linked

A term belongs in the public glossary only when it appears on a public page or is needed to understand a public page.

Planning-only terms stay in planning docs unless they become public website content.

---

## Recommended First Implementation Path

1. Approve this glossary strategy.
2. Add public route planning for /glossary/.
3. Draft first public glossary page with Wave 1 terms.
4. Add structured data only after visible terms are stable.
5. Add glossary route to sitemap.
6. Add glossary link to relevant pages where useful.
7. Update internal linking strategy.
8. Update page inventory.
9. Update content source map.
10. Run link checks.
11. Perform closeout updates.

---

## Final Rule

The glossary should make TENSA easier to understand.

It should help readers learn the language of controlled AI systems, Linux diagnostics, troubleshooting training, and source-grounded engineering without turning the site into a jargon maze.

The standard is:

> Public terms only. Plain English first. Technical accuracy second. TENSA context third. Links where they help.

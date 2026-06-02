# TENSA Engineering Search & Answer Optimization Template

---

## Purpose

This document defines the TENSA Engineering public page standard for making website content clear, readable, crawlable, internally connected, and easy for AI answer systems to understand without inventing context.

The goal is to optimize public pages for:

- human readability
- traditional search engines
- AI answer systems
- source-grounded summaries
- internal linking
- glossary expansion
- factual status clarity
- future content growth

This standard combines:

- SEO: Search Engine Optimization
- GEO: Generative Engine Optimization
- AEO: Answer Engine Optimization
- semantic page structure
- glossary-backed terminology
- current / near-term / future status boundaries
- source-of-truth discipline

The working goal is simple:

> Make TENSA pages easy for humans to read, easy for search engines to crawl, and hard for AI systems to misunderstand.

---

## Core Principle

TENSA pages should be useful first.

Optimization must not mean keyword stuffing, hidden text, fake authority, inflated claims, or generic AI marketing.

A well-optimized TENSA page should:

- explain the topic clearly
- define important terms
- answer the reader’s likely questions
- separate current implementation from future vision
- link to the best related pages
- avoid duplicated explanations across the site
- preserve technical honesty
- give AI answer systems clean, accurate material to summarize

The page should be structured enough for machines, but still written for people.

---

## What This Standard Is Not

This standard is not:

- a trick for manipulating AI search
- a replacement for useful content
- a keyword-spam checklist
- a reason to make pages longer than necessary
- a reason to hide machine-targeted text on public pages
- a reason to overstate maturity
- a substitute for source-of-truth documentation

TENSA public pages should remain clear, grounded, readable, and human.

---

## Page Types Covered

This template applies primarily to:

- project pages
- Knowledge Base articles
- glossary entries
- future Build Notes pages
- future Resources pages
- future About pages
- major public explanation pages

The homepage may use a lighter version of this standard because its role is to introduce and route, not explain everything.

---

## Standard Page Goals

Every major public page should help the reader understand:

1. What the topic is.
2. Why it matters.
3. What exists now.
4. What is being built next.
5. What is future vision.
6. How the topic fits the TENSA ecosystem.
7. Which related pages explain deeper concepts.
8. Which terms have glossary definitions.
9. What claims are grounded in current source material.
10. Where the reader should go next.

---

## Required Source Discipline

Before writing or significantly rewriting a factual page:

1. Check the repository map.
2. Check the content source map.
3. Load the required source-of-truth docs.
4. Confirm the current implementation state.
5. Confirm what is near-term work.
6. Confirm what is future vision.
7. Avoid filling gaps from memory.
8. Ask for missing docs when needed.

Do not invent implementation status.

Do not imply that planned or future work is available now.

Do not describe a feature as released, downloadable, installable, packaged, hosted, or production-ready unless the source documents prove it.

---

## Standard Page Structure

Most major public pages should follow this structure.

Not every page needs every section, but deviations should be intentional.

---

## 1. Metadata Block

Each public HTML page should include:

- unique `<title>`
- meta description
- canonical URL
- Open Graph title
- Open Graph description
- Open Graph URL
- Open Graph image
- Twitter card metadata
- JSON-LD structured data where appropriate

The metadata should accurately describe the page.

Avoid vague titles like:

> NeuroCore | TENSA Engineering

Prefer more descriptive titles like:

> NeuroCore | Local-First AI Platform for Controlled System Intelligence

Meta descriptions should:

- be human-readable
- describe the actual page
- include the primary topic naturally
- avoid hype
- avoid false maturity
- stay aligned with current implementation status

---

## 2. Header and Navigation

Each page should preserve consistent site navigation.

Current primary navigation:

- Home
- Projects
- Knowledge Base
- Story

Before adding new links:

1. Confirm the destination exists.
2. Confirm the preferred destination in the internal linking strategy.
3. Avoid dead links.
4. Avoid linking to internal planning docs from public pages.
5. Avoid turning the header into a crowded menu.

Future navigation additions should be deliberate and tracked in the relevant planning docs.

---

## 3. Hero Section

The hero section should quickly orient the reader.

Recommended elements:

- eyebrow label
- clear H1
- short subtitle
- one primary action
- one secondary action when useful
- optional brand image or visual asset

The H1 should state the page’s main idea plainly.

Good pattern:

> Real Linux troubleshooting, practiced on real failure.

Avoid:

> The Future of AI-Powered Troubleshooting Is Here

Hero subtitles should be two to four sentences maximum.

They should answer:

- What is this?
- Why should I care?
- What is the current status or role?

---

## 4. Quick Answer Section

Each major page should include an early direct-answer section.

Recommended heading patterns:

- What is NeuroCore?
- What is Argus ACLI?
- What is Argus Lab?
- What is controlled AI?
- What is persistent AI memory?
- What is safe tool interaction?

This section should be written so a human, search engine, or AI answer system can extract a clean summary.

Recommended length:

- 1 short heading
- 2 to 4 short paragraphs
- optional 3-bullet summary

This section should not contain every detail.

It should establish the core definition accurately.

---

## 5. Status Boundary Section

Every factual project page should clearly separate:

- current reality
- near-term work
- future vision

Recommended visible section title:

> Current Status

Recommended format:

### Current reality

Describe only what exists now and has been verified.

### Near-term work

Describe the next planned or active work.

### Future vision

Describe the long-term direction without implying availability.

This section is especially important for:

- NeuroCore
- Argus ACLI
- Argus Lab
- install/download guidance
- model-guided troubleshooting
- memory and continuity features
- hosted services
- certification or user-account features
- remote diagnostics
- packaging

---

## Status Language Rules

Use current-state phrases when describing verified work:

- currently
- today
- in the current implementation
- the current version
- the current baseline
- the current public site
- verified
- implemented
- built
- tested
- validated
- protected by snapshot
- available in the current repository

Use near-term phrases for active next steps:

- near-term
- next planned phase
- next validation step
- currently being prepared
- planned next
- the next implementation pass
- the immediate focus

Use future phrases for longer-term direction:

- planned
- future-phase
- intended
- long-term
- future versions may
- the roadmap includes
- this is designed to support
- this is not currently available
- this should not be treated as released

Avoid false maturity phrases unless source docs prove them:

- production-ready
- released
- generally available
- enterprise-grade
- fully automated
- self-healing
- downloadable now
- installable now
- hosted platform
- complete training product

---

## 6. Why It Matters Section

Each page should explain the real problem.

Recommended questions to answer:

- What problem does this solve?
- What failure or gap does this address?
- Why does the reader need this concept?
- Why is the TENSA approach different?
- Why does this matter in real systems?

This section should be practical, not philosophical fluff.

For TENSA pages, strong “why it matters” themes include:

- AI loses usefulness without continuity.
- Raw output alone is not always enough.
- Real diagnostics require evidence.
- Real system interaction requires governance.
- Troubleshooting skill requires practice.
- AI should reason, but authority must be controlled.
- Local-first systems keep trust boundaries closer to the user.
- Documentation and source-grounding reduce drift.

---

## 7. Ecosystem Fit Section

Major pages should explain how the topic fits into the TENSA ecosystem.

Recommended structure:

- TENSA Engineering: public hub, knowledge platform, ecosystem portal
- NeuroCore: local-first governed AI runtime and system-awareness foundation
- Argus ACLI: first practical product / distribution built on NeuroCore
- Argus Lab: real-Linux training and validation environment
- Knowledge Base: public teaching layer
- Story: origin and philosophy

Do not repeat the full ecosystem explanation on every page.

Use a short explanation and link to the best related pages.

---

## 8. Core Concepts Section

Each page should identify the most important concepts a reader needs.

Use cards, short subsections, or concise headings.

Each concept should include:

- plain-English explanation
- technical term where appropriate
- why it matters
- link to deeper explanation if available
- glossary link if available

---

## 9. FAQ / Direct Answer Section

Major pages should include a short FAQ or direct-answer block when useful.

This helps:

- human scanning
- search snippets
- AI answer extraction
- long-tail search queries
- reader confidence

Recommended question count:

- 3 to 6 questions

Good FAQ questions:

- Is Argus ACLI read-only?
- Is Argus Lab available now?
- Does NeuroCore let the model control the machine?
- What makes Argus Lab different from a normal tutorial?
- Why does TENSA focus on local-first AI?
- What does “controlled AI system” mean?

Answers should be short, factual, and source-grounded.

Do not use FAQ sections to sneak in hype.

---

## 10. Related Reading Section

Each page should guide the reader to the next useful page.

Recommended related link categories:

- related project pages
- related Knowledge Base articles
- glossary terms
- Story page
- future Build Notes
- future Resources page

Use natural link text.

Avoid generic “click here.”

Good:

> Read the Linux Diagnostics article for a deeper explanation of evidence-first troubleshooting.

Bad:

> Click here.

---

## 11. Proof / Source Boundary Section

Some pages should include a light public proof section.

This may reference:

- public GitHub repositories
- public project pages
- current implementation status
- build notes after created
- selected public documentation
- verified baseline state

Do not link public pages to private internal planning docs.

Do not expose private scenario truth, credentials, internal-only instructions, or implementation details that should remain private.

If a page makes a specific current-status claim, make sure it is grounded in source docs.

---

## 12. Footer Call to Action

Each page should end with a useful next step.

Possible CTA patterns:

- explore a related project
- read the next Knowledge Base article
- return to Projects
- read the Story
- review related architecture article
- future Resources page when available

Avoid salesy CTAs unless the site later supports actual product adoption.

---

## Search & Answer Optimization Checklist

Use this checklist before publishing or replacing a public page.

### Human readability

- [ ] H1 is clear.
- [ ] Subtitle explains the page quickly.
- [ ] Paragraphs are short.
- [ ] Sections are easy to scan.
- [ ] Technical terms are defined or linked.
- [ ] The page does not read like internal planning notes.
- [ ] The page does not sound like generic AI marketing.
- [ ] The page has a clear next step.

### SEO basics

- [ ] Title is unique and descriptive.
- [ ] Meta description is accurate.
- [ ] Canonical URL is correct.
- [ ] Open Graph metadata exists where appropriate.
- [ ] Twitter card metadata exists where appropriate.
- [ ] JSON-LD exists where appropriate.
- [ ] Page URL matches sitemap strategy.
- [ ] Page is linked from at least one logical public page.
- [ ] Page does not have broken internal links.

### AI answer readiness

- [ ] Page includes a direct “What is…” style definition when appropriate.
- [ ] Page has clear headings.
- [ ] Page separates current reality from future vision.
- [ ] Page avoids ambiguous maturity claims.
- [ ] Page defines important entities and terms.
- [ ] Page uses consistent names across the ecosystem.
- [ ] Page contains direct-answer sections or FAQ where useful.
- [ ] Page is easy to summarize accurately.

### Source-grounding

- [ ] Required source docs were loaded before factual edits.
- [ ] Current implementation claims are verified.
- [ ] Near-term work is clearly labeled.
- [ ] Future vision is clearly labeled.
- [ ] No planned feature is described as currently available.
- [ ] No private or internal-only details are exposed.
- [ ] Public copy matches the current source-of-truth state.

### Internal linking

- [ ] First meaningful mention of major topics links to the preferred destination.
- [ ] Repeated terms are not over-linked.
- [ ] Glossary terms are linked where useful.
- [ ] Knowledge Base links are used for deeper concept explanation.
- [ ] Project page links are used for ecosystem/product explanation.
- [ ] No links point to missing pages.
- [ ] No public page links to internal planning docs.

### Glossary readiness

- [ ] Important terms are identified.
- [ ] Terms use consistent naming.
- [ ] Terms that need definitions are either linked or marked for glossary creation.
- [ ] Page avoids redefining the same term in multiple conflicting ways.
- [ ] Glossary expansion opportunities are captured for later.

---

## Glossary Linking Rules

When a public glossary exists, use these rules:

1. Link the first meaningful mention of a glossary term.
2. Do not link every repeated occurrence.
3. Prefer a Knowledge Base link when the reader needs a full conceptual explanation.
4. Prefer a glossary link when the reader needs a short definition.
5. Prefer a project page link when the term names a TENSA project.
6. Avoid linking terms inside headings unless it improves clarity.
7. Do not overload paragraphs with too many links.
8. Do not create glossary links to terms that are not yet defined.
9. Track missing terms in the glossary strategy.
10. Keep term definitions consistent across the site.

---

## Entity Naming Rules

Use consistent names:

- TENSA Engineering
- NeuroCore
- Argus ACLI
- Argus Lab
- Knowledge Base
- Story
- AI Operations
- Controlled AI Systems
- Local-First AI
- Safe Tool Interaction
- Linux Diagnostics
- Troubleshooting Training

Avoid casual variants on public pages unless context requires them.

Do not use old project names unless a page specifically explains historical renaming.

---

## Project Status Patterns

### NeuroCore

Current-state language should focus on verified platform implementation and current architecture.

Future-state language should be used for advanced memory, context-aware generation, remote diagnostics, hosted services, and mature product ecosystem features unless source docs prove implementation.

### Argus ACLI

Current-state language should emphasize read-only Linux diagnostics, structured findings, severity, recommendations, raw evidence, daemon path, and current validation state.

Future-state language should be used for packaging, public install/download guidance, broader platform support, and production adoption until those exist.

### Argus Lab

Current-state language should reflect verified implementation.

As of the current source docs, Argus Lab is no longer only planning.

Current verified state includes:

- web01 exists
- web01 uses Ubuntu Server 24.04.4 LTS minimized
- nginx is installed, enabled, active, and listening on TCP port 80
- NeuroCore source runtime exists on web01 at `/opt/neurocore`
- Python venv exists at `/opt/neurocore/.venv`
- NeuroCore daemon starts on web01
- local CLI service diagnostics have been validated through the daemon path
- VMnet1 host-only static networking is configured
- web01 has static IP `192.168.150.20/24`
- no default route exists in the final baseline
- known-good snapshot `web01-known-good-acli-slice-001` exists
- the next planned validation step is `AL-T1-0001` nginx failed-state validation

Near-term language should describe controlled nginx failed-state validation.

Future language should describe the full training, evaluation, mentor-guidance, skill-tracking, and certification-like demonstrated-ability direction.

Do not describe Argus Lab as currently available to users.

Do not describe it as a completed training product.

---

## Structured Data Guidance

Use JSON-LD where it helps clarify page identity.

Common page-level types:

- `WebPage`
- `Article`
- `TechArticle`
- `FAQPage`
- `DefinedTermSet`
- `DefinedTerm`
- `BreadcrumbList`
- `Organization`
- `WebSite`

Use structured data honestly.

Do not add structured data that claims functionality, availability, reviews, products, downloads, courses, software releases, or commercial offers that do not exist.

Structured data should match visible page content.

---

## Recommended Public Page Template

Use this as the default structure for future major pages.

Project page pattern:

1. metadata
2. header
3. project hero
4. quick answer
5. current status
6. why it exists
7. what exists now
8. near-term work
9. future vision
10. ecosystem fit
11. proof / implementation notes
12. FAQ
13. related reading
14. project CTA
15. footer

Knowledge Base article pattern:

1. metadata
2. header
3. article hero
4. quick answer
5. concept explanation
6. why it matters
7. TENSA ecosystem example
8. common misunderstanding
9. related terms
10. related reading
11. next article navigation
12. footer

Glossary page pattern:

1. metadata
2. header
3. glossary hero
4. purpose
5. how to use this glossary
6. category navigation
7. alphabetized term index
8. terms by category
9. related Knowledge Base links
10. footer

---

## Existing Page Audit Process

When bringing existing pages into compliance:

1. Read the current public page.
2. Read the relevant planning docs.
3. Load required source-of-truth docs.
4. Identify stale claims.
5. Identify missing current / near-term / future boundaries.
6. Identify missing glossary terms.
7. Identify missing or weak internal links.
8. Check metadata.
9. Check JSON-LD.
10. Draft a full-file replacement.
11. Run local visual review when possible.
12. Run link checks.
13. Update sitemap only if route changes.
14. Update planning docs during closeout.

Do not apply this mechanically.

Some pages should stay short.

The purpose is clarity, not bloat.

---

## Initial Compliance Priority

Recommended first compliance pass:

1. Argus Lab page
2. Argus ACLI page
3. NeuroCore page
4. Knowledge Base index
5. Existing Knowledge Base articles
6. Projects index
7. Story page
8. Homepage

Reasoning:

Argus Lab has a known stale implementation-status claim and should be corrected first.

Project pages carry the most factual maturity risk.

Knowledge Base pages carry the most glossary and internal-linking opportunity.

The homepage should remain concise and should not be overloaded.

---

## Standard Closeout Requirements

After pages are updated using this standard:

- update page inventory if page status or next action changed
- update content source map if source requirements changed
- update internal linking strategy if preferred destinations changed
- update search indexing strategy if routes, sitemap, robots, or indexing behavior changed
- update website state after major public changes
- update repository map if files are added, moved, renamed, or removed
- run targeted link checks
- verify no planned feature is presented as current
- verify no public page links to internal planning docs

---

## Final Rule

Search and answer optimization should make the site more honest, not more artificial.

TENSA pages should be structured enough for machines to understand, but grounded enough that humans can trust them.

The public standard is:

> Clear to readers. Crawlable by search engines. Understandable by AI systems. Grounded in source-of-truth documentation.

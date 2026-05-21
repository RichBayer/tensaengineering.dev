# Claude Website Polish Resume Prompt

---

## Purpose

This document is the reusable Claude handoff prompt for polishing TENSA Engineering public website pages.

Claude's role is narrow:

    Improve public-facing writing quality without changing factual meaning, technical boundaries, page structure, links, metadata, or product maturity.

Claude is not the source of truth.

Claude is not the system architect.

Claude is not responsible for deciding project facts.

Claude is the prose polish layer.

The normal workflow is:

    Richard drafts / reviews direction
    ChatGPT prepares technically accurate website copy
    Claude polishes tone, cadence, clarity, and flow
    ChatGPT proofreads the Claude-polished result for factual drift
    Richard reviews locally
    Richard publishes

This workflow exists because TENSA pages need to sound clean and human while remaining technically honest.

---

## Core Instruction For Claude

You are polishing public website copy for TENSA Engineering.

Your job is to improve:

- clarity
- readability
- flow
- tone
- cadence
- public-facing polish
- paragraph rhythm
- transitions
- sentence-level smoothness

Your job is not to invent, expand, reinterpret, or exaggerate project facts.

Preserve the factual meaning of the draft.

Preserve the technical boundaries of the draft.

Preserve the current-vs-future status of every system, feature, and product claim.

Preserve the structure unless explicitly instructed otherwise.

---

## TENSA Engineering Context

TENSA Engineering is the public hub, brand home, knowledge platform, and ecosystem portal for NeuroCore, Argus ACLI, and Argus Lab.

The public site explains the ecosystem.

The repositories prove the engineering.

The internal documentation keeps the website honest.

TENSA Engineering focuses on:

- controlled AI systems
- local-first AI
- persistent AI continuity
- AI operations
- governed tool interaction
- Linux diagnostics
- real-system troubleshooting
- evidence-backed technical explanation

TENSA Engineering should not sound like a generic AI startup.

It should sound like a serious builder explaining real systems clearly.

---

## Ecosystem Context

### NeuroCore

NeuroCore is a local-first AI platform for persistent understanding, controlled tool interaction, and real-system awareness.

Important concepts:

- persistent local understanding
- operational continuity
- daemon-based runtime
- runtime manager
- control plane
- execution engine
- tool registry
- structured tool outputs
- observability
- governed execution paths
- local retrieval / RAG foundation
- future structured knowledge and context-aware memory direction

Do not reduce NeuroCore to only AI governance.

Governance is part of the architecture.

The deeper purpose is persistent local understanding with controlled interaction against real systems.

---

### Argus ACLI

Argus ACLI is the first practical product / distribution built on NeuroCore.

It is being built as a local-first, read-only Linux diagnostics tool.

Important concepts:

- read-only by design
- local-first operation
- real Linux telemetry
- structured findings
- severity classification
- recommendations
- raw evidence
- concise output
- optional raw / summary / JSON output modes
- AI explanation grounded in structured evidence

Argus ACLI inspects, structures, and explains.

It does not:

- modify system state
- restart services
- change configuration
- execute fixes
- automate remediation
- replace human judgment

Do not imply install/download readiness unless the source draft explicitly says packaging or release work exists.

---

### Argus Lab

Argus Lab is a planned future real-Linux troubleshooting, training, and validation environment.

Important concepts:

- future-phase status
- real Linux systems
- controlled failure scenarios
- resettable lab sessions
- support-ticket-style troubleshooting
- mentor-style AI guidance
- validation environment for NeuroCore and Argus ACLI
- future skill tracking and proficiency progression

Argus Lab is not currently a finished product.

Do not imply that it is available, downloadable, hosted, released, or ready for users unless the draft explicitly says so.

Argus Lab should not sound like:

- a quiz app
- a fake terminal simulator
- a simple tutorial site
- a finished commercial platform

Core idea:

    Real skill comes from solving real problems.

---

## Core Philosophy

The site should naturally preserve these ideas when they appear in the draft:

    Intelligence without continuity is fragile.

    Continuity must be engineered.

    AI can reason, but authority must be governed.

    Less guessing, more signal.

    The website explains.
    The repositories prove.
    The documentation keeps both honest.

Use these ideas naturally.

Do not force every phrase onto every page.

---

## Base Voice

Every TENSA page should feel like it belongs to the same site.

The base voice should be:

- clear
- grounded
- technically credible
- builder-oriented
- honest
- practical
- human
- confident without hype
- educational without talking down to the reader

The page should sound like:

    A capable engineer explaining a real system clearly.

The page should not sound like:

- a startup pitch deck
- a corporate brochure
- a hype-heavy AI product page
- a raw internal planning note
- a textbook
- a sales funnel
- a vague AI manifesto

The base voice stays consistent across the website.

The page type changes the structure, cadence, and emotional weight.

---

## Page-Type Style Modifier System

Use this model for every Claude polish pass:

    TENSA base voice
        ↓
    Page-type modifier
        ↓
    Specific file/page instructions

Do not use the same emotional cadence on every page.

Preserve the TENSA voice, but adapt the writing pattern to the page type.

A Story page, a Knowledge Base article, a Project page, a Resources page, and an About page should all sound like TENSA Engineering, but they should not feel identical.

The difference should come from:

- section rhythm
- paragraph length
- emotional weight
- technical density
- explanatory structure
- amount of narrative
- amount of direct instruction
- next-step framing

---

## Page-Type Style Modifiers

### Homepage Modifier

Purpose:

    Introduce the ecosystem and route visitors to deeper pages.

Use:

- concise positioning
- strong first impression
- clear ecosystem summary
- short sections
- direct navigation cues
- minimal technical depth
- carefully chosen philosophy lines

Style:

- concise
- confident
- directional
- polished but not salesy
- human but not overly narrative

Avoid:

- turning the homepage into an encyclopedia
- overexplaining architecture
- stuffing every project detail into the first page
- repeating entire project-page summaries
- sounding like a launch announcement

The homepage should act as the front door.

It should make readers understand where they are and where to go next.

---

### Project Page Modifier

Purpose:

    Explain a major ecosystem project in public-facing language.

Use:

- what it is
- why it exists
- what problem it solves
- current status
- current capabilities
- future-phase direction
- ecosystem relationship
- proof or next-step links

Style:

- credible
- technical but readable
- public-facing
- specific
- grounded
- not too dry
- not too emotional

Avoid:

- raw repository documentation tone
- excessive implementation detail
- overloading the page with every architecture decision
- hiding product maturity status
- turning future plans into current features

Project pages should translate technical work into public understanding.

They should not become architecture manuals.

---

### Story Page Modifier

Purpose:

    Explain the origin and philosophy behind the ecosystem.

Use:

- origin
- problem
- turning point
- lesson
- philosophy
- connection to architecture
- connection to current projects

Style:

- warmer
- more reflective
- more narrative
- more flowing
- human
- memorable
- still professional
- still technically honest

Avoid:

- melodrama
- startup mythology
- invented personal details
- exaggerated stakes
- over-polished inspirational language
- making the story sound fictional
- burying the practical lesson

Story pages may carry more emotional weight than project pages.

They should still remain grounded.

The story should feel real because it is real.

---

### Knowledge Base Modifier

Purpose:

    Teach one useful concept clearly.

Use:

- definition
- problem
- why it matters
- plain-English explanation
- technical term when needed
- practical example
- how the concept applies to TENSA / NeuroCore / Argus
- next-step link

Style:

- structured
- educational
- clear
- direct
- more technical when useful
- less emotional
- concept-focused
- SEO-friendly without keyword stuffing

Avoid:

- promotional language
- vague thought leadership
- excessive story language
- turning the article into a project sales page
- dumping internal architecture docs into public copy
- keyword stuffing
- assuming readers already know the concept

Knowledge Base pages should teach.

They should not pitch.

They should help readers understand an idea well enough to care about the related project.

---

### Resources Page Modifier

Purpose:

    Help readers find useful links and next actions.

Use:

- clear sections
- short descriptions
- link groups
- availability status
- current-vs-future labels
- practical next steps

Style:

- brief
- useful
- organized
- low-fluff
- directory-like but still polished
- clear about what exists now

Avoid:

- long narrative sections
- advertising unavailable downloads
- implying install readiness before packaging exists
- turning Resources into another project page
- vague link text

Resources pages should reduce friction.

They should help readers find GitHub repos, videos, docs, downloads, demos, or other public materials when those materials exist.

---

### About Page Modifier

Purpose:

    Explain TENSA Engineering, the mission, and the builder perspective.

Use:

- what TENSA Engineering is
- what it builds
- why it exists
- who it serves
- what principles guide the work
- short origin context if useful

Style:

- professional
- concise
- mission-focused
- human
- builder-oriented
- credible
- not overly autobiographical

Avoid:

- long personal biography
- dramatic founder-story language
- repeating the full Story page
- generic company-page fluff
- vague mission statements
- unsupported business claims

The About page should help readers understand the identity and direction of TENSA Engineering.

The deeper narrative belongs in the Story section.

---

### Build Notes Modifier

Purpose:

    Make technical progress readable to public technical readers.

Use:

- what changed
- why it mattered
- what problem it solved
- what architectural lesson came from it
- where the proof lives

Style:

- practical
- chronological when useful
- technical but approachable
- more public-friendly than source build logs
- specific without becoming noisy

Avoid:

- raw commit-log dumps
- excessive implementation detail
- pretending every small change is a milestone
- marketing language
- unsupported claims about maturity

Build Notes should bridge social content, GitHub proof, and public technical understanding.

They should not replace internal build logs.

---

### Internal Documentation Modifier

Purpose:

    Preserve operational clarity for future build sessions.

Use:

- clear rules
- file paths
- source requirements
- workflow steps
- update triggers
- ownership boundaries
- anti-drift warnings

Style:

- direct
- operational
- precise
- repeatable
- less polished if precision requires it

Avoid:

- making internal docs sound like public website copy
- removing useful repetition
- softening warnings too much
- removing source requirements
- removing command examples
- removing workflow gates

Internal docs exist to prevent drift.

Clarity matters more than elegance.

---

## Cadence Rules

Prefer:

- clear section openings
- short to medium paragraphs
- varied sentence length
- smooth transitions
- plain English before jargon
- focused explanations
- strong but grounded statements

Avoid:

- over-compressed marketing blurbs
- dense architecture walls
- repetitive phrasing
- excessive bullet lists
- robotic sentence rhythm
- dramatic overstatement
- corporate filler
- over-polished language that loses the builder voice

The writing should feel clean, not sanitized.

It should feel human, not theatrical.

---

## Hype Filter

Avoid phrases like:

- revolutionary
- game-changing
- industry-leading
- next-generation
- cutting-edge
- disruptive
- autonomous AI agent
- fully automated infrastructure
- self-healing system
- production-ready
- enterprise-grade
- AI-powered everything
- unlock productivity
- seamless transformation

Prefer grounded alternatives:

- controlled AI system
- governed tool interaction
- structured Linux system intelligence
- diagnostic support
- evidence-backed recommendations
- persistent local understanding
- operational continuity
- read-only diagnostics
- local-first system awareness
- traceable tool interaction
- less guessing, more signal

---

## Current-Vs-Future Rules

Always preserve the distinction between:

- what exists now
- what is currently being built
- what is planned
- what is long-term vision

Use wording like:

- currently
- today
- in the current version
- the current implementation focuses on
- the initial version is designed to
- planned
- future-phase
- intended
- the long-term direction
- future versions may
- this is not currently available

Do not turn future plans into present-tense capabilities.

Do not make planned features sound released.

Do not make under-development products sound production-ready.

---

## Claim Safety Rules

Do not invent:

- features
- product maturity
- architecture details
- release status
- install steps
- download availability
- supported platforms
- commercial plans
- security guarantees
- performance claims
- customer claims
- production readiness
- hosted service availability
- certification or account systems

If a claim is not in the draft, do not add it.

If a sentence sounds smoother but changes the claim, do not use it.

If the draft says a thing is planned, keep it planned.

If the draft says a tool is read-only, keep it read-only.

If the draft says a model explains or guides, do not make it execute, remediate, or control.

---

## HTML Preservation Rules

When polishing an HTML page:

Preserve:

- document structure
- heading hierarchy unless explicitly asked to improve it
- CSS classes
- IDs
- links
- image paths
- script tags
- metadata fields unless improving wording only
- canonical URLs
- Open Graph tags
- Twitter card tags
- JSON-LD structure
- buttons and CTA destinations
- section order unless explicitly asked to restructure

Do not remove sections.

Do not add new sections unless explicitly requested.

Do not change URLs.

Do not change CSS class names.

Do not change project names.

Do not silently change navigation behavior.

Do not replace technical terms with vague marketing language.

---

## Markdown Preservation Rules

When polishing Markdown:

Preserve:

- document title
- heading structure unless asked otherwise
- file purpose
- operational boundaries
- path names
- command examples
- source references
- status labels
- checklists
- ordered workflow steps

Do not turn internal operational docs into public marketing copy.

Do not remove warnings or boundary rules because they sound repetitive.

Operational clarity matters more than elegance in internal docs.

---

## Preferred Editing Behavior

Improve awkward wording.

Reduce repetition.

Make transitions smoother.

Clarify dense sentences.

Break up overly long paragraphs.

Keep important technical distinctions.

Preserve strong phrases when they are accurate.

Do not over-polish the builder voice out of the page.

Do not make everything sound like a brochure.

---

## Forbidden Changes

Do not:

- invent new facts
- add unsupported features
- add unsupported maturity claims
- imply autonomous remediation
- imply live product availability
- imply Argus Lab is released
- imply Argus ACLI modifies systems
- imply NeuroCore gives AI uncontrolled authority
- imply cloud upload is required
- remove local-first framing
- remove read-only framing
- remove raw evidence framing
- remove current-vs-future distinctions
- replace precise technical meaning with vague language
- make the copy sound like venture-capital marketing

---

## Output Rules

Unless instructed otherwise:

- Return the complete replacement file.
- Do not return snippets.
- Do not include commentary before the file.
- Do not include commentary after the file.
- Do not summarize what you changed.
- Do not add markdown fences around the file unless asked.
- Do not ask for permission to continue.
- Do not include alternative versions unless requested.

The output should be ready for Richard to paste into the target file.

---

## Required Handoff Back To ChatGPT

Claude-polished website files must be reviewed before publishing.

After Claude returns a polished version, send it back to ChatGPT for:

- factual drift check
- current-vs-future check
- project maturity check
- technical boundary check
- HTML structure check
- link/path check
- metadata sanity check
- tone consistency check

Claude improves readability.

ChatGPT verifies alignment.

Richard performs final local review and publishes.

---

## Standard Prompt To Paste Into Claude

Use the following prompt when sending a TENSA website page to Claude for polish.

---

You are polishing the writing style of a TENSA Engineering public website page.

Your job is to improve clarity, flow, tone, cadence, and readability while preserving all factual meaning, technical boundaries, page structure, links, metadata, CSS classes, and HTML structure.

Do not invent features.
Do not imply anything is currently available unless the draft says it is.
Do not change project status.
Do not add new product claims.
Do not remove important technical distinctions.
Do not turn future plans into current capabilities.
Do not make the page sound like marketing hype.
Do not make it sound like internal planning notes.

Use the TENSA page-type style system:

    TENSA base voice
        ↓
    Page-type modifier
        ↓
    Specific file/page instructions

The base TENSA voice is clear, grounded, technically credible, builder-oriented, practical, human, and honest about current-vs-future status.

Adapt the cadence to the page type:

- Homepage: concise, directional, ecosystem front door.
- Project page: credible, technical, public-facing, current-vs-future careful.
- Story page: human, reflective, narrative, grounded, not melodramatic.
- Knowledge Base page: structured, educational, concept-focused, less emotional.
- Resources page: practical, organized, low-fluff, link-oriented.
- About page: professional, concise, mission-focused, human but not autobiographical.
- Build Notes page: public-friendly technical milestone summary.
- Internal doc: operational clarity over elegance.

Audience:

- smart general readers
- curious learners
- technical people
- potential users or collaborators

Tone:

- professional
- clear
- practical
- human
- builder-oriented
- technically credible
- not corporate
- not overhyped
- not too dense

Use technical terms only when necessary. When a technical term is important, make it understandable in plain language.

Context:

TENSA Engineering is the public umbrella for an ecosystem that includes NeuroCore, Argus ACLI, and Argus Lab.

NeuroCore is a local-first governed AI runtime platform. It is designed around continuity, controlled tool interaction, structured evidence, and keeping AI reasoning separate from execution authority.

Argus ACLI is the first product/distribution built on NeuroCore. It provides local-first, read-only Linux diagnostics using real system telemetry, structured findings, severity, recommendations, and raw evidence.

Argus Lab is a planned real-Linux troubleshooting, training, and validation environment. It will use controlled failure scenarios, resettable lab sessions, and mentor-style guidance to help users build real troubleshooting skill and validate Argus behavior.

Important factual boundaries:

- Argus Lab is planned/future unless the draft explicitly says a part already exists.
- Argus ACLI is read-only for V1.
- NeuroCore governs execution through a control-plane architecture.
- The AI/model layer may explain and guide, but it does not have uncontrolled authority over the machine.
- Do not imply autonomous remediation.
- Do not imply production maturity beyond what the draft states.
- Do not imply downloads, accounts, certifications, or hosted lab access already exist unless the draft says so.

Formatting:

- Preserve the existing HTML structure.
- Preserve links.
- Preserve CSS classes.
- Preserve metadata unless improving wording only.
- Preserve section order unless the draft specifically asks for restructuring.
- Return the complete replacement HTML file only.
- Do not include commentary before or after the file.

---

## Optional Add-On For Story Pages

Use this addition when polishing a Story page.

---

Additional instruction for this page:

This page may be more human and narrative than the project pages, but it must remain technically honest.

Improve emotional clarity without exaggerating, dramatizing beyond the draft, or inventing personal details.

The story should explain the real origin clearly:

An AI forgot the project.
That exposed the fragility of intelligence without continuity.
Documentation became external memory.
Structured workflows reduced drift.
Local AI suggested persistent understanding.
Real system interaction required governance.
NeuroCore emerged.
Argus became the first practical proof.
Argus Lab became the future training and validation environment.

Use a warmer and more reflective cadence than a Knowledge Base article, but do not become melodramatic.

Keep the story grounded.

Do not turn it into startup mythology.

---

## Optional Add-On For Knowledge Base Pages

Use this addition when polishing a Knowledge Base article.

---

Additional instruction for this page:

This page should teach one idea clearly.

Use a structured educational pattern:

1. Define the concept in plain English.
2. Explain the problem it addresses.
3. Explain why it matters.
4. Introduce technical terminology only when useful.
5. Show how the concept applies to TENSA, NeuroCore, Argus ACLI, or Argus Lab.
6. Route the reader to a useful next step.

Prioritize explanation over promotion.

Use plain English before technical terminology.

Use a more structured, technical cadence than a Story page.

Do not keyword-stuff.

Do not turn the article into a project sales page.

Connect the concept naturally to NeuroCore, Argus ACLI, or Argus Lab only where it helps the reader understand the idea.

---

## Optional Add-On For Project Pages

Use this addition when polishing a Project page.

---

Additional instruction for this page:

This page should explain a major ecosystem project clearly.

Balance technical credibility with public readability.

Preserve:

- current status
- current capabilities
- future-phase direction
- relationship to the rest of the ecosystem
- proof or next-step links
- technical boundaries

Do not make the page too story-heavy.

Do not make it too dry.

Do not turn it into raw repository documentation.

---

## Optional Add-On For Resources Pages

Use this addition when polishing a Resources page.

---

Additional instruction for this page:

This page should be practical and navigational.

Prioritize clarity, organization, and accurate availability status.

Make it easy for readers to find useful links.

Do not add unavailable downloads, unsupported install claims, or future resources as if they already exist.

Keep descriptions short and useful.

---

## Optional Add-On For About Pages

Use this addition when polishing an About page.

---

Additional instruction for this page:

This page should explain TENSA Engineering professionally and concisely.

It may include builder perspective and brief origin context, but it should not become the full Story page.

Keep the tone human, credible, and mission-focused.

Avoid generic company-page fluff.

Avoid unsupported business claims.

---

## Optional Add-On For Build Notes

Use this addition when polishing a Build Notes page.

---

Additional instruction for this page:

This page should make technical progress understandable to public technical readers.

Explain what changed, why it mattered, what problem it solved, and where the proof lives.

Do not dump raw build logs.

Do not overstate the importance of small changes.

Keep the tone practical and specific.

---

## Optional Add-On For Internal Docs

Use this addition when polishing an internal documentation file.

---

Additional instruction for this file:

This is an internal planning or operations document.

Clarity matters more than elegance.

Do not remove operational rules, warnings, source requirements, file paths, update triggers, or anti-drift instructions just because they sound repetitive.

Improve wording only where it makes the document easier to use.

Do not make internal documentation sound like public website copy.

---

## Final Rule

Make the writing cleaner without making the facts looser.

If a change makes the sentence prettier but the system less accurate, reject the change.

The goal is not polish at any cost.

The goal is readable, honest, technically grounded public communication.
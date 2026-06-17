# TENSA Engineering Long-Form Knowledge Base Style Guide

---

## Purpose

This document defines the specialized writing standard for long-form TENSA Engineering Knowledge Base articles.

It extends:

    docs/planning/content_style_guide.md

The general content style guide remains authoritative for public voice, factual discipline, current-vs-future language, hype avoidance, and ecosystem positioning.

This document owns the additional guidance needed for deeper educational articles that must explain technical concepts thoroughly without becoming dry reference manuals, internal planning notes, marketing copy, or compressed summaries.

When the two documents appear to conflict, follow the general content style guide first and use this document to refine long-form flow, teaching depth, cadence, and reader orientation.

This is an internal planning document.

It is not a public website page.

---

## Core Standard

Write like a capable builder explaining a real system to an intelligent reader who may be new to the specific tools or workflow.

The article should feel:

- professional
- practical
- technically grounded
- builder-oriented
- patient without being simplistic
- detailed without becoming bloated
- confident without hype
- educational without sounding academic
- human without becoming casual or chatty

The reader should feel that the author understands both the concept and the practical problems that appear when someone tries to use it.

The article should not feel like:

- a landing page
- a marketing funnel
- a startup pitch
- a glossary entry stretched into an article
- a compressed checklist without explanation
- a raw architecture document
- an internal AI working note
- a generic textbook chapter disconnected from real practice

---

## Reader Assumption

Assume the reader is intelligent and technically curious, but may not already understand every term, tool, or workflow dependency.

Do not assume the reader already knows:

- Git
- repositories
- branches
- commits
- local and remote state
- connectors
- permissions
- source-of-truth rules
- operating rules
- validation boundaries
- session startup and closeout workflows

Introduce the plain-English idea first, then name the technical term, then explain why it matters in practice.

Do not talk down to the reader.

Do not skip the connective explanation that makes a term understandable.

---

## Long-Form Article Goal

A long-form Knowledge Base article should do more than define a concept.

It should help the reader understand:

1. What the concept is.
2. Why the problem exists.
3. What usually goes wrong.
4. How the system or method works.
5. What boundaries or risks matter.
6. How to begin using the idea.
7. What related concepts should be explored next.

A reader who finishes the article should be able to explain the concept in their own words and take a reasonable first step without needing access to private TENSA implementation material.

---

## Recommended Teaching Flow

Use this general flow when it fits the topic:

1. Open with the practical problem.
2. Give a direct answer early.
3. Explain why the problem happens.
4. Define the foundational terms.
5. Show how the parts relate.
6. Explain the workflow or architecture.
7. Describe common failure patterns.
8. Give a lightweight starting method.
9. Answer likely reader questions.
10. Connect the concept to the broader TENSA ecosystem.
11. End with a clear next reading path.

The article does not need to follow this order mechanically, but the reader should always know where they are and why the next section matters.

---

## Direct-Answer Opening

The article should answer its main question near the beginning.

The direct answer should:

- use plain language
- be accurate enough to stand alone
- establish the core method or principle
- avoid trying to explain every detail at once
- create a natural path into the deeper article

After the direct answer, expand the reasoning step by step.

Do not make the reader wait through several sections before learning the central answer.

---

## Depth and Explanation

Long-form Knowledge Base pages are allowed to be substantially longer than landing pages, indexes, and project overview pages.

Do not compress a difficult concept merely to keep the article short.

When a concept is easy to misunderstand:

- define it directly
- explain it in plain English
- contrast it with a nearby concept
- show a practical example
- explain what failure looks like
- explain why the distinction matters

Use more than one explanatory angle when that helps the reader form a reliable mental model.

Do not repeat the same sentence in slightly different words only to add length.

Useful depth adds understanding.

Redundant depth adds noise.

---

## Paragraph and Sentence Flow

Prefer short to medium paragraphs.

Use a longer paragraph only when one connected idea would become harder to follow if split apart.

Paragraphs should usually do one job:

- introduce a concept
- explain a distinction
- provide an example
- describe a risk
- connect one section to the next

Use sentence-length variation.

Short sentences can emphasize an important boundary.

Longer sentences can connect related reasoning when the relationship is clear.

Avoid a repetitive rhythm where every paragraph contains one short declaration followed by another short declaration.

Avoid long, dense blocks that force the reader to unpack several technical ideas at once.

---

## Transitions

Sections should connect logically.

Use transitions that explain why the next topic follows from the previous one.

Good transition pattern:

    Understanding the difference between local and remote state explains why a repository connector may not see the newest work.

Weak transition pattern:

    Next, repository connectors.

The transition should preserve momentum without narrating the table of contents.

Do not overuse phrases such as:

- now let us discuss
- in the next section
- as mentioned above
- it is important to note
- in conclusion

Use them only when they genuinely improve orientation.

---

## Plain English Before Jargon

Technical terms are welcome when they are the correct terms.

At first meaningful use:

1. Explain the idea plainly.
2. Introduce the technical term.
3. Explain why it matters.
4. Link to a glossary entry or deeper article when appropriate.

Example:

    The files currently being edited on your computer are called the local working tree. Those changes may not yet exist in the remote repository that a cloud AI connector can inspect.

Do not introduce unexplained acronyms or tool names merely to sound technical.

If a term is not needed to understand the article, remove it.

---

## Examples and Concrete Scenarios

Use realistic examples to make abstract rules understandable.

Good examples show:

- what the user asked for
- what the AI might misunderstand
- what boundary prevents the mistake
- what evidence resolves the issue

Examples should remain general enough to apply beyond TENSA unless the article is specifically explaining a TENSA project.

Avoid examples that accidentally imply a current product feature, workflow, integration, or capability that has not been verified.

---

## Visual Explanation

Use simple text diagrams, flow diagrams, and repository trees when they make relationships easier to understand.

A useful diagram should:

- explain one relationship
- remain readable on mobile
- use clear labels
- avoid decorative complexity
- match the surrounding explanation

Examples include:

- local-to-remote repository flow
- branch relationships
- session startup flow
- source-precedence order
- continuity loops
- documentation ownership trees

The prose must still explain the diagram.

Do not rely on the visual alone to carry an important rule.

---

## Lists

Use lists when they improve scanning, comparison, sequencing, or recall.

Use narrative prose when the reader needs reasoning, context, or transition.

Avoid replacing an entire article with bullet lists.

A useful pattern is:

1. Explain the concept in prose.
2. Use a list to organize the parts.
3. Follow with a paragraph explaining the consequence or relationship.

---

## Reader-Facing Language

Every public paragraph must teach the reader or explain the subject.

Remove wording that exposes the drafting process or internal content strategy.

Do not publish sentences that sound like the writer is:

- talking to themselves
- negotiating how much value to reveal
- discussing free versus paid content
- describing what a future article should contain
- explaining why a paragraph was included
- instructing the website team
- referring to the draft as a draft
- commenting on internal SEO or editorial goals

Internal-monologue examples to remove:

    A reader should not need a commercial template pack to understand this.

    The public article should teach the method while preserving paid value.

    A future article can expand this section later.

Reader-facing alternatives:

    You can begin with a small set of plain Markdown files.

    Standardized templates can reduce setup time as the workflow grows.

    Repository permissions and recovery practices require deeper treatment than this introduction provides.

Do not announce a future article unless it is an approved public roadmap statement or the destination already exists.

---

## Public Versus Internal Terms

Some phrases that are usually internal may be valid public teaching terms when the article explicitly explains them.

For example:

- repository map
- session closeout
- operating rules
- anti-drift workflow

Use them publicly only when:

- the article defines them
- they are necessary to the concept
- they are written for the reader rather than as instructions to the website team

Do not expose internal TENSA file ownership rules, private planning notes, unpublished implementation details, or hidden workflow prompts merely because the public article discusses the same general concept.

---

## Human Authority and AI Assistance

When describing AI-assisted work, preserve the distinction between assistance and authority.

The AI may:

- inspect available evidence
- identify likely stale documentation
- propose changes
- draft detailed updates
- compare files
- summarize diffs
- help maintain project records

The human remains responsible for:

- approving scope
- approving important decisions
- granting write authority
- reviewing high-impact changes
- resolving ambiguous conflicts
- deciding what becomes part of the accepted project

Do not imply that the human must manually maintain every detailed document from memory.

Teach readers to use AI for the difficult drafting, comparison, and maintenance work while requiring the AI to work from current evidence.

Do not imply uncontrolled AI authority.

---

## Safety and Permission Language

When an article discusses repository or tool access:

- distinguish capability from authorization
- distinguish read access from write access
- distinguish discussion from approval
- recommend narrow permissions
- recommend task branches
- identify review and recovery paths
- avoid absolute safety claims

Prefer:

    Write access should be explicit, narrow, reviewable, and reversible.

Avoid:

    The connector is safe.

    Version control prevents mistakes.

Version control makes changes visible and recoverable. It does not remove the need for review.

---

## Current, Planned, and General Guidance

Separate factual current state from general educational guidance.

General technical explanations may describe how Git, branches, connectors, permissions, and documentation systems commonly work.

TENSA-specific claims must remain grounded in current source material.

When mentioning future TENSA pages, resources, templates, or products:

- do not imply availability
- do not add dead links
- avoid unnecessary roadmap commentary
- mention future direction only when it helps the reader

---

## Tone Boundaries

Use a professional builder voice.

The article may be mildly conversational when it improves clarity, but it should not become casual banter.

Avoid:

- hype
- corporate filler
- motivational language
- cute analogies
- sarcasm
- exaggerated certainty
- artificial authority
- dramatic claims about AI
- vague statements that sound profound but teach nothing

Prefer direct, grounded statements supported by explanation.

---

## Quotation and Callout Style

Use blockquotes or the site's established callout components for memorable principles.

Prefer:

    > Chat history is a workspace. It should not be the project database.

Avoid decorative quotation characters such as:

    « »

Use straight or typographic English quotation marks inside normal prose as appropriate.

Do not overuse callouts. Reserve them for principles worth remembering.

---

## Terminology Consistency

Choose one primary term for each concept and use it consistently.

Examples:

- AI model
- version control
- repository
- local working tree
- local repository
- remote repository
- repository connector
- source of truth
- operating rules
- project-state document
- decision record
- repository map
- session startup
- session closeout
- validation
- verification

Do not alternate between several near-synonyms unless the distinction is intentional and explained.

---

## Technical Accuracy Review

Before publication, review statements that simplify technical behavior.

Check for:

- local versus remote state confusion
- commit versus push confusion
- connector access assumptions
- branch and merge oversimplification
- permission claims
- security guarantees
- product-interface details that may become stale
- anthropomorphic descriptions of AI intent

Prefer:

    These failures often arise from ambiguity, incomplete context, or overly broad permissions.

Avoid:

    The AI meant well but made the wrong choice.

Describe model behavior without assigning human motives when the motive is not relevant.

---

## Claude and Multi-Model Polish Rules

A prose-polish model may improve:

- flow
- transitions
- sentence rhythm
- paragraph cadence
- reader orientation
- repetition
- awkward wording

It must not:

- change technical meaning
- weaken safety boundaries
- introduce unverified facts
- alter current-versus-future status
- remove important distinctions
- convert internal permission rules into implied authority
- add marketing language
- add unexplained terminology
- expose drafting strategy or internal monologue

After polish, ChatGPT or another designated reviewer must compare the result against the source draft and project rules.

The final human review remains required.

---

## Long-Form Knowledge Base Review Checklist

Before publishing, confirm:

- Does the article answer the main question early?
- Does it explain why the problem exists?
- Does it define unfamiliar technical terms in context?
- Does it teach rather than merely list?
- Do the sections follow a logical progression?
- Are transitions natural?
- Are examples concrete and accurate?
- Are diagrams readable and explained in prose?
- Does the article distinguish local and remote state where relevant?
- Does it distinguish capability from authorization?
- Does it preserve human authority?
- Does it avoid internal monologue and editorial strategy?
- Does it avoid commercial boundary discussion inside educational copy?
- Does it avoid dead links and unapproved future promises?
- Does it use glossary links only at meaningful first mentions?
- Does it preserve current-versus-future boundaries?
- Does it avoid unexplained jargon?
- Does it avoid anthropomorphizing model behavior?
- Does it give the reader a practical first step?
- Does it end with a useful next reading path?
- Does it still sound like TENSA Engineering?

---

## Reference Standard

The article:

    How to Keep AI From Losing Project Context

established the initial long-form cadence behind this guide.

The useful qualities to preserve are:

- a direct answer followed by deeper explanation
- patient teaching of foundational tools
- practical examples
- explicit safety boundaries
- simple visual flows
- strong separation between local and remote truth
- use of AI for detailed documentation maintenance
- human control over scope and approval
- thorough explanations written for technical readers

Do not copy the article's exact section structure into every future page.

Preserve the voice and teaching method, then adapt the structure to the concept being explained.

---

## Final Rule

Teach the reader enough to understand the system, recognize the risks, and begin using the method responsibly.

Be thorough where the concept is difficult.

Be direct where the boundary is important.

Keep the explanation grounded in real work.

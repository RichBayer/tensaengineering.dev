---
published: false
---

# TENSA Content Operations Strategy

## Status

Approved planning direction. Not implemented.

## Purpose

TENSA Engineering needs a repeatable way to research, draft, review, format, validate, and prepare public articles without weakening factual discipline or handing publication authority to an AI model.

This document records both the target architecture and the reasoning behind it. The reasoning is part of the design. Future agents must not simplify, replace, or "optimize" the workflow without understanding why its controls exist.

## The Proven Manual Workflow

The current reliable workflow is:

1. ChatGPT loads the relevant repository source documents and produces a technically grounded rough draft.
2. ChatGPT prepares the draft and a structured prompt for Claude.
3. Claude improves readability, cadence, flow, and public-facing polish without changing technical meaning.
4. ChatGPT reviews Claude's version for factual drift, maturity drift, technical boundary changes, path errors, and tone consistency.
5. ChatGPT formats the approved text into the existing website HTML pattern.
6. Richard reviews the page in a local browser and requests edits.
7. Richard approves publication and the work is committed and pushed.

The automation plan exists to preserve this proven sequence while removing repetitive copy-and-paste handoffs, source gathering, file assembly, validation, and branch preparation.

## Problem Being Solved

The website has an expanding content backlog, detailed tone and source rules, multiple project repositories, current-vs-future maturity boundaries, and a growing internal documentation system.

Manual production remains trustworthy but creates recurring friction:

- source documents must be found and loaded for every article;
- external research must be collected and preserved;
- prompts must be rebuilt for each model handoff;
- Claude changes must be compared against the technical draft;
- metadata, schema, links, and HTML structure must be rebuilt carefully;
- validation and branch preparation repeat the same mechanical work;
- context can drift between sessions if the reasons behind decisions are not preserved.

The goal is not maximum content volume. The goal is a controlled system that can prepare strong, reviewable articles while preserving TENSA's credibility.

## Core Design Decision

Use a local-first orchestrated workflow with selective cloud-model review.

- Local infrastructure owns job state, evidence, source collection, repository snapshots, deterministic processing, validation, previews, and Git operations.
- ChatGPT performs repository-grounded technical authorship and technical review.
- Claude performs a narrow prose-polish pass.
- ChatGPT performs the final semantic and factual review of Claude's changes.
- Richard remains the publication authority.

This division is intentional.

## Why Local-First

Local-first is not only a cost decision.

It provides:

- persistent job state that is independent of a chat thread;
- control over repository snapshots and source archives;
- private handling of internal planning and project evidence;
- deterministic validation and repeatable builds;
- a clear place to enforce tool and credential boundaries;
- the ability to resume interrupted work without reconstructing the full article history;
- a controlled Git boundary that models cannot bypass.

The Legion and R730xd have complementary roles.

### Legion role

The Legion is the interactive control node and local inference host.

It is suited for:

- the operator interface;
- orchestration control;
- local LLM inference through the RTX 3060;
- interactive draft inspection;
- approval and revision requests;
- local browser review from Richard's normal workstation.

The GPU runs model inference. A workflow service, not the GPU itself, acts as the orchestrator.

### R730xd role

The R730xd is the parallel workhorse and persistent service host.

It is suited for:

- isolated worker VMs or containers;
- browser and research workers;
- source extraction and archival;
- repository worktrees;
- databases and job state;
- vector search and document indexing;
- HTML generation and deterministic validation;
- storage of artifacts, diffs, reports, and previews.

The server may run small CPU models when useful, but it is not the primary prose-generation system. Its value is doing the work around the models reliably and in parallel.

## Why Cloud Models Remain in the Design

A fully local pipeline is possible, but the current RTX 3060 limits the size and quality of models that can run interactively.

The proven workflow already benefits from complementary cloud-model strengths:

- ChatGPT is used for technical grounding, synthesis, structured review, and final correction;
- Claude is used for prose cadence and readability;
- ChatGPT then checks whether the polish changed meaning.

The target system therefore uses local models for preparatory and lower-risk work while reserving cloud calls for high-value review stages.

Cloud use should be selective, observable, and replaceable. The workflow must not depend on an uncontrolled chain of model calls.

## Why ChatGPT Reviews First

The first cloud review is not a grammar pass.

It must:

- load the exact repository authorities named by the content job;
- verify project facts and maturity status;
- compare external claims against captured sources;
- remove unsupported or misleading claims;
- restructure weak technical explanations;
- produce a complete draft that is safe to polish;
- identify protected technical meanings that Claude must preserve.

This role remains with ChatGPT because the established workflow uses ChatGPT as the technical author and repository-grounded reviewer.

## Why Claude's Role Is Narrow

Claude has produced strong improvements to TENSA prose when given a technically accurate draft and strict boundaries.

Claude is therefore the prose specialist, not the technical authority.

Claude may improve:

- clarity;
- flow;
- cadence;
- transitions;
- paragraph rhythm;
- sentence-level readability;
- natural public-facing tone.

Claude may not:

- introduce new facts;
- change product maturity;
- convert plans into capabilities;
- remove read-only or local-first boundaries;
- add recommendations not supported by the reviewed draft;
- redesign the architecture;
- decide what TENSA products currently do.

This preserves the value of Claude's writing without allowing stylistic polish to become factual drift.

## Why ChatGPT Reviews Again

The final ChatGPT pass must compare Claude's output against the approved technical draft, not merely read the polished version in isolation.

This semantic comparison exists because a smoother sentence can accidentally:

- remove an important qualification;
- overstate certainty;
- imply availability;
- change a planned capability into a current one;
- weaken a safety boundary;
- introduce a new causal claim;
- alter TENSA terminology.

The final reviewer should retain genuine readability improvements while reverting or correcting technical drift.

## Why HTML Generation Is Deterministic

Models should produce final article content and a structured page manifest. A local builder should generate the HTML from approved templates.

This is preferred because it:

- keeps navigation, metadata, canonical URLs, CSS classes, and schema consistent;
- reduces accidental template drift;
- makes diffs smaller and easier to review;
- allows automated validation;
- separates editorial decisions from site assembly;
- avoids asking a model to recreate boilerplate correctly every time.

A model may inspect generated HTML, but it should not freely reinvent the page shell.

## Why Sources Must Be Captured

External URLs alone are not sufficient evidence because pages change, disappear, or become inaccessible.

The local system should preserve, where permitted:

- source title and publisher;
- URL;
- publication or revision date;
- retrieval time;
- relevant extracted text;
- content hash;
- source classification;
- claims supported by the source;
- freshness and confidence notes.

Repository evidence should also be tied to a frozen commit or immutable snapshot.

This lets every reviewer inspect the same evidence and allows later audits to explain why a claim was accepted.

## Why Models Do Not Own Git Credentials

The orchestration system owns repository worktrees and Git operations.

Models receive narrow tools or supplied context for reading. They do not receive unrestricted GitHub credentials.

This prevents a model from:

- pushing unreviewed content;
- merging to `main`;
- modifying unrelated files;
- deleting branches or files;
- bypassing human approval;
- turning a content-generation error into a repository mutation.

## Why Human Approval Is Mandatory

TENSA content represents Richard's projects, judgment, reputation, and public claims.

Automated checks cannot fully determine whether:

- the article sounds like Richard and TENSA;
- the framing is fair;
- a personal lesson is represented correctly;
- a recommendation is responsible;
- the timing is appropriate;
- the page looks right in a real browser;
- the article should be published at all.

The workflow must stop at `HUMAN_REVIEW_REQUIRED` until Richard explicitly approves it.

## Architectural Invariants

The following rules may not be removed casually:

1. Repository and captured source evidence override model memory.
2. All reviewers use the same frozen base repository state and source packet.
3. ChatGPT performs technical review before Claude receives a draft.
4. Claude is a prose-polish layer, not a technical authority.
5. Protected technical meanings must accompany the Claude handoff.
6. ChatGPT performs a semantic and factual review after Claude.
7. Deterministic code generates the site shell and validates the result.
8. Models do not receive unrestricted GitHub credentials.
9. No model may push, merge, or publish without explicit human approval.
10. Current, under-development, planned, and long-term states remain distinct.
11. Public content may not reveal private repository details merely because an agent can read them.
12. Every published factual claim must be traceable to repository evidence, captured external evidence, or clearly identified first-hand experience.
13. Automation must preserve the existing content style, source, linking, article-template, and engagement authorities.
14. The system optimizes for trustworthy reviewable output, not maximum article throughput.

## Alternatives Considered

### Fully local autonomous publishing

Deferred because local model quality and the current GPU may not consistently match the proven GPT and Claude review quality. It would also remove useful separation of roles.

### Cloud-only multi-agent workflow

Rejected as the default because it weakens local state ownership, increases cost, complicates evidence persistence, and risks giving remote agents too much operational authority.

### One model for research, writing, polish, and publication

Rejected because it removes independent review and makes subtle factual drift harder to detect.

### Claude as the primary technical author

Rejected for this workflow because the established process treats repository-grounded ChatGPT output as the technical baseline and Claude as the prose-polish layer.

### Free-form multi-agent conversation

Deferred because open-ended agent councils can loop, duplicate work, and blur authority. A state machine with explicit inputs, outputs, retries, and approval gates is easier to audit.

### Model-generated full HTML

Rejected as the default because deterministic template generation is safer, more consistent, and easier to validate.

### Direct model access to GitHub

Rejected because reading and writing authority should be separated. The local orchestrator should mediate repository access and execute approved Git operations.

## Conditions for Changing the Design

A future session may propose changes, but it must document:

- the specific problem with the current design;
- evidence from actual content jobs;
- which invariant would change;
- the new failure modes introduced;
- how factual, credential, and publication boundaries remain protected;
- a rollback path;
- Richard's explicit approval.

New tools or models do not by themselves justify redesigning the workflow.

## Success Criteria

The planning direction succeeds when one proof article can move through the full workflow with:

- a frozen source packet;
- traceable claims;
- a technically reviewed draft;
- a constrained Claude polish pass;
- a final semantic review;
- deterministic HTML output;
- clean validation;
- a local browser preview;
- a complete diff and evidence report;
- no GitHub push before Richard's approval.

Only after that proof should the workflow be generalized for regular content production.

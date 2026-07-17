---
published: false
---

# TENSA Content Operations Workflow

## Status

Approved workflow planning. Not implemented.

## Purpose

This document defines the planned execution model for producing reviewable TENSA Engineering articles through a controlled local-first workflow.

It does not authorize autonomous publishing. It does not create API integrations, model credentials, GitHub credentials, public pages, or runtime services.

## Operating Model

The workflow uses a state machine rather than a free-form group of agents.

Each state must have:

- defined inputs;
- defined outputs;
- an owner;
- allowed tools;
- completion checks;
- retry rules;
- a recorded decision or artifact;
- a clear next state.

The orchestrator may use different models or tools behind a stable task contract, but no worker may skip required gates.

## Planned Roles

### Richard

Richard is the editorial owner and publication authority.

Richard:

- approves the topic or content job;
- resolves subjective framing questions;
- reviews the rendered local page;
- requests edits;
- approves or rejects publication;
- controls whether a branch is pushed or merged.

### Local orchestrator

The local orchestrator owns:

- job state;
- task routing;
- immutable input references;
- model request construction;
- retry and failure handling;
- artifact storage;
- approval gates;
- repository worktree coordination;
- audit history.

A future implementation may use LangGraph or an equivalent explicit workflow engine. The architecture should not depend on one framework name.

### Local research workers

Research workers may:

- search approved public sources;
- retrieve official documentation and changelogs;
- extract relevant text;
- archive permitted source evidence;
- identify publication and revision dates;
- build claim-to-source mappings;
- flag conflicts or missing evidence.

They may not decide TENSA project facts from public web sources when repository evidence is required.

### Local model workers

Local models may assist with:

- research-question decomposition;
- source triage;
- claim inventory drafts;
- rough-draft preparation;
- metadata suggestions;
- internal-link candidates;
- FAQ candidates;
- repetitive classification tasks.

Local-model output remains provisional until the required review gates pass.

### ChatGPT technical reviewer

ChatGPT receives a structured review packet and performs repository-grounded technical authorship or review.

It must:

- load the named repository authorities;
- use the frozen base commit or supplied snapshot;
- verify external claims against captured evidence;
- preserve current-vs-future distinctions;
- identify unsupported claims;
- produce the safe technical draft;
- identify protected technical meanings;
- generate the constrained Claude handoff.

### Claude prose-polish reviewer

Claude receives the approved technical draft, page-type rules, protected meanings, prohibited changes, and output contract.

Claude may improve prose but may not introduce technical meaning.

### ChatGPT final reviewer

ChatGPT receives both the pre-Claude technical draft and Claude's output.

It must perform a semantic comparison, accept safe improvements, revert drift, and produce final approved content plus a structured page manifest.

### Deterministic site builder

The site builder converts approved content and the page manifest into the existing TENSA page structure.

It owns:

- template assembly;
- canonical metadata placement;
- Open Graph and social metadata;
- structured data generation;
- required header and footer reuse;
- link insertion from approved destinations;
- repeatable output.

### Validation workers

Validation workers perform deterministic checks and produce machine-readable and human-readable reports.

## Planned State Machine

```text
TOPIC_PROPOSED
    -> TOPIC_APPROVED
    -> SOURCE_PLAN_CREATED
    -> RESEARCH_IN_PROGRESS
    -> RESEARCH_COMPLETE
    -> CLAIM_AUDIT_COMPLETE
    -> LOCAL_DRAFT_COMPLETE
    -> GPT_TECHNICAL_REVIEW
    -> GPT_REVIEW_COMPLETE
    -> CLAUDE_POLISH
    -> CLAUDE_POLISH_COMPLETE
    -> GPT_FINAL_REVIEW
    -> CONTENT_APPROVED_BY_MODELS
    -> HTML_GENERATED
    -> VALIDATION_COMPLETE
    -> HUMAN_REVIEW_REQUIRED
    -> HUMAN_REVISION_REQUESTED
       or HUMAN_APPROVED
    -> GIT_BRANCH_PREPARED
    -> PUSH_AUTHORIZED
    -> PUSHED_TO_GITHUB
```

`HUMAN_REVIEW_REQUIRED` is a hard gate.

`PUSH_AUTHORIZED` must require a separate explicit Richard approval. Approval of article wording does not automatically authorize a remote push unless the interface clearly combines those actions and Richard knowingly selects it.

## Content Job Packet

Every article should have a durable content job record.

Minimum identity fields:

```yaml
job_id: TENSA-CONTENT-YYYY-NNNN
status: TOPIC_APPROVED
content_type: blog_post | knowledge_base_article | build_note | other
working_title: string
target_path: string | null
category: string | null
created_at: timestamp
base_repository: RichBayer/tensaengineering.dev
base_commit: immutable_commit_sha
owner: Richard Bayer
```

Minimum scope fields:

```yaml
primary_question: string
target_reader: string
reader_problem: string
direct_answer_goal: string
approved_tensa_connection: string
out_of_scope:
  - item
```

Minimum authority fields:

```yaml
required_repo_context:
  - path
required_external_source_classes:
  - official_documentation
  - current_vendor_information
allowed_public_project_claims:
  - claim_or_reference
private_information_boundaries:
  - boundary
```

Minimum workflow fields:

```yaml
chatgpt_review_required: true
claude_polish_required: true
chatgpt_final_review_required: true
human_browser_review_required: true
push_requires_explicit_approval: true
```

## Source Plan

The source plan is created before drafting.

It identifies:

- repository documents required by `content_source_map.md`;
- article-type authorities;
- current public pages that may be linked;
- official external documentation;
- current facts that require web verification;
- first-hand experience that must be confirmed by Richard;
- prohibited or private source material;
- freshness requirements.

No worker should draft a factual article while required sources remain unresolved.

## Evidence Record

Each external source record should include:

```yaml
source_id: EXT-NNN
publisher: string
title: string
url: string
source_class: official_docs | changelog | vendor_specs | research | discussion | other
published_at: date | null
modified_at: date | null
retrieved_at: timestamp
content_hash: sha256
archive_path: local_path | null
relevant_excerpt_path: local_path
freshness_notes: string
authority_notes: string
supports_claims:
  - CLM-NNN
```

Repository sources should include path and frozen commit SHA.

First-hand experience should be labeled separately and must not be presented as independent external verification.

## Claim Inventory

The system should build a claim inventory before the final draft.

Each material claim should record:

```yaml
claim_id: CLM-NNN
claim_text: string
claim_type: repo_fact | external_current_fact | interpretation | recommendation | first_hand_experience
supporting_sources:
  - source_id_or_repo_reference
confidence: high | medium | low
stability: stable | slow_changing | current
status: supported | needs_review | rejected
```

Low-confidence or unsupported material claims block progression to the technical review unless the review packet explicitly asks ChatGPT to resolve them.

## Initial Local Draft

The local draft is a research-grounded working artifact, not publishable copy.

It should:

- answer one primary question;
- follow the relevant Blog or Knowledge Base pattern;
- separate evidence from interpretation;
- avoid unsupported TENSA project claims;
- mark unresolved sections;
- include source markers that can be mapped during review;
- preserve plain-English explanation before jargon.

## ChatGPT Technical Review Packet

The orchestrator should send a structured request containing:

- job identity and target page type;
- frozen repository commit;
- required repository paths;
- source dossier and claim inventory;
- local rough draft;
- style and article-pattern authorities;
- current-vs-future boundaries;
- public/private information boundaries;
- expected structured output.

Required output fields should include:

```yaml
decision: ready_for_claude | blocked
technical_findings: []
unresolved_claims: []
reviewed_draft: string
protected_meanings: []
claude_polish_instructions: string
source_usage_map: []
```

ChatGPT should use read-only repository access or supplied file content. It should not receive write credentials.

## Protected Technical Meanings

Protected meanings are concise statements Claude must not weaken, remove, or reinterpret.

Examples may include:

- a capability is planned rather than implemented;
- Argus ACLI is read-only for the relevant version;
- the model explains evidence but does not hold uncontrolled execution authority;
- a resume prompt supports continuity but does not replace repository verification;
- a recommendation applies only under stated conditions.

The protected list should be article-specific.

## Claude Handoff Packet

Claude should receive only the context required to polish safely:

- reviewed draft;
- TENSA base voice;
- page-type modifier;
- protected meanings;
- terminology that must remain unchanged;
- prohibited changes;
- current-vs-future labels;
- required output format.

Claude should normally return:

```yaml
polished_draft: string
meaningful_editorial_changes: []
uncertain_preservation_points: []
```

Claude should not perform independent web research or add claims during the polish pass unless a future workflow explicitly creates a separate, reviewed research role.

## ChatGPT Final Review Packet

The final review packet must include:

- the pre-Claude reviewed draft;
- Claude's polished draft;
- Claude's change list;
- protected meanings;
- claim inventory;
- source dossier;
- same repository snapshot;
- relevant page and style authorities.

Required output fields should include:

```yaml
decision: ready_for_html | blocked
final_markdown: string
accepted_claude_changes: []
reverted_or_corrected_changes: []
unresolved_items: []
page_manifest: object
```

The reviewer must compare versions semantically rather than trusting the polish output as a new baseline.

## Page Manifest

The approved manifest should separate editorial content from site assembly.

Possible fields:

```yaml
title: string
slug: string
canonical_path: string
content_type: string
category: string
meta_description: string
social_title: string
social_description: string
author: string
date_published: date
date_modified: date
estimated_reading_time: string
quick_answer: string | null
headings: []
faq: []
related_links: []
source_note: string | null
structured_data_type: Article | BlogPosting
```

The builder should reject incomplete required fields rather than invent them.

## Deterministic HTML Generation

The builder should:

- use the approved TENSA template for the page type;
- preserve common header and footer behavior;
- use approved CSS classes;
- generate metadata from the manifest;
- generate JSON-LD from structured fields;
- add only approved internal and external links;
- emit stable formatting for clean diffs;
- avoid modifying unrelated files.

The builder may later support Markdown plus YAML front matter as the internal editorial source format, but adoption requires a separate implementation decision and migration plan.

## Validation Gates

Validation should include, as applicable:

- required-file and path checks;
- HTML parsing and structural checks;
- heading-order checks;
- canonical URL checks;
- metadata completeness;
- JSON-LD parsing;
- internal-link resolution;
- anchor resolution;
- external source presence;
- stale placeholder detection;
- current-vs-future phrase checks;
- forbidden hype phrase review;
- private path or internal-doc leak detection;
- spelling and style linting;
- changed-file scope check;
- `git diff --check`;
- local rendered-page smoke test.

Automated style checks are advisory unless a rule is explicitly designated as blocking.

Technical integrity, broken links, malformed HTML, invalid structured data, private-information leaks, and missing required evidence should be blocking.

## Human Review Package

The local review interface should show:

- rendered desktop view;
- rendered mobile-width view;
- final article text;
- source dossier;
- claim inventory;
- ChatGPT technical findings;
- Claude change list;
- ChatGPT final corrections;
- validation report;
- full changed-file list;
- Git diff;
- proposed branch name and commit message;
- unresolved warnings.

Richard should be able to:

- approve the article;
- request a revision in plain language;
- edit the editorial source directly;
- return the job to a specific stage;
- reject or archive the job;
- approve branch preparation without approving push;
- explicitly authorize push.

## Revision Handling

A human revision request should become a new recorded job event.

The system should preserve:

- original request;
- affected artifact;
- stage selected for re-entry;
- revised model inputs;
- new output;
- diff from the previous approved candidate;
- reason for acceptance or rejection.

The system should not discard earlier versions.

## Git and Repository Boundary

Each content job should use an isolated worktree or equivalent workspace based on a frozen commit.

Before branch preparation:

- confirm the target base state;
- confirm no unrelated files changed;
- rerun validation;
- generate the proposed commit message;
- preserve the evidence packet locally.

Models do not push.

After Richard authorizes push, the local orchestrator may:

1. create or finalize the named branch;
2. commit the approved files;
3. push the branch;
4. optionally open a draft pull request;
5. report the exact branch, commit, files, and validation result.

Merging to `main` remains a separate human-controlled action unless Richard explicitly changes that policy in a future authority document.

## Credential Boundaries

Credentials should be separated by function.

- research workers receive only the access required for public source retrieval;
- model APIs receive content packets, not GitHub credentials;
- repository read tools are path-scoped and read-only;
- GitHub credentials belong to the local Git worker;
- the Git worker acts only after the approval state permits it;
- secrets must not appear in prompts, artifacts, logs, or generated pages.

## Model Routing

The workflow should use capability-based routing rather than hard-code every step to one permanent model version.

Example task classes:

- local research decomposition;
- local source classification;
- technical authoring review;
- prose polish;
- final semantic review;
- HTML artifact inspection.

A model change must preserve the role contract and pass a proof workflow before becoming the default.

## Failure Handling

The orchestrator should stop and record a blocked state when:

- required repository context is unavailable;
- sources conflict materially;
- evidence is missing;
- a model fails the structured-output contract repeatedly;
- Claude changes protected meaning;
- final review leaves unresolved factual issues;
- validation fails;
- the base branch changes in a way that invalidates the worktree;
- private information appears in public content;
- Richard rejects the article.

Failures should be visible, not silently repaired by changing requirements.

## Audit Record

The content job should preserve:

- state transitions;
- timestamps;
- model and tool versions;
- prompt templates or prompt hashes;
- repository commit references;
- source records;
- artifact hashes;
- reviewer decisions;
- human approvals;
- validation reports;
- Git branch and commit references after authorization.

The audit record exists to support continuity and explain why the final page says what it says.

## Recommended Proof Implementation

The first implementation should process one approved article end to end.

Recommended boundaries:

- one article type;
- one target template;
- one research policy;
- one ChatGPT technical review call;
- one Claude polish call;
- one ChatGPT final review call;
- deterministic HTML generation;
- local validation;
- local browser review;
- branch preparation;
- no automatic merge.

The proof should measure:

- source completeness;
- factual corrections made by ChatGPT;
- useful prose improvements from Claude;
- drift caught during final review;
- validation failures;
- manual edits requested by Richard;
- total API usage;
- time spent in each state;
- whether the final output required less manual handling than the current process.

## Deferred Decisions

The following remain implementation decisions, not settled architecture:

- exact orchestration framework;
- exact local model and quantization;
- GPT Researcher adoption or replacement;
- vector database choice;
- database and object-storage choices;
- LiteLLM or direct provider APIs;
- approval dashboard framework;
- exact Markdown-to-HTML toolchain;
- whether model calls use direct repository tools or preloaded source bundles;
- whether the proof article is a Blog post or Knowledge Base article.

These choices must preserve the strategy invariants.

## Current Planning Boundary

This document defines a future workflow only.

It does not mean:

- the orchestrator exists;
- local workers are deployed;
- API keys are configured;
- models have repository access;
- Markdown is the current website source format;
- HTML generation is automated;
- Git branches are automatically pushed;
- the Blog is publicly launched;
- regular automated content production has begun.

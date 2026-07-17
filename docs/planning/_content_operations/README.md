---
published: false
---

# TENSA Content Operations Planning Set

## Status

Planning only.

No content automation service, public page, public Blog route, API integration, model workflow, GitHub publishing workflow, or production deployment is created by these documents.

## Publishing Boundary

This planning set is stored under an underscore-prefixed internal directory and each document is marked `published: false`.

It must not be:

- linked from public navigation;
- added to `sitemap.xml`;
- referenced from public Blog or Knowledge Base pages;
- treated as a released TENSA capability;
- described as implemented until repository and runtime evidence proves implementation.

## Purpose

These documents define a future controlled content-production workflow for TENSA Engineering.

The workflow is intended to automate the established manual process without removing the controls that made that process reliable:

1. repository-grounded technical drafting;
2. ChatGPT technical and editorial review;
3. Claude prose polish under narrow factual boundaries;
4. ChatGPT final semantic and technical review;
5. deterministic HTML generation and validation;
6. Richard's local browser review and explicit publication approval.

## Documents

- `content_operations_strategy.md`
  - owns the problem statement, design rationale, architectural decisions, rejected alternatives, invariants, trust boundaries, and conditions for changing the design;
- `content_operations_workflow.md`
  - owns the planned state machine, content-job packet, model handoffs, evidence requirements, validation gates, human approval gate, and Git workflow;
- `README.md`
  - owns this planning-set index and publishing boundary.

## Relationship to Existing Authorities

These documents do not replace:

- `docs/planning/blog_strategy.md` for Blog role, categories, and public content direction;
- `docs/planning/blog_reader_experience.md` for reader-facing Blog components;
- `docs/planning/blog_engagement_strategy.md` for contact, collaboration, attribution, and link safety;
- `docs/planning/content_source_map.md` for source requirements before factual writing;
- `docs/planning/content_style_guide.md` for public TENSA voice and tone;
- `docs/ai-operations/claude/claude_website_polish_resume_prompt.md` for Claude's narrow prose-polish contract;
- `docs/planning/knowledge_base_article_template.md` for long-form Knowledge Base structure;
- `docs/planning/documentation_strategy.md` for documentation ownership;
- `docs/website_state.md` for current implemented state;
- `docs/ai-operations/tensa_website_resume_prompt.md` for compressed session startup context.

## Current Planning Boundary

The planning set may describe a target architecture and future implementation sequence.

It must clearly distinguish:

- the current proven manual editorial workflow;
- the approved planning direction;
- future implementation work;
- components that remain optional or under evaluation;
- capabilities that do not yet exist.

No future session may infer implementation from the existence of these planning documents alone.

---
name: swarm-prompt-engineer
description: Create optimized multi-agent swarm prompts that decompose complex missions into orchestrated agent workflows. Use when the user wants to (1) create a prompt for multiple collaborating agents, (2) break down a complex task into subagents, (3) achieve high-accuracy output (0.9+) through multi-agent review, (4) organize agent swarms for research, writing, analysis, or coding tasks, or (5) design agent hierarchies with planners, researchers, executors, fact-checkers, editors, and critics. Triggers on phrases like "agent swarm", "multi-agent", "orchestrate agents", "create a swarm prompt", "meta-analysis", "high accuracy", "decompose into agents", or any complex mission requiring specialized subagent coordination.
---

# Swarm Prompt Engineer

Build production-grade swarm prompts. A swarm prompt is a complete specification that decomposes a complex mission into orchestrated agent roles, workflows, and quality gates.

## Engineering Principles

Read `references/engineering-principles.md` before every swarm design. These four rules -- Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution -- govern all decisions in the swarm design process.

## Swarm Design Workflow

Designing a swarm prompt involves these steps:

1. **Analyze mission** -> verify: mission type, complexity, and accuracy target identified
2. **Design swarm architecture** -> verify: correct pattern selected, agent roles defined
3. **Draft agent prompts** -> verify: every agent has input, output format, and quality criteria
4. **Define quality gates** -> verify: accuracy target is achievable with selected verification
5. **Assemble final prompt** -> verify: complete swarm prompt passes all checklist items

### Step 1: Analyze Mission

Before designing anything, state assumptions and ask if unclear:

```
Mission type: [research / creation / analysis / synthesis / mixed]
Complexity: [low / medium / high / critical]
Accuracy target: [0.0 - 1.0] (default: 0.9 if unspecified)
Domain: [subject area]
Output format: [required format, if specified]
Constraints: [length, style, citation format, etc.]
```

If accuracy target is not stated, assume 0.9. Map target to quality gate:

| Target | Gate | Required Additions |
|--------|------|-------------------|
| 0.7-0.8 | Basic | Self-check by Executor |
| 0.8-0.9 | Standard | + Fact-Checker with source tracing |
| 0.9-0.95 | High | + Critic, redundant Fact-Checker |
| >0.95 | Critical | + Domain-Expert, adversarial review |

### Step 2: Design Swarm Architecture

Read `references/swarm-patterns.md` for full agent taxonomy and workflow patterns.

Select the workflow pattern:

- **Pattern A (Sequential)**: Linear dependencies only. Small missions.
- **Pattern B (Parallel Research)**: Multiple research dimensions. Medium missions.
- **Pattern C (Iterative)**: Progressive refinement. Quality-first missions.
- **Pattern D (Full Swarm)**: Maximum accuracy. Complex, high-stakes missions.

Default to the simplest pattern that achieves the accuracy target. Do not over-engineer.

### Step 3: Draft Agent Prompts

Read `references/agent-templates.md` for prompt templates per role.

For each agent in the swarm, produce a complete prompt containing:

1. **Role definition**: Clear purpose within the swarm.
2. **Input specification**: Exactly what this agent receives.
3. **Output format**: Structured template the agent must follow.
4. **Constraints**: Hard rules and limits.
5. **Quality criteria**: Verifiable conditions for completion.

### Step 4: Define Quality Gates

Read `references/quality-checklist.md` for the complete quality framework.

Every swarm must specify:

- **Verification method**: How facts are checked (source tracing, redundant checks, adversarial review).
- **Integration rules**: How parallel outputs merge without conflict.
- **Final gate**: Editor checklist against original mission requirements.

### Step 5: Assemble Final Prompt

Combine into a single, self-contained swarm prompt with this structure:

```markdown
# Swarm Mission: [Title]

## Overview
- Mission: [one-sentence description]
- Accuracy target: [N.NN]
- Pattern: [A/B/C/D]

## Phase 1: [Name]
### Agent: [Role Name]
[PROMPT]
### Agent: [Role Name]
[PROMPT]
[...]

## Phase 2: [Name]
[...]

## Quality Gates
[Verification rules]

## Final Output Specification
[Exact format and delivery requirements]
```

Before delivering, run the pre-flight checklist from `references/quality-checklist.md`.

## Example: Meta-Analysis on CAR-T Cell Therapy

**User mission**: "Write a meta-analysis on CAR-T cell therapy efficacy in treating B-cell acute lymphoblastic leukemia. Target accuracy: 0.92."

**Analysis**:
- Type: research + synthesis
- Complexity: critical
- Accuracy target: 0.92 -> High gate
- Domain: oncology / immunotherapy
- Output: academic meta-analysis with PRISMA compliance

**Swarm design**:
- Pattern: D (Full Swarm)
- Agents: 1 Planner, 1 Domain-Expert, 3 Researchers, 2 Fact-Checkers, 2 Executors, 1 Critic, 1 Editor, 1 Formatter

**Key decomposition**:

```
Subtask 001: Literature search (RCTs on CAR-T for B-ALL)
Subtask 002: Data extraction (response rates, survival, adverse events)
Subtask 003: Statistical analysis plan (fixed vs random effects)
Subtask 004: Risk of bias assessment (Cochrane RoB 2)
Subtask 005: Draft methods section
Subtask 006: Draft results section
Subtask 007: Draft discussion section
Subtask 008: Cross-verification of all claims
Subtask 009: Critic review of complete draft
Subtask 010: Final editing and PRISMA formatting
```

**Verification**: Every statistical claim checked by 2 Fact-Checkers against original studies. Critic reviews complete draft for methodological soundness. Editor gates against PRISMA checklist.

## Rules

- Always apply Simplicity First: do not add agents beyond what the accuracy target requires.
- Every swarm prompt must include explicit success criteria per subtask.
- Parallelize aggressively; sequentialize only when dependencies force it.
- The final output is the complete swarm prompt, ready for execution.

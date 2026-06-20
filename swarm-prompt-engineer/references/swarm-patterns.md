# Swarm Orchestration Patterns

Reference this file when designing the agent hierarchy and workflow for a swarm task.

## Agent Taxonomy

Every swarm consists of these agent roles. Assign 1..N agents per role based on task complexity.

### Core Roles

| Role | Purpose | When to Add |
|------|---------|-------------|
| **Planner** | Decomposes mission into subtasks, creates execution plan | Always (1) |
| **Researcher** | Gathers information, searches sources, extracts data | When task requires external knowledge (1..N) |
| **Executor** | Performs the core work: writes code, drafts content, analyzes data | Always (1..N, parallelizable by subtask) |
| **Fact-Checker** | Verifies claims, checks sources, validates data accuracy | When accuracy > 0.8 is required (1..N) |
| **Editor** | Reviews output against requirements, polishes, ensures consistency | Always (1..2) |
| **Integration** | Merges parallel outputs, resolves conflicts, produces final deliverable | When N>1 Executors (1) |

### Specialized Roles (add as needed)

| Role | Purpose | When to Add |
|------|---------|-------------|
| **Domain-Expert** | Provides deep subject-matter expertise | Highly technical domains (medicine, law, finance) |
| **Critic** | Stress-tests reasoning, finds edge cases, challenges assumptions | High-stakes or complex reasoning tasks |
| **Formatter** | Handles output formatting, citations, style compliance | Strict format requirements |

## Workflow Patterns

### Pattern A: Sequential Pipeline

For tasks with linear dependencies (e.g., research -> write -> edit).

```
Planner -> Researcher -> Executor -> Editor -> Output
```

Use when: Each step depends on the previous output.

### Pattern B: Parallel Research, Sequential Execution

For tasks requiring broad research before focused execution.

```
Planner -> [Researcher-A, Researcher-B, Researcher-C] (parallel)
        -> Integration (merge findings)
        -> [Executor-A, Executor-B] (parallel by section)
        -> Integration (merge sections)
        -> Editor -> Output
```

Use when: Task has multiple independent research dimensions or output sections.

### Pattern C: Iterative Refinement

For tasks requiring progressive quality improvement.

```
Planner -> Executor -> Critic -> [Executor + Critic loop N times] -> Editor -> Output
                  ^                    |
                  |____________________|
```

Use when: Maximum quality is required; task benefits from multiple revision cycles.

### Pattern D: Full Swarm (Research + Parallel + Iterative)

For complex, high-accuracy missions (e.g., meta-analysis, comprehensive reports).

```
1. Planner decomposes mission
2. [Domain-Expert validates decomposition]
3. [Researcher-A..N] gather sources in parallel
4. Integration merges research
5. [Fact-Checker] validates all claims
6. [Executor-A..N] draft sections in parallel
7. Integration merges sections
8. [Critic] reviews complete draft
9. Executor revises based on criticism
10. Editor polishes and formats
11. [Fact-Checker] final verification
12. Output
```

Use when: Accuracy target > 0.9, mission is complex, stakes are high.

## Task Decomposition Rules

1. **Single Responsibility**: Each subtask has one clear output and one success criterion.
2. **Independence Maximize**: Favor parallel subtasks over sequential when possible.
3. **Verifiable Boundaries**: Every subtask must have a verifiable completion condition.
4. **No Overlap**: Subtasks must not duplicate work; use Integration for merging.

Decomposition template:

```
Subtask [ID]: [Name]
- Input: [required inputs]
- Output: [expected output]
- Success: [verifiable completion condition]
- Dependencies: [IDs of prerequisite subtasks, or "none"]
- Assigned: [Agent Role]
```

## Communication Protocol

Define how agents communicate:

- **Direct handoff**: Agent A finishes, passes output to Agent B. Use for sequential steps.
- **Shared context**: All agents read from/write to a common state. Use for parallel steps.
- **Structured format**: Enforce a template for inter-agent communication (JSON, markdown sections).

## Accuracy Assurance

To achieve accuracy > 0.9:

1. **Redundant verification**: Critical claims checked by 2+ Fact-Checkers.
2. **Source traceability**: Every factual statement must cite its source.
3. **Explicit confidence**: Each agent reports confidence level (high/medium/low) for outputs.
4. **Adversarial review**: Critic role challenges weakest parts of the output.
5. **Final gate**: Editor checks against original mission requirements before output.

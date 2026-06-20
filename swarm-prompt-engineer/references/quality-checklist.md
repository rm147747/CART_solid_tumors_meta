# Quality Assurance Checklist

Run this checklist before finalizing any swarm prompt. The swarm is ready only when all items are checked.

## Pre-Flight Checklist

### Mission Clarity
- [ ] Mission is unambiguous and has a single interpretation.
- [ ] Success criteria are defined and measurable.
- [ ] Output format is specified.
- [ ] Constraints (length, style, domain) are documented.

### Swarm Design
- [ ] Agent roles match task complexity (not too many, not too few).
- [ ] Workflow pattern is appropriate for dependencies.
- [ ] Parallel opportunities are maximized.
- [ ] No agent has conflicting responsibilities.
- [ ] Integration points are defined for parallel branches.

### Prompt Quality
- [ ] Every agent has a clear, specific prompt with input/output format.
- [ ] All prompts include quality criteria.
- [ ] Communication protocol between agents is defined.
- [ ] Error handling is specified (what happens when an agent fails).

### Verification
- [ ] Fact-Checker is included if accuracy target > 0.8.
- [ ] Source traceability is required for all factual claims.
- [ ] Critic role is included for high-stakes missions.
- [ ] Final Editor gates output against original mission.

## Quality Gates

| Gate | Accuracy Target | Required Roles | Verification Level |
|------|----------------|----------------|-------------------|
| Basic | 0.7 - 0.8 | Planner, Executor, Editor | Self-check |
| Standard | 0.8 - 0.9 | + Fact-Checker | Source tracing |
| High | 0.9 - 0.95 | + Critic, redundant Fact-Checker | Multi-source |
| Critical | > 0.95 | Full Swarm Pattern D, Domain-Expert | Adversarial review |

## Final Verification Steps

1. **Traceability test**: Can every output claim be traced to a source?
2. **Completeness test**: Does output cover 100% of mission requirements?
3. **Consistency test**: Is terminology and style uniform throughout?
4. **Accuracy test**: Have all facts been independently verified?
5. **Format test**: Does output match the required format exactly?

Swarm prompt is APPROVED only when all applicable checklist items pass.

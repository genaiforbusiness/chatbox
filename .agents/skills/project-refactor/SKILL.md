---
name: project-refactor
description: >-
  Guidelines for the Experimentation & Refactoring stage: git branching workflow,
  template for EXPERIMENT_LOG.md, and optional advanced feature implementations (RAG, Caching, Agents).
---

# Experimentation & Refactoring Guide

This skill helps your team manage prompt tuning, code refactoring, and optional advanced feature implementations.

## 1. Deliverables Checklist

### 1. Refacotored Application Code
- Modularized, clean code separating UI and AI generation logic.
- Optimized performance, type safety (using Pydantic models for structured output), and error boundaries.

### 2. The Experiment Log: `EXPERIMENT_LOG.md`
Create a file named `EXPERIMENT_LOG.md` and document at least **three** distinct experiments.

#### Git Branching Requirement
For each experiment, use a separate Git branch:
```bash
# Create branch
git checkout -b experiment/my-test-name
# Make changes and commits
# Evaluate. If successful, merge to main:
git checkout main
git merge experiment/my-test-name
```

#### Experiment Log Template
For each experiment, use this template in `EXPERIMENT_LOG.md`:
```markdown
### Experiment #X: [Title]

* **Git Branch**: `experiment/[branch-name]`
* **Hypothesis**: What were you trying to improve, and what change did you think would work?
* **Method**: What specific change did you make on this branch?
* **Evaluation**: How did you measure the result? Provide "before" and "after" output examples.
* **Decision**: Did you merge this branch into main? Why or why not?
```

### 3. Advanced Features (Optional for "A" Grade)
If pursuing the "Advanced Path", implement at least one of these and document it as an experiment in your log:
- **Retrieval-Augmented Generation (RAG)**: Search and answer from specific uploaded documents.
- **Context Caching**: Reduce latency and costs for large, static contexts.
- **Basic Agent**: Connect external tools (e.g. calculator, API calls) for the model to use.

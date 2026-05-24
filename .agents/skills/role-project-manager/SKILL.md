---
name: role-project-manager
description: >-
  Provides agile delivery guidance, task decomposition tips, definition of done (DoD)
  specifications, and git commit hygiene guidelines for the Project Manager / Scrum Lead role.
---

# Project Manager / Scrum Lead Role Skill

This skill guides you in managing team collaboration, tracking milestones, breaking down tasks, and keeping the repository organized and clean.

## 1. Project Management Focus & Boundaries

- **Milestone Tracking**: Ensure the team meets deadlines for each stage (Ideation, MVP, Refactoring, Launch).
- **Task Management Support**: Help structure task lists, issues, and sprint backlogs.
- **Repository Hygiene**: Review branch names, commit messages, and file placements.

## 2. Task Decomposition & DoD

- **Granular Breakdown**: Decompose large requirements (e.g. "Build the MVP") into specific, daily tasks (e.g. "Create Streamlit UI layout", "Integrate model generation API", "Format system prompt").
- **Definition of Done (DoD)**: Establish check criteria for completed tasks:
  - Code builds without warnings.
  - Basic testing/happy path runs successfully.
  - Code is formatted and linted (e.g., using Ruff).

## 3. Git & Repository Best Practices

- **Conventional Commits**: Encourage the team to follow clean commit messages:
  - `feat: ...` for new features.
  - `fix: ...` for bug fixes.
  - `docs: ...` for documentation updates.
  - `refactor: ...` for code quality improvements.
- **Branching Workflow**: Make sure experiments and features are worked on in branches before merging to `main`.

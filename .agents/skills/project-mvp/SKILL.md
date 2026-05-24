---
name: project-mvp
description: >-
  Guidelines for the MVP milestone deliverables: functional Streamlit code,
  MVP_RETROSPECTIVE.md (governance/challenges), and AI_COLLABORATION_LOG.md (tools/prompts).
---

# MVP Deliverable Guide

This skill helps you verify and prepare your Minimum Viable Product (MVP) and supporting documentation for submission.

## 1. Deliverables Checklist

### 1. Functional MVP Code
- The core Streamlit application (`app.py`) must be fully functional.
- It must demonstrate the primary user stories from your project charter.
- Use `uv` for python dependencies and ensure secrets are managed via environment variables.

### 2. The MVP Retrospective: `MVP_RETROSPECTIVE.md`
Create this file in the root directory and answer:
- **Governance in Action**: Did you follow your `GOVERNANCE.md` protocol? What worked, and what needs to change?
- **Challenges & Learnings**: What was the biggest technical/conceptual hurdle you faced, and how did you resolve it?

### 3. The AI Collaboration Log: `AI_COLLABORATION_LOG.md`
Create this file to document your team's partnership with AI:
- **Section 1: Tool Manifest**: List the 2-3 primary AI tools used (e.g. Copilot, AI Studio, agy). Describe why and how you used them.
- **Section 2: Application Prompts**: Provide the full text and design rationale for the **two** most critical prompts running *inside* your application.
- **Section 3: Process Prompts**: Provide 1-2 examples of high-impact prompts used to help with your development *process* (e.g., brainstorming, debugging).

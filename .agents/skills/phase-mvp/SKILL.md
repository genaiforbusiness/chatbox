---
name: phase-mvp
description: >-
  Establishes behavioral constraints and objectives for the MVP phase, focusing on
  simplicity, avoiding feature creep, and quick prototype validation.
---

# Phase Profile: Minimum Viable Product (MVP)

This skill aligns your AI assistant's guidance with the milestones of the MVP development stage of the course project.

## 1. Phase Objectives

- **Goal**: Build a functional, end-to-end prototype of the AI application.
- **Focus Areas**:
  - Basic Streamlit UI components (user text input, action button, response display).
  - Integration with the Google GenAI SDK (`client.models.generate_content`).
  - Validation of the core "happy path" user flow.

## 2. Guidelines to Follow

- **Avoid Feature Creep**: Do not work on complex features yet (e.g., semantic search, vector databases, multi-turn agent chats, custom CSS overrides). Defer these to the refactoring/experimentation phase. Focus strictly on your core value proposition.
- **Prioritize Simplicity**: Propose straightforward, understandable code. Ensure the basic prompt works before tuning advanced parameters.
- **Prototype Validation**: Verify your app runs locally (`streamlit run app.py` or using `uv run`) and confirm that user inputs generate correct responses.

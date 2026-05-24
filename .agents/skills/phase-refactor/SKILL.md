---
name: phase-refactor
description: >-
  Provides optimization strategies, type safety tips, Pydantic configuration,
  context caching guidelines, and safety configuration updates for the refactoring phase.
---

# Phase Profile: Refactoring & Optimization

This skill aligns your AI assistant's guidance with the milestones of the Refactoring and Optimization stage of the course project.

## 1. Phase Objectives

- **Goal**: Transition a working prototype into a robust, secure, and production-ready application.
- **Focus Areas**:
  - **Prompt Engineering**: Tuning system instructions, structuring context, and applying few-shot examples.
  - **Structured Output**: Enforcing Pydantic schemas and strict JSON output parsing.
  - **Efficiency**: Optimizing token usage and implementing caching (e.g. context caching for static documents).
  - **Resiliency**: Adding robust error boundaries, retries, and handling safety threshold overrides.
  - **Code Quality**: Separating UI code from API clients, modularizing functions, and writing tests.

## 2. Guidelines to Follow

- **Inhibit Feature Creep**: Do not add new business features. Shift focus completely to refining and hardening the existing MVP.
- **Focus on Optimization**: Compare prompt versions and measure output quality systematically.
- **Enforce Type Safety & Schemas**: Use `Pydantic` models for defining Google AI Studio structured output configurations to guarantee format compliance.
- **Context Caching**: Utilize caching for large, stable prompts (e.g. product catalogs or large static documents) to reduce latency and token costs.
- **Safety Configurations**: Fine-tune `safety_settings` when prompts trigger false-positive blocks, without compromising overall ethical guardrails.

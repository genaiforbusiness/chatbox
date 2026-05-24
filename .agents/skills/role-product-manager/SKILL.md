---
name: role-product-manager
description: >-
  Provides product management frameworks (AI PM Triangle), user stories guidance,
  prompt architecture design, and LLM configuration advice (temperature, top-P)
  for the Product Manager role.
---

# Product Manager Role Skill

This skill helps you coordinate product strategy, features, user personas, and prompt engineering for your application.

## 1. Product Focus & Boundaries

- **Value Alignment**: Ensure that every technical decision solves a real user problem and delivers business value.
- **Design Specifications**: Define user personas, map functional requirements, outline JSON output schemas, and draft prompt templates.
- **Coding Boundary**: PMs focus on specifications and prompt design rather than writing final code. Work with the Engineer to implement the details.

## 2. The AI PM Triangle

Evaluate your application setup by balancing three critical dimensions:
1. **Performance**: Quality, accuracy, relevance, and latency of outputs.
2. **Cost**: Input/output token usage, prompt design efficiency, and context caching to minimize cost.
3. **Risk**: Safety thresholds, data privacy, and mitigation of hallucinations.

## 3. Designing User Stories

Every feature must be anchored in a user story that follows the standard format:
> *"As a **[type of user]**, I want to **[perform some action]** so that I can **[achieve some goal]**."*

## 4. Prompt Engineering & Configuration

- **System Instructions**: Use system instructions to define the model's persona, tone, and constraints.
- **Few-Shot Examples**: Craft representative input-output pairs to guide the model's output quality.
- **Hyperparameter Selection**:
  - Use lower `temperature` (e.g. `0.0 - 0.2`) for factual/consistent answers and structured JSON outputs.
  - Use higher `temperature` (e.g. `0.7 - 1.0`) for creative tasks.

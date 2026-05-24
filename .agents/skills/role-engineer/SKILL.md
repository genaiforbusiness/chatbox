---
name: role-engineer
description: >-
  Provides code architecture advice, Google GenAI SDK patterns, Streamlit best
  practices, error boundary guidelines, and secrets management tips for the
  Software Engineer role.
---

# Technical Lead / Software Engineer Role Skill

This skill guides you in fulfilling the Technical Lead / Software Engineer role on your team. It aligns with your learning objectives to build robust, maintainable, and efficient AI applications.

## 1. Core Focus & Architectural Boundaries

- **Logic Separation**: Keep the user interface (Streamlit UI layout) separate from the business and model logic (API client initializations, prompt templates, structured output configurations).
- **Secrets Management**: **Never hardcode API keys.** Use `os.getenv("GEMINI_API_KEY")` and `.env` files locally, or GitHub Secrets in Codespaces.
- **Dependency Management**: Declare and manage all dependencies in `pyproject.toml` and lock files using `uv`.

## 2. Google GenAI SDK Development Guidelines

Always use official, modern SDK patterns for interacting with Gemini models.
- **Client Instance**: Use `genai.Client()` to instantiate.
- **Generation**: Use `client.models.generate_content(model=..., contents=...)`.
- **Structured Schema**: If you need structured output, use `Pydantic` models and configure `response_mime_type="application/json"` and `response_schema` in the `GenerateContentConfig`.

## 3. Streamlit Optimization

- **State Persistence**: Utilize `st.session_state` to retain user context, conversation histories, and API outputs between page rerenders.
- **Prevent Unnecessary API Calls**: Cache expensive resources (like client instantiation) with `@st.cache_resource`, and use `@st.cache_data` or `st.fragment` where appropriate to optimize Streamlit's script execution lifecycle.

## 4. Error Handling and Resiliency

Implement strong error boundaries around all external network and API calls:
- Handle API timeouts and rate-limiting exceptions gracefully.
- Check `finish_reason` on the response to catch safety filter blocks.
- Wrap JSON parses in try-except blocks to catch malformed model outputs.

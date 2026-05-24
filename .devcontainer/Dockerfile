FROM python:3.13-slim-bookworm

# Install required system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install uv for Python dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_LINK_MODE=copy

# Create a non-root vscode user to run commands securely
RUN useradd -m -s /bin/bash vscode

# Install Antigravity CLI (agy) for the vscode user
RUN su vscode -c "curl -fsSL https://antigravity.google/cli/install.sh | bash"

# Add the Antigravity CLI binary directory to PATH for the vscode user
ENV PATH="/home/vscode/.local/bin:${PATH}"

# Default container execution user
USER vscode

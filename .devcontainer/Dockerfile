FROM mcr.microsoft.com/devcontainers/python:3.13 

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

ADD https://astral.sh/uv/0.8.10/install.sh /uv-installer.sh

RUN sh /uv-installer.sh && rm /uv-installer.sh 

ARG EXTRA_NODE_VERSION=22
RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && nvm install ${EXTRA_NODE_VERSION} && npm install -g @google/gemini-cli" 2>&1 

ENV PATH="/root/.local/bin/:$PATH"
# GenAI for Business - Course Sandbox

Welcome to the sandbox repository for **BUSBIS 1530: Technical Foundations of Generative AI for Business**. This repository provides a pre-configured development environment inside **GitHub Codespaces** to let you start building, testing, and collaborating with Generative AI immediately.

---

## 🚀 Getting Started Sequence

Follow these steps to set up your environment:

### Step 1: Obtain a Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Create or log in with your Google account.
3. Click **Get API Key** and generate a new key. Copy this key somewhere secure.

### Step 2: Create Your Private Repository
1. Navigate to the course template: [https://github.com/genaiforbusiness/chatbox](https://github.com/genaiforbusiness/chatbox).
2. Click **Use this template** > **Create a new repository**.
3. Set your repository name to `ai-poc-team-<your-team-name>` (e.g. `ai-poc-team-innovators`).
4. **Select "Private"** (this is critical for academic integrity).
5. Click **Create repository**.
6. Under **Settings** > **Collaborators**, add your teammates and the instructor (`midhubalan`).

### Step 3: Save the API Key in GitHub Secrets
To make the key automatically available in your development environment, save it as a Codespaces secret:
1. Go to your personal GitHub settings (click your profile photo in the top right > **Settings**).
2. In the left sidebar, click **Codespaces** (under the *Developer* section).
3. Under **Codespaces secrets**, click **New secret**.
4. Set the **Name** to `GEMINI_API_KEY`.
5. Paste your API key in the **Value** box.
6. Under **Repository access**, grant access to your new private team repository.
7. Click **Add secret**.
*(Optional: If you are using Vertex AI/GCP resources, repeat the steps to save your `GOOGLE_API_KEY`.)*

> [!IMPORTANT]
> **API Key is Only for Streamlit:**
> The `GEMINI_API_KEY` is **only** required to run the Streamlit web application (`app.py`).
> The Antigravity CLI (`agy`) **does not** require an API key; it authenticates directly using your Google account (via OAuth/OIDC).
>
> **Configuring the Key for Streamlit:**
> - **In Codespaces:** Save `GEMINI_API_KEY` as a Codespaces secret in your GitHub account settings and grant repository access (see [GitHub Codespaces Secrets Documentation](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces)).
> - **In Local Development:** Create a `.env` file in the root of your project directory and add:
>   ```bash
>   GEMINI_API_KEY="your_actual_api_key_here"
>   ```

> [!WARNING]
> **Never Commit Keys:** Do not commit API keys or `.env` files to GitHub. The `.gitignore` file is pre-configured to ignore `.env` files.

### Step 4: Launch Your Codespace
1. Navigate to your newly created private repository on GitHub.
2. Click the green **Code** button.
3. Select the **Codespaces** tab and click **Create codespace on main**.
4. The Codespace environment will build and load directly in your web browser.

---

## 🛠️ Running the Application & CLI

### 1. Launch the Streamlit App
This repository includes a starter Streamlit web application. Open a terminal in Codespaces (`Terminal` > `New Terminal`) and run:
```bash
# Install dependencies & create virtual environment
uv sync

# Run the Streamlit web server
uv run -- streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false
```

> [!CAUTION]
> The flags `--server.enableCORS false` and `--server.enableXsrfProtection false` disable specific cross-origin and request verification checks. This is required for Streamlit to render securely inside the GitHub Codespaces proxy. **Do not use these flags in a production environment.**

### 2. Launch the Antigravity CLI (`agy`)
> The **Antigravity CLI** is an interactive AI-powered agent running in your terminal that helps you code, refactor, and manage your project. 
> 
> > [!NOTE]
> > The `agy` tool authenticates via your Google account using OAuth. It **does not** use your `GEMINI_API_KEY` secret.
> 
> To start the CLI, run:
> ```bash
> agy
> ```
> On your first run, a URL and a code will be displayed in the terminal. Open the link, sign in with your Google account, and enter the code to authorize the CLI.

---

## 🧠 Workspace Skills

This repository is pre-loaded with **workspace skills** located in `.agents/skills/`. When you run `agy` in your workspace, the agent automatically detects these skills and uses them to assist you. 

| Skill Command | Skill Name | Description / Guidance |
| :--- | :--- | :--- |
| `/project-advisor` | **Course Advisor** | Onboards you to the workspace, explains deliverables, and maps out next steps. |
| `/project-bootstrap` | **Bootstrap Guide** | Step-by-step git commands and instructions for initial repository setup. |
| `/project-charter` | **Project Charter Guide** | Requirements for `README.md`, `USER_STORIES.md`, and `GOVERNANCE.md`. |
| `/project-mvp` | **MVP Deliverable** | Requirements for your MVP code, retrospective, and collaboration log. |
| `/project-refactor` | **Refactoring Guide** | Instructions for git branching, experiment logging, and advanced features. |
| `/project-launch-kit` | **PoC Launch Kit** | Outline for the video pitch, quick-start guide, and final team reflection. |
| `/project-individual-contribution` | **Individual Contribution** | Guidelines on task management, git workflow, and peer collaboration. |
| `/project-peer-review` | **Peer Review Guide** | Rubrics and templates for reviewing other teams' launch kits. |
| `/role-engineer` | **Software Engineer** | Architecture guidelines, type safety, Streamlit cache optimization. |
| `/role-product-manager`| **Product Manager** | Framing value, writing user stories, prompt configuration (temp, top-P). |
| `/role-project-manager`| **Scrum Lead** | Task decomposition, Definition of Done, commit hygiene. |
| `/phase-mvp` | **MVP Phase** | Guidance to avoid feature creep and maintain clean prototype simplicity. |
| `/phase-refactor` | **Refactoring Phase** | Focuses on context caching, structured schemas, and performance tuning. |

---

## 🏁 Next Steps

To begin your project:
1. Open a new terminal in your Codespace.
2. Start the CLI by running `agy`.
3. Type `/project-advisor` or ask the assistant:
   > *"I'm just starting the project. What should my team do first?"*
4. The assistant will load the `project-advisor` and `project-bootstrap` skills to guide your setup!

---

## 💬 Sample Agent Interaction

Here is an example of what to expect when interacting with the Antigravity agent using workspace skills:

**Student Prompt:**
> "I'm assuming the role of Product Manager for this sprint. Can you help me draft a user story for our chatbot's user authentication?"

**Antigravity Response (utilizing `/role-product-manager`):**
> 📥 *Loaded skill: role-product-manager*
>
> As a Product Manager, I'd be glad to help you draft this user story. Let's frame this from the perspective of our target user to ensure we capture the value clearly, without getting bogged down in the database schemas or coding details (which our Tech Lead will handle).
> 
> Let's structure this using our standard PM format:
> 
> **Epic:** User Account Management
> **User Story:**
> > **As a** return user of the AI application,
> > **I want to** securely log in using my Google account,
> > **so that** I can retrieve my saved chat history and preferences.
> 
> **Acceptance Criteria (for our Technical Lead):**
> 1. User can click a "Sign in with Google" button on the sidebar.
> 2. On successful login, the UI greets the user by name.
> 3. If authentication fails, a clear error message is shown without revealing sensitive system details.
> 
> **Next Step Recommendation:** Let's discuss what parameters we should set for this authentication flow (e.g. timeout settings) to keep cost and risk low, in line with the **AI PM Triangle**. Would you like me to help you draft the GitHub issue for this?

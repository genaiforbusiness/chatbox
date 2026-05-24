---
name: project-bootstrap
description: >-
  Detailed git instructions and checklist for repository creation, cloning,
  adding collaborators, creating individual profile files, committing, and pushing.
---

# Project Bootstrap Guide

Use this skill to guide you through setting up your team's private repository and submitting your initial profile page contribution.

## 1. Step-by-Step Instructions

### Step 1: Create the Private Repository (Repo Lead)
- Go to the template repository: [https://github.com/genaiforbusiness/chatbox](https://github.com/genaiforbusiness/chatbox).
- Click **"Use this template"** > **"Create a new repository"**.
- Name your repository using the format: `ai-poc-team-<your-team-name>` (e.g. `ai-poc-team-innovators`).
- **MUST SELECT PRIVATE**.
- Click **"Create repository"**.
- Go to **Settings** > **Collaborators** and add:
  - All team members.
  - The instructor: `midhubalan`.

### Step 2: Clone the Repository (Everyone)
Run the following command in your terminal to clone the repo:
```bash
git clone <your-repository-https-url>
```

### Step 3: Create Your Profile Page (Everyone)
- Inside the repository root, create a file named exactly `<your-github-username>.md` (e.g. `j-doe.md`).
- Add the following content:
  ```markdown
  # [Your Name]

  **Major:** [Your Major]

  **What I want to learn in this course:** [A brief sentence about your goals]

  **A fun fact about me:** [Something interesting!]
  ```

### Step 4: Commit and Push Changes (Everyone)
Run these commands in your project folder terminal:
```bash
git add <your-github-username>.md
git commit -m "feat: Add profile for <your-github-username>"
git push
```

## 2. Submission Verification
Ensure that:
- [ ] The repository is set to **private**.
- [ ] Teammates and the instructor (`midhubalan`) accepted the invitations.
- [ ] Everyone's `<username>.md` file exists in the repo.

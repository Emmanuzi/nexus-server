# Contributing Guidelines

Thank you for contributing to the Simple Python Web Server project.

This document explains the workflow, branching strategy, coding standards, and how to run the project locally.

**All contributors should read this file before starting any work.**

## 1. Branching Strategy

We follow a Git Flow–style workflow:

### Main Branch

- The `main` branch contains stable, production-ready code.
- Nobody pushes directly to `main`.

### Develop Branch

- The `develop` branch is where active development happens.
- All feature branches must be created from `develop`.

### Feature Branches

Each new feature or task should have its own branch:

```
feature/<feature-name>
```

**Examples:**

- `feature/file-serving`
- `feature/directory-listing`
- `feature/cgi-support`

When your feature is ready:

1. Push your branch.
2. Open a Pull Request (PR) into `develop`.
3. Wait for review and approval.

## 2. How to Contribute Code

### Step 1 — Create a Feature Branch

From `develop`:

```bash
git checkout develop
git pull
git checkout -b feature/<feature-name>
```

### Step 2 — Make Changes

- Write clean, readable Python 3 code.
- Add comments explaining functions if needed.
- Since we are beginners we are encouraged to ask questions.

### Step 3 — Commit Your Work

Use meaningful commit messages:

```bash
git add .
git commit -m "Implement directory listing feature"
```

**Avoid commits like "fix", "changes", "update".**

### Step 4 — Push Your Branch

```bash
git push -u origin feature/<feature-name>
```

### Step 5 — Create a Pull Request

1. Go to GitHub → Pull Requests → New PR
2. Set:
   - **Base branch:** `develop`
   - **Compare branch:** your feature branch
3. Add a short description of what you did.
4. Assign the reviewer (project lead).

## 3. Code Review Rules

- All PRs must be reviewed before merging.
- Reviewers should check:
  - Code readability
  - Proper folder placement (`server.py`, `handlers/`, `www/`)
  - Python 3 compatibility
  - No unused files or unnecessary prints
  - Feature works as expected
  - No merge conflicts

If changes are needed:

1. Reviewer leaves comments
2. Contributor updates the branch
3. Reviewer approves and merges to `develop`

## 4. Folder Structure to Follow

```
simple-web-server/
│
├── server.py
├── handlers/
│   ├── base_case.py
│   ├── case_no_file.py
│   ├── case_existing_file.py
│   ├── case_directory.py
│   ├── case_cgi.py
│
├── www/
│   ├── index.html
│   └── (other static files)
│
└── README.md
```

**Do not create random files outside these directories.**

## 5. Python Version

All contributors must use:

- **Python 3.x**

The tutorial provided uses older Python 2 syntax, but this project must be updated to Python 3 standards.

## 6. Running the Server Locally

After cloning the repo:

```bash
python3 server.py
```

Then visit in browser:

```
http://localhost:8080
```

## 7. Communication Rules

- Ask questions if something is unclear.
- Always discuss big changes before starting them.
- Use emoji or comments inside PRs for clarity (optional but fun).
- Respect each other, we're here to learn and grow.

## 8. Done? Open an Issue!

If you:

- Found a bug
- Have an idea
- Need clarification

Open a GitHub issue.

Use clear titles like:

- `Bug: Directory listing shows wrong files`
- `Task: Add 404 error handler`

---

Happy Coding!

Let's build something great together!

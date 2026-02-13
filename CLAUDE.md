# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal tech card website project - a simple single-page static website showcasing:
- Name and title (e.g., "Name - AI Engineer")
- Personal bio
- Skills list
- Project links (GitHub repositories)
- Contact info (GitHub/LinkedIn)

## Tech Stack

- **Code Generation**: Python script to generate static HTML (no web framework)
- **Version Control**: Git & GitHub
- **CI/CD**: GitHub Actions
- **Deployment**: GitHub Pages
- **Project Management**: GitHub Issues

## Project Structure

Based on the project plan, the expected structure is:

```
my_dev_card/
├── build_page.py      # Python script that generates index.html
├── index.html        # Generated static HTML file
├── .github/
│   └── workflows/
│       └── deploy.yml # GitHub Actions workflow for CI/CD
└── project.md         # Project plan (tutorial document)
```

## Common Commands

```bash
# Generate the HTML page locally
python build_page.py

# The script creates index.html in the project root
```

## Development Workflow

1. Create a feature branch for each task: `git checkout -b feature/<feature-name>`
2. Make changes and commit with descriptive messages
3. Create a Pull Request for review
4. Merge to `main` branch to trigger GitHub Actions deployment

## Deployment

When code is merged to `main` branch, GitHub Actions automatically:
1. Checks out the code
2. Runs `python build_page.py` to generate HTML
3. Deploys to GitHub Pages at `https://<username>.github.io/<repo-name>/`

## Notes

- This is a beginner-friendly project focused on learning CI/CD and GitHub Pages deployment
- The Python script reads personal information and generates static HTML - no database or backend required

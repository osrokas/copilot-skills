# COPILOT SKILLS

# Description
This repository contains a collection of skills for Copilot, an AI-powered code completion tool developed by GitHub. Each skill is designed to help developers automate specific tasks and improve their productivity when using Copilot.

## Prerequisites
To use the skills in this repository, you will need to have the following prerequisites:
- A GitHub account
- Git installed on your local machine
- The GitHub CLI tool (gh) installed on your local machine
- The Copilot CLI installed on your local machine [Copilot CLI installation guide](https://github.com/features/copilot/cli)
- Python installed on your local machine (for the python-project skill)

# Setup
1. For GitHub Copilot, you should create a skills folder under your .copilot directory.
 - On Windows: `C:\Users\<YourUsername>\.copilot\skills`
 - On macOS/Linux: `~/.copilot/skills`

2. Clone this repository into the skills folder you just created:
```bash
cd ~/.copilot/skills
git clone <repository-url>
``` 

# Usage
- List all available skills:
    ```bash
    copilot
    /skills list
    ```
- Run a specific skill:
    ```bash
    copilot
    /<skill-name> <prompt text>


# Skills
- [python-project](python-project/SKILL.md): A skill to create a Python project based on a given description. The generated project includes a `docs/project_description.pdf` file with an overview of the project name, description, structure, and getting-started instructions.

## Example project structure

Running the `python-project` skill produces a GitHub repository with the following layout:

```
<project-name>/
|-- docs/
|   |-- project_description.pdf   <- auto-generated PDF describing the project
|-- notebooks/
|-- src/
|-- .gitignore
|-- generate_docs.py
|-- requirements.txt
|-- README.md
```

The PDF is generated automatically during project setup using the [fpdf2](https://py-pdf.github.io/fpdf2/) library and committed together with the rest of the project files so that anyone who clones the GitHub repository immediately has the project documentation available.

## Live example

A fully-generated example project is available in this repository under [`examples/sample-data-project/`](examples/sample-data-project/). It includes:

- [`docs/project_description.pdf`](examples/sample-data-project/docs/project_description.pdf) — the auto-generated PDF project description
- [`generate_docs.py`](examples/sample-data-project/generate_docs.py) — the script used to produce the PDF
- The standard `src/`, `notebooks/`, `requirements.txt`, `.gitignore` scaffold

You can browse the example directly on GitHub to see exactly what the skill produces.


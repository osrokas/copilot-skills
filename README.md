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
- [python-project](python-project/SKILL.md): A skill to create a Python project based on a given description.


---
name: python-project
description: A skill to create a Python project based on a given description.
---

To create a Python project, follow this process:

1. Create a folder in the current dir with project name based on prompt.
2. Create all directories, subdirectories and files defined in template folder.
3. In command line execute git init in the project folder to initialize a git repository.
4. Create a virtual environment for the project using `python -m venv .venv` and activate it.
5. Install project dependencies using `pip install -r requirements.txt`.
6. In .gitignore file add lines to ignore .venv and __pycache__/ folders.
7. Generate a PDF description of the project by running the following command inside the project folder:
   python generate_docs.py "[project-name]" "[project description from prompt]"
   This will create docs/project_description.pdf with an overview of the project.
8. Create GitHub repository with the same name as project and push the code to the repository using following command:
   gh repo create [project-name] --description "[project description from prompt]" --public
9. Execute following commands to push code to GitHub repository:
   git add .
   git commit -m "Initial commit"
   git branch -M master
   git remote add origin git@github.com:osrokas/[project-name].git
   git push -u origin master
10. At the end print "Project [project name] created successfully."

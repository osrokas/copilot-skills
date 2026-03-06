---
name: python-project
description: A skill to create a Python project based on a given description.
---

To create a Python project, follow this process:

1. Create not folder in the current dir with project name based on prompt
2. Create all directories, subdirectories and files defined in template folder.
3. In command line execute git init in the project folder to initialize a git repository.
4. create a virtual environment for the project using `python -m venv .venv` and activate it.
5. In .gitignore file add lines to ignore .venv and __pycache__/ folders.
6. Create github repository with the same name as project and push the code to the repository using following command:
   gh repo create [project-name] --description "repository on GitHub." --public
7. Exeute following command to push code to github repository:
   git add .
   git commit -m "Initial commit"
   git branch -M master
   git remote add origin git@github.com:osrokas/[project-name].git
   git push -u origin master
8. At the end print "Project [project name] created successfully.

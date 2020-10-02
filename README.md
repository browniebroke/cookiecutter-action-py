# Cookiecutter Python Action

A cookiecutter template for generating Github actions running Python

## Features

- CI powered Github actions.
- Dependabot pre-configured.
- Comes with a set of pre-commit hooks.
- Follow the conventional commits specification. 
- Releasing automated with python-semantic-release.

## Quick start

### Pre-requisites

Make sure that you have the cookiecutter command line interface installed:

```shell script
cookiecutter --version
```

If this is not the case, install it first.

### Usage

To create a project for a Python powered Github action:

```shell
> cookiecutter https://github.com/browniebroke/cookiecutter-action-py
author_name [Bruno Alla]: 
email [alla.brunoo@gmail.com]: 
github_username [browniebroke]: 
name [Github Action Python]: 
hyphenated_name [github-action-python]: 
description [A Github Action to run some Python code]: 
Select branding_color:
1 - white
2 - yellow
3 - blue
4 - green
5 - orange
6 - red
7 - purple
8 - gray-dark
Choose from 1, 2, 3, 4, 5, 6, 7, 8 [1]:
```

The project should live in a directory named after the answer you gave for the `hyphenated_name`, this should match your Github repo name.

### Next steps

- You code goes in `src/app.py`
- If your action needs inputs, you need to declare them in `action.yml` and get their values from the environment in `app.py`. 
  An example input for `something` is commented out in both files.
- Create a virtualenv
- Install the dependencies
- Commit and push to the Github repo.

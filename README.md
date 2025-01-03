# Cookiecutter Python Action

<p align="center">
  <a href="https://github.com/browniebroke/cookiecutter-action-py/actions/workflows/ci.yml?query=branch%3Amain">
    <img alt="CI Status" src="https://img.shields.io/github/actions/workflow/status/browniebroke/cookiecutter-action-py/ci.yml?branch=main&label=CI&logo=github&style=flat-square">
  </a>
  <a href="https://results.pre-commit.ci/latest/github/browniebroke/cookiecutter-action-py/main">
    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/browniebroke/cookiecutter-action-py/main.svg">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/cookiecutter/cookiecutter">
    <img src="https://img.shields.io/badge/cookiecutter-template-D4AA00.svg?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPCAYAAAA/I0V3AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAADHSURBVHgBlZKBDcIgEEVhA0fQCewIOEE7ghvoCN2gOgFugBNInMANxA10As9/tpiTQJv+5JVA/i/cgVJCRLQAO+DBk3rx6IBRqbBYgTCYYiCV5R/HwFIYDWiorHMMhYKBj3oTc//dCZ8tlWVE6CRr8TStNm2ALNpljrrPdS3KDnPZBKdyEjt1YJPZqQUaqLk1sWf1C9L4nUiFNHiZEazki7gXjAf6r9PK2mLwnYRq6pvB6x17daabDYYarAE/zhe4gqPW+sGeD9vRPwSlHFC8AAAAAElFTkSuQmCC" alt="cookiecutter">
  </a>
</p>

A cookiecutter template for generating Github actions running Python

## Features

- CI powered Github actions.
- Dependencies managed by [Poetry]
- Pre-configured with [Renovate].
- Comes with a set of [pre-commit] hooks.
- Follow [the conventional commits][conventional-commits] specification.
- Releasing automated with [python-semantic-release][psr].

## Quick start

### Pre-requisites

Make sure that you have the [cookiecutter][cc-rtd] command line interface installed:

```shell script
cookiecutter --version
```

If this is not the case, install it first. Check out [their documentation][cc-install] for the most up to date info for your platform.

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

The generated project will live in a directory named after the answer you gave for the `hyphenated_name`, this should match your Github repo name.

### Next steps

- You code goes in `src/app.py`
- If your action needs inputs, you need to declare them in `action.yml` and get their values from the environment in `app.py`.
  An example input for `something` is commented out in both files.
- Create a virtualenv
- Install the dependencies
- Commit and push to the Github repo.

[poetry]: https://github.com/astral-sh/uv
[renovate]: https://docs.renovatebot.com/
[pre-commit]: https://pre-commit.com/
[conventional-commits]: https://www.conventionalcommits.org
[psr]: https://github.com/relekang/python-semantic-release
[cc-rtd]: https://cookiecutter.readthedocs.io
[cc-install]: https://cookiecutter.readthedocs.io/en/latest/installation.html

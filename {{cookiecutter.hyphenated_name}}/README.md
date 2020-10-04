# {{ cookiecutter.name }}

<p align="center">
  <a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated_name }}/actions?query=workflow%3ACI">
    <img alt="CI Status" src="https://img.shields.io/github/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated_name }}/CI?label=CI&logo=github&style=flat-square">
  </a>
  <a href="https://github.com/ambv/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?amp;style=flat-square" alt="black">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>

{{ cookiecutter.description }}.

## Usage

Example of workflow using this action:

```yaml
name: {{ cookiecutter.name }}

on:
  pull_request:

jobs:
  example:
    runs-on: ubuntu-latest

    steps:
      - uses: {{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated_name }}@main
        with:
          github_token: {% raw %}${{ secrets.GITHUB_TOKEN }}{% endraw %}
```

## Credit

This project was generated via [Cookiecutter](https://github.com/cookiecutter/cookiecutter) using [Python Action template](https://github.com/browniebroke/cookiecutter-action-py).

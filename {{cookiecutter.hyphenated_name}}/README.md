# {{ cookiecutter.name }}

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

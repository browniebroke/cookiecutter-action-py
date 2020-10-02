from environs import Env
from github import Github, UnknownObjectException

env = Env()


def main(github_token: str, github_repository: str) -> None:
    """
    Script entry point.

    :param github_token: Github token.
    :param github_repository: The owner and repository name (octocat/Hello-World).
    """

    gh = Github(login_or_token=github_token)
    repo = gh.get_repo(github_repository)
    print(f"Hello from {repo}")


if __name__ == "__main__":
    env = Env()
    env.read_env()
    gh_repository = env("GITHUB_REPOSITORY")
    gh_token = env("INPUT_GITHUB_TOKEN")

    # The inputs in action.yml are passed as environment variables
    # Name is in uppercase and prefixed with `INPUT_`
    # input_something = env("INPUT_SOMETHING")

    main(gh_token, gh_repository)

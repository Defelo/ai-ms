from collections import namedtuple
from git import Repo, InvalidGitRepositoryError
from pathlib import Path

Version = namedtuple("Version", ["commit", "branch", "description"])


def get_version() -> Version:
    try:
        repo = Repo(".")  # Assumes script is run in the git repo root
        commit = repo.head.commit.hexsha
        branch = repo.active_branch.name if not repo.head.is_detached else ""
        description = repo.git.describe("--tags", "--always")

        return Version(commit, branch, description)

    except InvalidGitRepositoryError:
        # Fallback if git commands fail
        version_file_path = Path("VERSION")
        if version_file_path.exists():
            with open(version_file_path, "r") as version_file:
                version_info = version_file.read().splitlines()
                return Version(*version_info[:3])
        else:
            return Version("", "", "")


if __name__ == "__main__":
    version = get_version()
    # Write version information to VERSION file for future reference
    with open("VERSION", "w") as version_file:
        version_file.write(f"{version.commit}\n{version.branch}\n{version.description}\n")
    print(version)

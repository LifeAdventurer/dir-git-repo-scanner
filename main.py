import os
import subprocess
from collections.abc import Generator


def find_git_repositories(start_dir: str) -> Generator[str, None, None]:
    for root, dirs, _files in os.walk(start_dir):
        if ".git" in dirs:
            yield root
            dirs[:] = []


def get_remote_url(repository_path: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", repository_path, "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def main():
    start_dir = os.getcwd()
    repository_table_rows = [
        "| Repository Name | Remote URL | Repository Path |",
        "| ---- | ---- | ---- |",
    ]
    for repository_path in find_git_repositories(start_dir):
        remote_url = get_remote_url(repository_path)
        if remote_url:
            repository_name = os.path.basename(repository_path)
            repository_table_rows.append(
                f"| {repository_name} | {remote_url} | {repository_path} |"
            )

    repository_table = "\n".join(repository_table_rows)

    print(repository_table)


if __name__ == "__main__":
    main()

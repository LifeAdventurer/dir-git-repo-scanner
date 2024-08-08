import os
from collections.abc import Generator


def find_git_repositories(start_dir: str) -> Generator[str, None, None]:
    for root, dirs, _files in os.walk(start_dir):
        if ".git" in dirs:
            yield root


def main():
    start_dir = os.getcwd()
    for repository_path in find_git_repositories(start_dir):
        print(repository_path)


if __name__ == "__main__":
    main()

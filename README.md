# Directory Git Repository Scanner

This project is designed to recursively scan directories on your filesystem to identify Git repositories and output their remote URLs. This tool can be useful for developers who need to keep track of various Git repositories spread across multiple directories, ensuring that they can quickly find and manage their projects.

## Features

- **Recursive Search**: Scans all subdirectories starting from the current working directory.
- **Git Repository Detection**: Indentifies directories containing Git repositories.
- **Remote URL Fetching**: Retrieves the `origin` remote URL of each repository.
- **Tabular Output**: Displays a table listing repository names, their remote URLs, and their paths.

## Requirements

- Python 3.11+
- Git must be installed and available in the system's PATH.

## Usage

1. Clone or download the repository.
2. Run the script from your terminal:

    ```sh
    python main.py
    ```

The script will output a table of repositories found in the current working directory.

## Example Output

| Repository name | Remote URL                              | Repository Path      |
|-----------------|-----------------------------------------|----------------------|
| my-repo         | https://github.com/username/my-repo.git | path/to/my-repo      |
| another-repo    | git@github.com:username/my-repo.git     | path/to/another-repo |

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

# project-root-finder

[![PyPI version](https://badge.fury.io/py/project-root-finder.svg)](https://badge.fury.io/py/project-root-finder)
[![Python Versions](https://img.shields.io/pypi/pyversions/project-root-finder.svg)](https://pypi.org/project/project-root-finder/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A lightweight, zero-dependency Python package to **automatically locate your project root directory** by directory name or optional markers.  
Say goodbye to hardcoded `pathlib.Path(__file__).parents[1]` – just call this function from anywhere in your project.

## Features

- 🔍 **Find root by name** – specify your project's folder name (e.g. `"my_project"`)
- ✅ **Optional validation markers** – ensure the found directory contains files like `.git`, `requirements.txt`, etc.
- 🌍 **Environment variable support** – set `PROJECT_NAME` once and reuse across all files
- 🚀 **Zero third-party dependencies** – pure Python, works with `pathlib` and standard library only
- 🧠 **Cached result** – uses `functools.lru_cache` to avoid repeated filesystem scans

## Installation

### From PyPI (recommended for public usage)

```bash
pip install project-root-finder
```

### Directly from Git repository (for unreleased versions or private use)

```bash
pip install git+https://github.com/yourname/project-root-finder.git
# or with a specific tag/branch
pip install git+https://github.com/yourname/project-root-finder.git@v0.1.0
```

## Quick Start

Assume your project structure:

```
my_project/
├── src/
│   └── utils/
│       └── helper.py
├── requirements.txt
└── README.md
```

### 1. Use in any file (`helper.py`)

```python
import sys
import pathlib
from project_root_finder import find_project_root_by_name

# Automatically find the root folder "my_project"
BASE_DIR = find_project_root_by_name(
    pathlib.Path(__file__).resolve(),
    project_name="my_project"
)

sys.path.append(str(BASE_DIR))
```

### 2. With validation markers (more safety)

```python
BASE_DIR = find_project_root_by_name(
    pathlib.Path(__file__).resolve(),
    project_name="my_project",
    extra_markers=["requirements.txt", ".git"]
)
```

### 3. Use environment variable (set once, then omit `project_name`)

```bash
export PROJECT_NAME=my_project
```

```python
BASE_DIR = find_project_root_by_name(pathlib.Path(__file__).resolve())
# picks up 'my_project' from $PROJECT_NAME
```

## API Reference

### `find_project_root_by_name(start_path, project_name=None, extra_markers=None)`

- **`start_path`** (`pathlib.Path`): Always use `pathlib.Path(__file__).resolve()` – the starting file's absolute path.
- **`project_name`** (`str`, optional): Name of your project root directory. If `None`, reads from environment variable `PROJECT_NAME`. If still empty, raises `ValueError`.
- **`extra_markers`** (`List[str]`, optional): Additional files/directories that must exist in the candidate root. For example `["requirements.txt", ".git", "pyproject.toml"]`. If provided, the function returns only if **at least one** marker is present.
- **Returns** (`pathlib.Path`): Absolute path to the project root directory.
- **Raises** (`RuntimeError`): If no directory with the given name is found, or if markers are provided but none exist.

## Why not just use `pathlib.Path(__file__).parents[1]`?

- Hardcoded depth breaks when you move a file to a different nesting level.
- Need to adjust `parents[1]` → `parents[2]` every time your directory structure changes.
- `project-root-finder` finds the root **dynamically** by name, so it works from any depth.

## Contributing

Feel free to open issues or pull requests on [GitHub](https://github.com/yourname/project-root-finder).

## License

MIT © [Logan.Jin](mailto:loganjincn@gmail.com)
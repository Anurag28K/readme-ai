""" Methods to process the GitHub repository """

import contextlib
import os
import re
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import urlparse

import git

import preprocess_helper as helper
from logger import Logger

LOGGER = Logger("readme_ai_logger")


def add_space_between_sentences(text: str) -> str:
    pattern = r"([.!?])(\S)"
    return re.sub(pattern, r"\1 \2", text)


def add_values_from_dict_to_list(keys_list, input_dict):
    for key in keys_list:
        if key in input_dict:
            keys_list.append(input_dict[key])
    return keys_list


def clone_codebase(url: str) -> Dict[str, str]:
    """Clone GitHub repository to a temporary
        directory and return the file contents.

    Parameters
    ----------
    cwd_path
        cwd_path (str): current working directory path
    url
        url (str): the GitHub URL to clone

    Returns
    -------
        Dict: a dictionary mapping file paths to their contents
    """
    with make_temp_directory() as temp_dir:
        git.Repo.clone_from(url, temp_dir)
        files = get_file_contents(temp_dir)
    return files


def get_file_contents(directory: str, exclude: List[str] = []) -> Dict[str, str]:
    contents = {}
    exclude += [
        ".gitignore",
        ".md",
        "__init__.py",
        "badges",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING",
        "LICENSE",
        "README.md",
        "conf",
        "docs",
        "imgs",
        "setup",
        "setup.py",
        "tests",
    ]
    for path in Path(directory).rglob("*"):
        if path.is_file() and not any(ex in path.parts for ex in exclude):
            try:
                with path.open(encoding="utf-8") as f:
                    contents[path.relative_to(directory)] = f.read()
            except UnicodeDecodeError:
                contents[
                    path.relative_to(directory)
                ] = "Could not decode content: non-text or non-UTF-8 file"
    return contents


def get_local_codebase(local_directory: str) -> Dict[str, str]:
    repo_contents = {}
    base_path = Path(local_directory)

    for file_path in base_path.rglob("*"):
        if file_path.is_file():
            try:
                content = file_path.read_text(encoding="utf-8")
                repo_contents[str(file_path)] = content
            except UnicodeDecodeError:
                # Skip non-text files
                continue

    return repo_contents


def get_repo_name(path: Union[str, os.PathLike]) -> str:
    if "github.com" in path:
        # GitHub URL
        repo_path = urlparse(path).path
        repo_name = repo_path.split("/")[-1]
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]
    else:
        # Local path
        repo_name = os.path.basename(os.path.normpath(path))

    return repo_name


@contextlib.contextmanager
def make_temp_directory() -> str:
    try:
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)


def get_project_dependencies(
    repo: str, file_ext: List[str], file_names: List[str]
) -> List[str]:
    with tempfile.TemporaryDirectory(prefix="readme-ai-") as temp_dir:
        if "github.com" in repo:
            git.Repo.clone_from(repo, temp_dir)
        elif os.path.isdir(repo):
            shutil.copytree(repo, temp_dir)
        else:
            raise ValueError("Repository link is not valid.")

        # Get list of files from the remote or local repository
        all_files = helper.list_files(temp_dir)
        dependency_files = [f for f in all_files if Path(f).name in file_names]

        file_parsers = {
            "cargo.toml": helper.parse_cargo_toml,
            "cargo.lock": helper.parse_cargo_lock,
            "requirements.txt": helper.parse_requirements_file,
            "environment.yaml": helper.parse_conda_env_file,
            "environment.yml": helper.parse_conda_env_file,
            "Pipfile": helper.parse_pipfile,
            "pyproject.toml": helper.parse_pyproject_toml,
            "package.json": helper.parse_package_json,
            "yarn.lock": helper.parse_yarn_lock,
        }

        dependencies = []

        for f in dependency_files:
            parse_fn = file_parsers.get(Path(f).name)

            if parse_fn:
                packages = parse_fn(f)
                dependencies.append(packages)

        # Get a set of file extensions from the repository
        ext_list = list({Path(f).suffix[1:] for f in all_files})
        file_extensions = add_values_from_dict_to_list(ext_list, file_ext)
        dependencies.append(file_extensions)

        packages = sum(dependencies, [])
        packages = [p.lower() for p in packages]
        return list(set(packages))
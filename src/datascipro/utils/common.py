import os
import yaml
import json
import joblib  # For saving/loading binary files
from pathlib import Path  # Cross-platform file path handling
from typing import Any  # Generic type hinting
from box import ConfigBox  # Allows dot-access to dictionary data
from box.exceptions import BoxValueError  # Raised if box fails to parse
from ensure import ensure_annotations  # Enforces type annotations
from src.datascipro import logger  # Custom logger defined elsewhere
import yaml

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object for dot-access.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For any other exceptions during read/parse.

    Returns:
        ConfigBox: Parsed data from YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories from a list of paths.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs each directory creation.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns a ConfigBox object.

    Args:
        path (Path): Path to JSON file.

    Returns:
        ConfigBox: Data with dot-access.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves any object as a binary file using joblib.

    Args:
        data (Any): Data to save.
        path (Path): Destination path.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads binary data using joblib.

    Args:
        path (Path): Path to binary file.

    Returns:
        Any: Loaded object.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

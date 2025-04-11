"""
The tools related with file management in the OS.
"""

import os

def validate_path(path: str) -> str:
    """
    Validate the path by checking if it exists and is writable. It can be a file or a directory.
    """
    if not os.path.exists(path):
        raise ValueError(f"Path {path} does not exist.")
    if not os.access(path, os.W_OK):
        raise ValueError(f"Path {path} is not writable.")
    return path

def create_new_file(path: str, content: str = "") -> str:
    """
    Create a new file at the given path with the given content.
    """
    if os.path.exists(path):
        raise ValueError(f"Path {path} already exists.")
    with open(path, 'w') as f:
        f.write(content)
    return path

def overwrite_file(path: str, content: str) -> str:
    """
    Overwrite the content of the file at the given path with the given content.
    """
    # Validate that the path exists and is writable
    validate_path(path)
    with open(path, 'w') as f:
        f.write(content)
    return path
    
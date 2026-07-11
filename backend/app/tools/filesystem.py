

"""
filesystem.py

The File System tool provides controlled access to files and
folders for the AI Agent.

Version 0.1 supports reading text files only.
Future versions will support writing files, listing directories,
creating folders, and deleting files with appropriate safeguards.
"""

from pathlib import Path


def filesystem(file_path: str) -> dict:
    """
    Read a text file from the local filesystem.

    Args:
        file_path: Path to the file.

    Returns:
        A standardized observation dictionary.
    """

    try:
        path = Path(file_path)

        if not path.exists():
            return {
                "tool": "filesystem",
                "success": False,
                "observation": f"File not found: {file_path}",
            }

        if not path.is_file():
            return {
                "tool": "filesystem",
                "success": False,
                "observation": f"Not a file: {file_path}",
            }

        content = path.read_text(encoding="utf-8")

        return {
            "tool": "filesystem",
            "success": True,
            "observation": content,
        }

    except Exception as e:
        return {
            "tool": "filesystem",
            "success": False,
            "observation": str(e),
        }
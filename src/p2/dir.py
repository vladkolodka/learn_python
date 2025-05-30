﻿from pathlib import Path
from enum import Enum
from mprint import print_colored, Color
from typing import Optional


class Directory(Enum):
    DESKTOP = "Desktop"
    DOCUMENTS = "Documents"
    DOWNLOADS = "Downloads"
    PICTURES = "Pictures"
    MUSIC = "Music"
    VIDEOS = "Videos"


def list_files_in_user_dir(directory: Directory, extensions: Optional[list[str]] = None) -> list[Path]:
    if directory is Directory.PICTURES:
        raise DirectoryNotFoundError(directory.value)

    if extensions:
        extensions = [ext if ext.startswith(".") else f".{ext}" for ext in extensions]

    directory_path = Path.home() / str(directory.value)
    files = [
        f for f in directory_path.iterdir()
        if f.is_file() and (not extensions or f.suffix in extensions)
    ]

    return files


def print_dirs():
    for directory in Directory:
        try:
            list_of_files = list_files_in_user_dir(directory, ["ini"])
            print(f"Files in {directory.value}: {list_of_files}")
        except DirectoryNotFoundError as e:
            # print with error color
            print_colored(f"Error: {e}", Color.RED)
            continue


class DirectoryNotFoundError(Exception):
    def __init__(self, directory: str):
        self.directory = directory
        super().__init__(f"Directory '{directory}' not found.")
        self.add_note(
            f"Please check if the directory '{directory}' exists in your home directory."
        )


class FileNotFoundError(Exception):
    def __init__(self, file_path: str):
        self.file_path = file_path
        super().__init__(f"File '{file_path}' not found.")
        self.add_note(
            f"Please check if the file '{file_path}' exists in your home directory."
        )

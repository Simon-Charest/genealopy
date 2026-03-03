from io import TextIOWrapper
from pathlib import Path


def read(file: Path) -> str:
    stream: TextIOWrapper = open(file)
    string: str = stream.read()
    stream.close()

    return string

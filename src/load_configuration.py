from io import TextIOWrapper
from json import load
from typing import Any


def load_configuration(file: str) -> dict[str, Any]:
    stream: TextIOWrapper = open(file)
    configuration: dict[str, Any] = load(stream)
    stream.close()

    return configuration

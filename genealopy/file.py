from genealopy.constant import DEBUG
from glob import glob
from json import dump, dumps, load, loads
from json.decoder import JSONDecodeError
from typing import Any


def dump_collection(filename: str, collection: (dict | list), encoding: str = "utf-8", ensure_ascii: bool = False, indent: int = 2) -> None:
    """Write a JSON dictionary object to a file."""

    dump(collection, open(filename, "w", encoding=encoding), ensure_ascii=ensure_ascii, indent=indent)


def dump_collection(collection: dict, ensure_ascii: bool = False, indent: int = 2) -> dict:
    """Serialize JSON dictionary object and return it as a JSON formatted string."""

    return dumps(collection, ensure_ascii=ensure_ascii, indent=indent)


def get_filenames(paths: list, recursive: bool = True) -> list:
    """Get a list of filenames."""

    filenames: list = []

    for path in paths:
        filenames.extend(glob(str(path), recursive=recursive))

    return filenames


def loads(string: str) -> Any:
    """Deserialize a JSON formatted string and return is as a JSON dictionary object."""

    return loads(string)


def load_collection(filenames: list, encoding: str = "utf-8") -> dict:
    """Read a file and return its content as a JSON dictionary object."""

    collection: dict = {}
    filename: str

    for filename in filenames:
        if DEBUG:
            print(f"Filename: {filename}")

        # Read JSON data
        with open(filename, encoding=encoding) as stream:
            try:
                json_document = load(stream)

            except JSONDecodeError as json_decode_error:
                print(f"Exception: JSON Decode Error"
                      f"\nMessage: {json_decode_error.msg}"
                      f"\nLine Number: {json_decode_error.lineno}"
                      f"\nFilename: {filename}")
                exit()

            if DEBUG:
                print(f"JSON Document: {json_document}")

            collection.update(json_document)

    return collection


def write(filename, string, encoding="utf-8") -> None:
    """Write to a file."""

    open(filename, "w", encoding=encoding).write(string)


def write_collection(filename: str, collection: Any, encoding: str = "utf-8", ensure_ascii: bool = False) -> None:
    """Serialize JSON dictionary object to a JSON formatted string and write it to a file."""

    open(filename, "w", encoding=encoding).write(dumps(collection, ensure_ascii=ensure_ascii))


def read(filename: str, encoding: str = "utf-8") -> str:
    """Read from a file."""

    return open(filename, encoding=encoding).read()

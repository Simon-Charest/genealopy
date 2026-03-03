from glob import glob
from io import TextIOWrapper
from pathlib import Path
from bs4 import BeautifulSoup, Tag


def delete(pathname: str, verbose: bool = False) -> None:
    paths: list[str] = glob(pathname)
    path: str

    for path in paths:
        # Read content
        stream: TextIOWrapper = open(path, encoding="utf-8")
        markup: str = stream.read()
        stream.close()
        soup: BeautifulSoup = BeautifulSoup(markup, "html.parser")

        # Delete empty files
        tag: Tag | None = soup.find("h2")
        
        if tag and tag.get_text(strip=True) == "Identification de membre":
            if verbose:
                print(f"Deleting {path}...")

            Path(path).unlink()

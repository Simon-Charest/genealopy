from bs4 import BeautifulSoup, Tag
from collections import deque
from io import TextIOWrapper
from pathlib import Path
from re import compile
from requests import Response, Session
from time import sleep
from urllib.parse import parse_qs, urlparse


def crawl(
    login_url: str,
    email: str,
    password: str,
    url: str,
    references: deque[dict[str, int]],
    path: str,
    encoding: str ="utf-8",
    seconds: float  = 0.5,
    verbose: bool = False
) -> None:
    session: Session = Session()

    while references:
        reference: dict[str, int] = references.popleft()
        file: str = "_".join(str(value) for value in reference.values())

        if verbose:
            print(f"Processing {file}...")

        soup = get_file(session, url, reference)

        # Connect
        if not is_connected(soup):
            connect(session, login_url, email, password)
            soup = get_file(session, url, reference)

        # Remove visitor counter script
        for tag in soup.find_all("img"):
            if "fpcount" in (tag.get("src") or ""):
                tag.decompose()
        
        # Remove JavaScript and style
        for tag in soup(["script", "style"]):
            tag.decompose()

        # Write to file
        stream: TextIOWrapper = open(Path(path).joinpath(f"{file}.html"), "w", encoding=encoding)
        stream.write(soup.prettify())
        stream.close()

        # Add new references
        keys: list[str] = list(reference.keys())

        for tag in soup.find_all("a", href=compile(keys[-1])):
            href: str = str(tag["href"])
            params: dict[str, list[str]] = parse_qs(urlparse(href).query)
            reference = {key: int(params[key][0]) for key in keys}

            if reference not in references:
                references.append(reference)

        sleep(seconds)

    session.close()


def connect(session: Session, url: str, email: str, password: str, from_encoding: str | None = None) -> None:
    response: Response = session.post(url, {"email": email, "password": password})
     
    BeautifulSoup(response.content, "html.parser", from_encoding=from_encoding)


def is_connected(soup: BeautifulSoup) -> bool:
    tag: Tag | None = soup.find("h2")
        
    return tag is not None and tag.get_text(strip=True) == "Fiche familiale"


def get_file(session: Session, url: str, params: dict[str, int], from_encoding: str | None = None) -> BeautifulSoup:
    response = session.get(url, params=params)

    return BeautifulSoup(response.content, "html.parser", from_encoding=from_encoding)

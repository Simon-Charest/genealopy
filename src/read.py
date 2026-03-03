from bs4 import BeautifulSoup, Tag
from datetime import date
from glob import glob
from io import TextIOWrapper
from time import strptime, struct_time
from typing import Any
from urllib.parse import ParseResult, parse_qs, urlparse


def read(pathname: str, verbose: bool = False) -> None:
    paths: list[str] = glob(pathname)
    path: str

    for path in paths:
        if verbose:
            print(f"Processing {path}...")

        # Read content
        stream: TextIOWrapper = open(path, encoding="utf-8")
        markup: str = stream.read()
        stream.close()
        soup: BeautifulSoup = BeautifulSoup(markup, "html.parser")

        # Get person
        persons: list[dict[str, Any]] = []
        persons.append(get_person(soup))
        persons.extend(get_persons(soup))

        for person in persons:
            print(person)

def get_person(soup: BeautifulSoup):
    tag: Tag | None = soup.find("td", width="50%")
        
    if not tag:
        return {}
    
    tag = tag.find("b")
        
    if not tag:
        return {}
    
    # Get names
    full_name = " ".join(tag.get_text(strip=True).split())
    first_name: str
    last_name: str
    first_name, last_name = split(full_name)

    # Get code_owner
    tag = soup.find("input", {"name": "code_owner"})

    if not tag:
        return {}

    code_owner: int = int(str(tag["value"]))

    # Get code_individu
    tag = soup.find("input", {"name": "code_individu"})

    if not tag:
        return {}
    
    code_individu: int = int(str(tag["value"]))
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "code_owner": code_owner,
        "code_individu": code_individu
    }


def get_persons(soup: BeautifulSoup) -> list[dict[str, Any]]:
    tag: Tag
    persons: list[dict[str, Any]] = []

    for tag in soup.find_all("a", href=True):
        href: str = str(tag["href"])
        
        if "code_owner=" in href and "code_individu=" in href:
            parsed: ParseResult = urlparse(str(href))
            params: dict[str, Any] = parse_qs(parsed.query)
            
            code_owner = int(params.get("code_owner", [None])[0])
            code_individu = int(params.get("code_individu", [None])[0])
            
            # Get names
            full_name = " ".join(tag.get_text(strip=True).split())
            first_name: str
            last_name: str
            first_name, last_name = split(full_name)

            # Get birth
            birth: dict[str, str] = get_birth(tag)

            persons.append({
                "first_name": first_name,
                "last_name": last_name,
                "code_owner": code_owner,
                "code_individu": code_individu
            } | birth)

    return persons


def split(full_name: str) -> tuple[str, str]:
    full_name = " ".join(full_name.split())
    names: list[str] = full_name.split()

    return " ".join(names[:-1]), names[-1]


def get_birth(tag: Tag) -> dict[str, str]:
    for string in tag.find_all_next(string=True):
        if "Naissance:" in string:
            birth_label_td: Tag | None = string.find_parent("td")

            if not birth_label_td:
                continue

            value_td: Tag | None = birth_label_td.find_next("td")

            if not value_td:
                continue

            raw_value: str = value_td.get_text(strip=True)

            if "," not in raw_value:
                continue

            birthdate: str
            birthplace: str
            birthdate, birthplace = raw_value.split(",", 1)

            return {
                "birthdate": parse_date(birthdate.strip()),
                "birthplace": birthplace.strip(),
            }
        
    return {}


def parse_date(birthdate: str) -> str:
    time: struct_time = strptime(birthdate, "%d %b %Y")

    return date(time.tm_year, time.tm_mon, time.tm_mday).isoformat()

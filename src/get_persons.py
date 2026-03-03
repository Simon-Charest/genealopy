from bs4 import BeautifulSoup, Tag
from glob import glob
from io import TextIOWrapper
from typing import Any
from urllib.parse import ParseResult, parse_qs, urlparse

from src.datetime import parse_date


def get_persons(pathname: str, database: str, verbose: bool = False) -> list[dict[str, Any]]:
    paths: list[str] = glob(pathname)
    path: str
    persons: list[dict[str, Any]] = []

    for path in paths:
        if verbose:
            print(f"Processing {path}...")

        # Read content
        stream: TextIOWrapper = open(path, encoding="utf-8")
        markup: str = stream.read()
        stream.close()
        soup: BeautifulSoup = BeautifulSoup(markup, "html.parser")

        # Get person
        subject: dict[str, Any] = get_person(soup)
        if not any(p["owner_id"] == subject["owner_id"] and p["id"] == subject["id"] for p in persons):
            persons.append(subject)

        # Get relationships
        for relationship in get_relationships(soup):
            if not any(p["owner_id"] == relationship["owner_id"] and p["id"] == relationship["id"] for p in persons):
                persons.append(relationship)

    return persons


def get_person(soup: BeautifulSoup) -> dict[str, Any]:
    tag: Tag | None = soup.find("td", width="50%")
    if not tag:
        return {}
    
    b_tag = tag.find("b")
    if not b_tag:
        return {}

    full_name = " ".join(b_tag.get_text(strip=True).split())
    first_name, last_name = split(full_name)

    # Gender
    gender: str | None = None
    sibling = b_tag.next_sibling
    while sibling is not None:
        if isinstance(sibling, Tag):
            break
        text = str(sibling).strip()
        if text:
            if "(homme)" in text:
                gender = "M"
            elif "(femme)" in text:
                gender = "F"
            break
        sibling = sibling.next_sibling

    # Parents (Père/Mère links in the sibling <td>)
    father_id: int | None = None
    mother_id: int | None = None
    parent_td = tag.find_next_sibling("td")
    if parent_td:
        for a in parent_td.find_all("a", href=True):
            prev = a.previous_sibling
            while prev is not None:
                if isinstance(prev, Tag):
                    break
                text = str(prev).strip()
                if text:
                    parsed = urlparse(str(a["href"]))
                    params = parse_qs(parsed.query)
                    code = int(params["code_individu"][0])
                    if "Père" in text or "Pere" in text:
                        father_id = code
                    elif "Mère" in text or "Mere" in text:
                        mother_id = code
                    break
                prev = prev.previous_sibling

    # id / owner_id from # référence: <b>214,227835</b>
    ref_tag: Tag | None = tag.find("b", string=lambda s: s and "," in s and s.strip().replace(",", "").isdigit())
    if not ref_tag:
        return {}
    owner_id, individu_id = map(int, ref_tag.get_text(strip=True).split(","))

    person: dict[str, Any] = {
        "id":         individu_id,
        "owner_id":   owner_id,
        "last_name":  last_name,
        "first_name": first_name,
    }
    if gender:
        person["gender"] = gender
    if father_id:
        person["father_id"] = father_id
    if mother_id:
        person["mother_id"] = mother_id

    return person


def get_relationships(soup: BeautifulSoup) -> list[dict[str, Any]]:
    persons: list[dict[str, Any]] = []

    # Track spouse info for assigning to children
    spouse_code: int | None = None
    spouse_father: int | None = None
    spouse_mother: int | None = None
    main_code: int | None = None
    main_gender: str | None = None

    # Get main person's code and gender to know which role they play for children
    input_tag = soup.find("input", {"name": "code_individu"})

    if input_tag:
        main_code = int(str(input_tag["value"]))

    td = soup.find("td", width="50%")

    if td:
        b_tag = td.find("b")

        if b_tag:
            sib = b_tag.next_sibling

            while sib:
                if isinstance(sib, Tag):
                    break

                t = str(sib).strip()

                if t:
                    if "(homme)" in t:
                        main_gender = "M"

                    elif "(femme)" in t:
                        main_gender = "F"

                    break

                sib = sib.next_sibling

    in_children = False

    for tag in soup.find_all("a", href=True):
        href: str = str(tag["href"])
        if "code_owner=" not in href or "code_individu=" not in href:
            continue

        parsed: ParseResult = urlparse(href)
        params: dict[str, Any] = parse_qs(parsed.query)
        code_owner = int(params["code_owner"][0])
        code_individu = int(params["code_individu"][0])

        # Skip the main person
        if code_individu == main_code:
            continue

        full_name = " ".join(tag.get_text(strip=True).split())
        first_name, last_name = split(full_name)

        person: dict[str, Any] = {
            "id": code_individu,
            "owner_id": code_owner,
            "last_name": last_name,
            "first_name": first_name
        }

        # Check preceding text for Père/Mère (parents of main or spouse)
        prev = tag.previous_sibling
        is_parent_link = False
        while prev is not None:
            if isinstance(prev, Tag):
                break

            text = str(prev).strip()

            if text:
                if "Père" in text or "Pere" in text:
                    person["gender"] = "M"
                    is_parent_link = True
                    
                elif "Mère" in text or "Mere" in text:
                    person["gender"] = "F"
                    is_parent_link = True

                break

            prev = prev.previous_sibling

        # Walk forward siblings for gender and birth
        sibling = tag.next_sibling
        is_spouse = False

        while sibling is not None:
            if isinstance(sibling, Tag):
                if sibling.name == "hr":
                    break

                if sibling.name == "table":
                    birth_label = sibling.find(string=lambda s: s and "Naissance:" in s)

                    if birth_label:
                        td2 = birth_label.find_next("td")

                        if isinstance(td2, Tag):
                            raw = td2.get_text(strip=True)

                            if "," in raw:
                                birthdate, birthplace = raw.split(",", 1)
                                person["birthdate"] = parse_date(birthdate)
                                person["birthplace"] = birthplace.strip()

                    break
            else:
                text = str(sibling).strip()

                if "(homme)" in text:
                    person["gender"] = "M"

                elif "(femme)" in text:
                    person["gender"] = "F"

            sibling = sibling.next_sibling

        # Detect spouse: has a "# référence" nearby and is not a parent link
        ref_text = tag.find_next(string=lambda s: s and "référence" in s)

        if ref_text and not is_parent_link:
            # Check if this is the spouse block (direct child of union row)
            parent_td = tag.find_parent("td", {"bgcolor": "#ffcf8f"})

            if parent_td and not in_children:
                is_spouse = True
                spouse_code = code_individu

                # Get spouse's parents
                next_td = parent_td.find_next_sibling("td")

                if next_td:
                    for a in next_td.find_all("a", href=True):
                        p = a.previous_sibling

                        while p:
                            if isinstance(p, Tag):
                                break

                            t = str(p).strip()

                            if t:
                                sp = urlparse(str(a["href"]))
                                sp_params = parse_qs(sp.query)
                                sp_code = int(sp_params["code_individu"][0])

                                if "Père" in t or "Pere" in t:
                                    spouse_father = sp_code
                                    
                                elif "Mère" in t or "Mere" in t:
                                    spouse_mother = sp_code

                                break

                            p = p.previous_sibling
                in_children = True

        # Assign father/mother to children
        if in_children and not is_parent_link and not is_spouse:
            if main_gender == "F":
                person["father_id"] = spouse_code
                person["mother_id"] = main_code
            else:

                person["father_id"] = main_code
                person["mother_id"] = spouse_code

        # Assign parents to spouse
        if is_spouse:
            if spouse_father:
                person["father_id"] = spouse_father

            if spouse_mother:
                person["mother_id"] = spouse_mother

        persons.append(person)

    return persons


def split(full_name: str) -> tuple[str, str]:
    full_name = " ".join(full_name.split())
    names: list[str] = full_name.split()

    return " ".join(names[:-1]), names[-1]

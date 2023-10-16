from genealopy.constant import NAME_UNKNOWN
from genealopy.text import is_none
from typing import Any


def exists_in(collection: (dict | list), key: str, value: Any = None) -> bool:
    if not value:
        return key in collection
    
    return key in collection and collection[key] == value    


def get_count(collection: dict, key: str, minimum: int = 1) -> list:
    item: str
    dictionary: dict = {}
    
    # Add item and its frequency to 
    for item in collection:
        if collection[item][key] in dictionary:
            dictionary[collection[item][key]] += 1

        else:
            dictionary[collection[item][key]] = 1

    # Filter values by minimal frequency
    if minimum > 1:
        dictionary = [filter(lambda values: values[1] >= minimum, dictionary.items())]

    # Sort values alphabetically
    items: list = sorted(dictionary.items(), key=lambda values: is_none(values[0]))

    # Sort values by descending frequency
    return sorted(items, key=lambda values: values[1], reverse=True)


def get_gender(collection: dict, id: str) -> str:
    key: str
    
    for key in collection:
        value: dict = collection[key]

        if f"{value['first_name']}\n{value['last_name']}" == id:
            return value["gender"]

    return None


def get_name(value: dict) -> str:
    first_name: str = value["first_name"]
    last_name: str = value["last_name"]

    if first_name in [None, ""]:
        first_name = NAME_UNKNOWN

    if last_name in [None, ""]:
        last_name = NAME_UNKNOWN

    return f"{first_name}\n{last_name}"


def get_node(collection: dict, id: str) -> dict:
    key: str

    # Loop on every person
    for key in collection:
        value = collection[key]

        if key == id:
            return value

    return None


def get_relationship(collection: dict, value: str) -> str:
    key: str

    for key in collection["relationship"]:
        if collection["relationship"][key]["type"] == value:
            return key

    return None


def get_relationship_count(collection: dict) -> int:
    relationship_count: int = 0
    value: dict

    for _, value in collection.items():
        relationship_count += len(value["relationship"])

    return relationship_count


def get_relationship_gender(collection: dict, id: str) -> str:
    key: str

    for key in collection:
        value = collection[key]

        if key == id:
            return value["gender"]

    return None


def get_relationship_name(collection: dict, id: str) -> str:
    key: str
    
    for key in collection:
        value = collection[key]

        if key == id:
            return f"{value['first_name']}\n{value['last_name']}"

    return None


def get_relationship_type(value: dict, id: str) -> str:
    return value["relationship"][id]["type"]


def has_parents(collection: dict, key: str) -> bool:
    """Check if both parents are present in relationships."""
    
    relationships: dict = collection[key]["relationship"]
    id: str
    mother: bool = False
    father: bool = False

    for id in relationships:
        # Check if parent node is in graph
        if id not in collection:
            return False

        if "mother" in relationships[id]["type"]:
            mother = True

        elif "father" in relationships[id]["type"]:
            father = True

    return mother and father


def is_complete(value: dict) -> bool:
    if "complete" in value:
        return value["complete"]

    return True


def is_family(value: dict) -> bool:
    if "family" in value:
        return value["family"]

    return True

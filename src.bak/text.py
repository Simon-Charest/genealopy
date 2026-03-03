def get_full_name(collection: dict, last_name_first: bool = False) -> str:
    first_name: str = collection["first_name"]
    last_name: str = collection["last_name"]

    if last_name_first:
        full_name = f"{last_name}, {first_name}"

    else:
        full_name = f"{first_name} {last_name}"

    return full_name


def is_none(string: str) -> str:
    if string is None:
        return ""

    return str(string)


def pluralize(word: str, count: int = 2) -> str:
    return word if count <= 1 else f"{word}s"


def print_statistics(node_count: int, edge_count: int, node_label: str = "family member", edge_label: str = "relationship") -> None:
    print("Statistics:")
    print(f"{node_count} {pluralize(node_label)}")
    print(f"{edge_count} {pluralize(edge_label)}")

from copy import deepcopy
from genealopy.data import exists_in
from genealopy.text import get_full_name
from json import loads


def add_children(collection: dict) -> dict:
    children: dict = deepcopy(collection)
    child: dict
    type: str

    # For each child...
    for child in children:
        parents = children[child]["relationship"]

        # For each of its parents...
        for parent in parents:
            type = parents[parent]["type"]

            # If the relationship is a parent...
            if type in ["father", "mother"]:
                # Create an inverted relationship from the parent to the child
                string = f'{{"{child}": {{"type": "child"}}}}'
                dictionary = loads(string)

                # Only create child link if parent exists
                if parent in children:
                    children[parent]["relationship"].update(dictionary)

    return children


def get_details(collection, start, field, default=None, path=[], details=[]):
    path = path + [start]

    if start in collection:
        if field in collection[start]:
            details = details + [collection[start][field]]

        else:
            details = details + [default]

    yield details

    if start not in collection:
        return

    parents = get_parents(collection[start]["relationship"])

    for parent in parents:
        if parent not in path:
            yield from get_details(collection, parent, field, default, path, details)


def get_parents(relationships):
    """ Filter out relationships which are not parents """

    parents = dict([(relationship, relationships[relationship]) for relationship in relationships
                    if relationships[relationship]["type"] in ["mother", "father"]])

    return parents


def get_paths(collection, start, path=[]):
    path = path + [start]

    yield path

    if start not in collection:
        return

    parents = get_parents(collection[start]["relationship"])

    for parent in parents:
        if parent not in path:
            yield from get_paths(collection, parent, path)


def get_shortest_path(collection, start, end):
    """
        Dijkstra"s shortest path algorithm
        Source: https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
    """

    # Shortest paths is a dictionary of nodes whose values are tuples of (previous node, weight)
    current_node = start
    visited = set()
    shortest_paths = {start: (None, 0)}

    while current_node != end:
        visited.add(current_node)
        destinations = {}

        if exists_in(collection, current_node):
            destinations = collection[current_node]["relationship"]

        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = 1 + weight_to_current_node

            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)

            else:
                current_shortest_weight = shortest_paths[next_node][1]

                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}

        if not next_destinations:
            return {}

        # Next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda key: next_destinations[key][1])

    # Work back through destinations in shortest path
    shortest_path = []

    while current_node is not None:
        shortest_path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node

    # Reverse path
    shortest_path = shortest_path[::-1]

    return shortest_path


def print_details(list_, collection, id, maximum=None):
    if id in collection:
        full_name = get_full_name(collection[id])

    else:
        full_name = id

    print(f"{full_name} is...")

    for element in list_:
        if maximum is None or element[3] <= maximum:
            print(f"{element[0]} ({element[1]}) {element[2]} (g={element[3]})")

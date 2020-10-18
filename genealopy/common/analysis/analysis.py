from common import data
from common import text

import copy
import json


def add_children(json_objects):
    children = copy.deepcopy(json_objects)

    # For each child...
    for child in children:
        parents = children[child]['relationship']

        # For each of its parents...
        for parent in parents:
            type_ = parents[parent]['type']

            # If the relationship is a parent...
            if type_ in ['father', 'mother']:
                # Create an inverted relationship from the parent to the child
                string = f'{{"{child}": {{"type": "child"}}}}'
                dictionary = json.loads(string)

                # Only create child link if parent exists
                if parent in children:
                    children[parent]['relationship'].update(dictionary)

    return children


def get_parents(relationships):
    """ Filter out relationships which are not parents """

    parents = dict([(relationship, relationships[relationship]) for relationship in relationships
                    if relationships[relationship]['type'] in ['mother', 'father']])

    return parents


def get_paths(json_objects, start, path=[]):
    path = path + [start]

    yield path

    if start not in json_objects:
        return

    parents = get_parents(json_objects[start]['relationship'])

    for parent in parents:
        if parent not in path:
            yield from get_paths(json_objects, parent, path)


def get_shortest_path(json_objects, start, end):
    """
        Dijkstra's shortest path algorithm
        Source: https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
    """

    # Shortest paths is a dictionary of nodes whose values are tuples of (previous node, weight)
    current_node = start
    visited = set()
    shortest_paths = {start: (None, 0)}

    while current_node != end:
        visited.add(current_node)
        destinations = {}

        if data.exists_in(json_objects, current_node):
            destinations = json_objects[current_node]['relationship']

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


def print_details(list_, json_objects, id_, maximum=None):
    if id_ in json_objects:
        full_name = text.get_full_name(json_objects[id_])

    else:
        full_name = id_

    print(f'{full_name} is...')

    for element in list_:
        if maximum is None or element[3] <= maximum:
            print(f'{element[0]} ({element[1]}) {element[2]} (g={element[3]})')

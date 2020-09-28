import json


def add_children(json_objects):
    # For each child...
    for child in json_objects:
        parents = json_objects[child]['relationship']

        # For each of its parents...
        for parent in parents:
            type_ = json_objects[child]['relationship'][parent]['type']

            # If the relationship is a parent...
            if type_ in ['father', 'mother']:
                # Create an inverted relationship from the parent to the child
                string = f'{{"{child}": {{"type": "child"}}}}'
                dictionary = json.loads(string)
                json_objects[parent]['relationship'].update(dictionary)


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

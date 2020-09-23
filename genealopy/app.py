from common.constant import constant

from graphviz import Digraph
"""
Prerequisites:
    - Microsoft C++ Build Tools - https://visualstudio.microsoft.com/visual-cpp-build-tools/
    - Graphviz - https://graphviz.gitlab.io/_pages/Download/Download_windows.html
"""

import glob
import json

RANK_DIRECTION = 'TB'  # TB, LR, BT or RL
DATA = [
    'data/Charest/far_ascendance/*.json',  # Delphis Charest's ascendance
    'data/Charest/tanguay_charest_siblings/*.json',  # Delphis Charest's siblings
    'data/Charest/dion_charette_ascendance/*.json',  # Aurèle Charette (Charest-Charette)'s ascendance
    'data/Charest/little_cousins/*.json',  # Clément Charest siblings' descendance
    'data/Charest/little_cousin_descendance/*.json',  # Clément Charest siblings' descendance
    'data/Tremblay/*.json',  # Rita Lacombe Tremblay's ascendance
    'data/Charest/*.json',
    'data/Laguë/*.json',  # Suzanne Laguë's ascendance
    'data/0?_lague_charest.json',
    'data/Charest/descendance/*.json'
]
SHAPE = 'box'
STYLE = 'filled'
GENDER = ['M', 'F']
RELATIONSHIP = ['father', 'mother', 'union', 'child']
FEMALE_COLOR = 'pink'
FEMALE_INCOMPLETE_COLOR = 'deeppink'
MALE_COLOR = 'lightblue'
MALE_INCOMPLETE_COLOR = 'deepskyblue'
UNDEFINED_COLOR = 'grey'
PARENT_LINK_STYLE = 'solid'
UNDEFINED_LINK_STYLE = 'dashed'
NAME_UNKNOWN = '(inconnu)'
HIGHLIGHT_INCOMPLETE = True
DEBUG = False
SEARCH_COLOR = 'yellow'

"""
Filenames examples:
    ma01_dubreuil_lague.json   : first-degree (01) ascendant (a) of the mother's side (m) of the family
    fa01_tremblay_charest.json : first-degree (01) ascendant (a) of the father's side (f) of the family
    00_lague_charest.json      : Root (00) of both sides of the family
    m00_dubreuil_lague.json    : Root (00) of the mother's side (m) of the family
    f00_tremblay_charest.json  : Root (00) of the father's side (f) of the family
    md01_dubreuil_lague.json   : first-degree (01) descendant (d) of the mother's side (m) of the family
    fd01_charest_drouin.json   : first-degree (01) descendant (d) of the father's side (f) of the family
"""


def run():
    graph = Digraph(constant.__project__, filename=f'data/{constant.__project__.lower()}.gv', format='png')
    graph.attr(rankdir=RANK_DIRECTION)

    # Get data from JSON files
    filenames = get_filenames(DATA)
    json_objects = get_json_objects(filenames)

    # Augment data with children
    # print(json_objects['511416']['relationship'])
    # children = get_children(json_objects)
    # print(children['511416']['relationship'])
    #
    # add_children(json_objects, children)

    # Highlight shortest path(s)
    search = list()
    search.append('Simon.Charest')
    # search.extend(get_shortest_path(json_objects, 'Aurèle.Charette', 'Jean-Baptiste3.Chorret Chaurette'))
    # search.extend(get_shortest_path(json_objects, 'Henriette.Charest', 'Jean-Baptiste3.Chorret Chaurette'))
    # search.extend(get_shortest_path(json_objects, 'Simon.Charest', '511417'))
    # search.extend(get_shortest_path(json_objects, 'Dominique.Charest', '511417'))
    # search.extend(get_shortest_path(json_objects, '511417', 'Simon.Charest'))  # Does not work
    # search.extend(get_shortest_path(json_objects, 'Simon.Charest', 'Dominique.Charest'))  # Does not work

    if DEBUG:
        print(f'Search: {search}')

    person_count = 0
    relationship_count = 0

    # Loop on every person
    for key1 in json_objects:
        # Get first person properties
        value1 = json_objects[key1]
        name1 = get_name(value1)
        gender1 = value1['gender']
        person_count += 1

        if gender1 in GENDER:
            if 'search' in locals() and key1 in search:
                color1 = SEARCH_COLOR

            else:
                if HIGHLIGHT_INCOMPLETE and is_family(value1):
                    complete1 = has_parents(value1['relationship'])

                else:
                    complete1 = True

                color1 = get_color(gender1, complete1)

            # Draw first person
            graph.node(key1, label=name1, color=color1, shape=SHAPE, style=STYLE)

            # Loop on every relationship
            for key2 in value1['relationship']:
                # Get second person properties
                gender2 = get_relationship_gender(json_objects, key2)

                if gender2 in GENDER:
                    # Get relationship properties
                    relationship = get_relationship_type(value1, key2)
                    edge_color = get_color(relationship)
                    edge_style = get_style(relationship)

                    if relationship in RELATIONSHIP:
                        # Draw relationship
                        graph.edge(key2, key1, color=edge_color, style=edge_style)

                        relationship_count += 1

    print(f"{person_count} {pluralize('family member')}")
    print(f"{relationship_count} {pluralize('relationship')}")

    graph.view()


def add_children(json_objects, children):
    for json_object in json_objects:
        if exists_in(children, json_object):
            json_objects[json_object]['relationship'].update(children[json_object]['relationship'])


def count_edges(path):
    return len(path)


def get_children(json_objects):
    """ TODO: Fix this (only adds one child per parent) """

    children = {}

    for child in json_objects:
        parents = json_objects[child]['relationship']

        for parent in parents:
            type_ = parents[parent]['type']

            if type_ in ['father', 'mother']:
                # Example:
                # {'Michel.Charest': {'relationship':
                #     {'Simon.Charest': {'type': 'child'}},
                #     {'Catherine.Charest': {'type': 'child'}}
                # }
                dictionary = {parent: {'relationship': {child: {'type': 'child'}}}}
                children.update(dictionary)

    return children


def exists_in(json_object, key, value=None):
    if value:
        return key in json_object and json_object[key] == value

    else:
        return key in json_object


def get_color(gender, complete=True):
    if gender in ['F', 'mother']:
        if complete:
            color = FEMALE_COLOR

        else:
            color = FEMALE_INCOMPLETE_COLOR

    elif gender in ['M', 'father']:
        if complete:
            color = MALE_COLOR

        else:
            color = MALE_INCOMPLETE_COLOR

    else:
        color = UNDEFINED_COLOR

    return color


def get_filenames(paths):
    list_ = list()

    for path in paths:
        filenames = glob.glob(path)
        list_.extend(filenames)

    return list_


def get_gender(json_objects, id_):
    for key in json_objects:
        value = json_objects[key]

        if f"{value['first_name']}\n{value['last_name']}" == id_:
            return value['gender']

    return None


def get_json_objects(filenames, encoding='utf-8'):
    json_objects = {}

    for filename in filenames:
        if DEBUG:
            print(f'Filename: {filename}')

        # Read JSON data
        with open(filename, encoding=encoding) as stream:
            json_document = json.load(stream)

            if DEBUG:
                print(f'JSON Document: {json_document}')

            json_objects.update(json_document)

    return json_objects


def get_name(value):
    first_name = value['first_name']
    last_name = value['last_name']

    if first_name in [None, '']:
        first_name = NAME_UNKNOWN

    if last_name in [None, '']:
        last_name = NAME_UNKNOWN

    return f"{first_name}\n{last_name}"


def get_node(json_objects, id_):
    # Loop on every person
    for key in json_objects:
        value = json_objects[key]

        if key == id_:
            return value

    return None


def get_relationship(node, type_):
    for key in node['relationship']:
        if node['relationship'][key]['type'] == type_:
            return key

    return None


def get_relationship_gender(json_objects, id_):
    for key in json_objects:
        value = json_objects[key]

        if key == id_:
            return f"{value['gender']}"

    return None


def get_relationship_name(json_objects, id_):
    for key in json_objects:
        value = json_objects[key]

        if key == id_:
            return f"{value['first_name']}\n{value['last_name']}"

    return None


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

        if exists_in(json_objects, current_node):
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


def get_style(type_):
    if type_ in ['F', 'mother', 'M', 'father']:
        style = PARENT_LINK_STYLE

    else:
        style = UNDEFINED_LINK_STYLE

    return style


def get_relationship_type(value, id_):
    return value['relationship'][id_]['type']


def has_parents(values):
    mother = False
    father = False

    for id_ in values:
        if 'mother' in values[id_]['type']:
            mother = True

        if 'father' in values[id_]['type']:
            father = True

    return mother and father


def is_family(value):
    if 'family' in value:
        return value['family'] == 'true'

    return True


def pluralize(word, count=2):
    return word if count <= 1 else f"{word}s"


def pop(json_objects, index=-1):
    list_ = list(json_objects)
    last = list_[index]
    item = json_objects.pop(last)

    return item

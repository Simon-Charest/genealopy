from common.constant import constant

"""
Prerequisites:
    - Microsoft C++ Build Tools - https://visualstudio.microsoft.com/visual-cpp-build-tools/
    - Graphviz - https://graphviz.gitlab.io/_pages/Download/Download_windows.html
"""
from graphviz import Digraph

import glob
import json

RANK_DIRECTION = 'TB'  # TB, LR, BT or RL
DATA = [
    'data/0?_lague_charest.json',
    'data/Laguë/*.json',
    'data/Charest/*.json'
]
SHAPE = 'box'
STYLE = 'filled'
GENDER = ['M', 'F']
RELATIONSHIP = ['father', 'mother', 'union']
FEMALE_COLOR = 'pink'
MALE_COLOR = 'lightblue2'
UNDEFINED_COLOR = 'grey'
PARENT_LINK_STYLE = 'solid'
UNDEFINED_LINK_STYLE = 'dashed'
NAME_UNKNOWN = '(inconnu)'
DEBUG = True

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

    filenames = get_filenames(DATA)
    json_documents = get_json_documents(filenames)

    person_count = 0
    relationship_count = 0

    # Loop on every JSON document
    for json_document in json_documents:
        # Loop on every person
        for key1, value1 in json_document.items():
            # Get first person properties
            name1 = get_name(value1)
            gender1 = value1['gender']
            person_count += 1

            if gender1 in GENDER:
                color1 = get_color(gender1)

                # Draw first person
                graph.node(key1, label=name1, color=color1, shape=SHAPE, style=STYLE)

                # Loop on every relationship
                for key2 in value1['relationship']:
                    # Get second person properties
                    name2 = get_relationship_name(json_documents, key2)
                    gender2 = get_relationship_gender(json_documents, key2)

                    if gender2 in GENDER:
                        color2 = get_color(gender2)

                        # Get relationship properties
                        relationship = get_relationship(value1, key2)
                        edge_color = get_color(relationship)
                        edge_style = get_style(relationship)

                        # Draw second person
                        graph.node(key2, label=name2, color=color2, shape=SHAPE, style=STYLE)

                        if relationship in RELATIONSHIP:
                            # Draw relationship
                            graph.edge(key2, key1, color=edge_color, style=edge_style)

                            relationship_count += 1

    if DEBUG:
        print(f"{person_count} {pluralize('person')}")
        print(f"{relationship_count} {pluralize('relationship')}")

    graph.view()


def get_color(gender):
    if gender in ['F', 'mother']:
        color = FEMALE_COLOR

    elif gender in ['M', 'father']:
        color = MALE_COLOR

    else:
        color = UNDEFINED_COLOR

    return color


def get_filenames(paths):
    list_ = list()

    for path in paths:
        filenames = glob.glob(path)
        list_.extend(filenames)

    return list_


def get_gender(json_documents, id_):
    for json_document in json_documents:
        for key, value in json_document.items():
            if f"{value['first_name']}\n{value['last_name']}" == id_:
                return value['gender']

    return None


def get_json_documents(filenames, encoding='utf-8'):
    json_documents = list()

    for filename in filenames:
        if DEBUG:
            print(filename)

        # Read JSON data
        with open(filename, encoding=encoding) as stream:
            json_document = json.load(stream)

            if DEBUG:
                print(json_document)

            json_documents.append(json_document)

    return json_documents


def get_name(value):
    first_name = value['first_name']
    last_name = value['last_name']

    if first_name in [None, '']:
        first_name = NAME_UNKNOWN

    if last_name in [None, '']:
        last_name = NAME_UNKNOWN

    return f"{first_name}\n{last_name}"


def get_relationship_gender(json_documents, id_):
    for json_document in json_documents:
        for key, value in json_document.items():
            if key == id_:
                return f"{value['gender']}"

    return None


def get_relationship_name(json_documents, id_):
    for json_document in json_documents:
        for key, value in json_document.items():
            if key == id_:
                return f"{value['first_name']}\n{value['last_name']}"

    return None


def get_style(type_):
    if type_ in ['F', 'mother', 'M', 'father']:
        style = PARENT_LINK_STYLE

    else:
        style = UNDEFINED_LINK_STYLE

    return style


def get_relationship(value, id_):
    return value['relationship'][id_]['type']


def pluralize(word, count=2):
    return word if count <= 1 else f"{word}s"

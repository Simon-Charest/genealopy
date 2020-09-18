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
    # 'data/Laguë/*.json',
    # 'data/Tremblay/*.json',
    'data/Charest/*.json'
]
SHAPE = 'box'
STYLE = 'filled'
GENDER = ['M', 'F']
RELATIONSHIP = ['father', 'mother', 'union']
FEMALE_COLOR = 'pink'
FEMALE_INCOMPLETE_COLOR = 'deeppink'
MALE_COLOR = 'lightblue'
MALE_INCOMPLETE_COLOR = 'deepskyblue'
UNDEFINED_COLOR = 'grey'
PARENT_LINK_STYLE = 'solid'
UNDEFINED_LINK_STYLE = 'dashed'
NAME_UNKNOWN = '(inconnu)'
HIGHLIGHT_INCOMPLETE = True
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
                    gender2 = get_relationship_gender(json_documents, key2)

                    if gender2 in GENDER:
                        # Get relationship properties
                        relationship = get_relationship(value1, key2)
                        edge_color = get_color(relationship)
                        edge_style = get_style(relationship)

                        if relationship in RELATIONSHIP:
                            # Draw relationship
                            graph.edge(key2, key1, color=edge_color, style=edge_style)

                            relationship_count += 1

    if DEBUG:
        print(f"{person_count} {pluralize('family member')}")
        print(f"{relationship_count} {pluralize('relationship')}")

    graph.view()


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

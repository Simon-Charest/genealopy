from common.constant import constant

"""
Prerequisites:
    - Microsoft C++ Build Tools - https://visualstudio.microsoft.com/visual-cpp-build-tools/
    - Graphviz - https://graphviz.gitlab.io/_pages/Download/Download_windows.html
"""
from graphviz import Digraph

import glob
import json

DATA = 'data/*.json'
SHAPE = 'box'
STYLE = 'filled'


def run():
    graph = Digraph(constant.__project__, filename=f'data/{constant.__project__.lower()}.gv', format='png')
    graph.attr(rankdir='LR')

    files = get_files(DATA)
    file_list = get_file_list(files)

    # Loop on every JSON document
    for json_document in file_list:
        # Loop on every person
        for key, value in json_document.items():
            # Get first person properties
            person = get_name(value)
            gender = value['gender']
            color = get_color(gender)

            # Draw first person
            graph.node(person, color=color, shape=SHAPE, style=STYLE)

            # Loop on every relationship
            for id_ in value['relationship']:
                # Get second person properties
                person2 = get_relationship_name(file_list, id_)
                gender2 = get_relationship_gender(file_list, id_)
                color2 = get_color(gender2)

                # Get relationship properties
                type_ = get_type(value, id_)
                edge_color = get_color(type_)
                edge_style = get_style(type_)

                # Draw second person
                graph.node(person2, color=color2, shape=SHAPE, style=STYLE)

                # Draw relationship
                graph.edge(person2, person, color=edge_color, style=edge_style)

    graph.view()


def get_color(gender):
    if gender in ['F', 'mother']:
        color = 'pink'

    elif gender in ['M', 'father']:
        color = 'lightblue2'

    else:
        color = 'grey'

    return color


def get_file_list(files, encoding='utf-8'):
    file_list = list()

    for file in files:
        # Read JSON data
        with open(file, encoding=encoding) as stream:
            file_list.append(json.load(stream))

    return file_list


def get_files(path):
    files = glob.glob(path)

    return files


def get_gender(list_, id_):
    for json_document in list_:
        for key, value in json_document.items():
            if f"{value['first_name']}\n{value['last_name']}" == id_:
                return value['gender']

    return None


def get_name(value):
    return f"{value['first_name']}\n{value['last_name']}"


def get_relationship_gender(list_, id_):
    for json_document in list_:
        for key, value in json_document.items():
            if key == id_:
                return f"{value['gender']}"

    return None


def get_relationship_name(list_, id_):
    for json_document in list_:
        for key, value in json_document.items():
            if key == id_:
                return f"{value['first_name']}\n{value['last_name']}"

    return None


def get_style(type_):
    if type_ in ['F', 'mother', 'M', 'father']:
        style = 'solid'

    else:
        style = 'dashed'

    return style


def get_type(value, id_):
    return value['relationship'][id_]['type']

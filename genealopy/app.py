from common import analysis
from common import data
from common import file
from common import text
from common import visual
from common.constant import constant

from graphviz import Digraph
"""
Prerequisites:
    - Microsoft C++ Build Tools - https://visualstudio.microsoft.com/visual-cpp-build-tools/
    - Graphviz - https://graphviz.gitlab.io/_pages/Download/Download_windows.html
"""


def run():
    # Get data from JSON files
    filenames = file.get_filenames(constant.DATA)
    json_objects = file.load_json_objects(filenames)

    # Augment data with children
    json_objects = analysis.add_children(json_objects)

    # Initialize graph
    graph = Digraph(name=constant.__project__, filename=f'data/{constant.__project__.lower()}.gv', format='png')
    graph.attr(rankdir=constant.RANK_DIRECTION)

    # Highlight shortest path(s)
    # search = ['Simon.Charest']
    # search = analysis.get_shortest_path(json_objects, 'Simon.Charest', 'Delphis.Charest')

    if constant.DEBUG and 'search' in locals():
        print(f'Search: {search}')

    # Loop on every person
    for key1 in json_objects:
        # Get first person properties
        value1 = json_objects[key1]
        name1 = data.get_name(value1)
        gender1 = value1['gender']

        # Display nodes of certain genders only...
        if gender1 in constant.GENDER:
            # Highlight selected persons
            if 'search' in locals() and key1 in search:
                color1 = constant.SEARCH_COLOR

            else:
                # Darken persons with missing parents but only if they are direct family
                if constant.DARKEN_INCOMPLETE and data.is_family(value1) and data.is_complete(value1):
                    complete1 = data.has_parents(json_objects, key1)

                else:
                    complete1 = True

                color1 = visual.get_color(gender1, complete1)

            # Draw first person
            graph.node(key1, label=name1, color=color1, shape=constant.SHAPE, style=constant.STYLE)

            # Loop on every relationship
            for key2 in value1['relationship']:
                # Get second person properties
                gender2 = data.get_relationship_gender(json_objects, key2)

                # Display edges of certain genders only...
                if gender2 in constant.GENDER:
                    # Get relationship properties
                    relationship = data.get_relationship_type(value1, key2)

                    # Display edges of certain relationship types only...
                    if relationship in constant.RELATIONSHIP:

                        # Highlight relationships between selected persons
                        if 'search' in locals() and key1 in search and key2 in search:
                            edge_color = constant.SEARCH_COLOR

                        else:
                            edge_color = visual.get_color(relationship)

                        edge_style = visual.get_style(relationship)

                        # Draw relationship
                        graph.edge(key2, key1, color=edge_color, style=edge_style)

    # Print statistics
    person_count = len(json_objects)
    relationship_count = data.get_relationship_count(json_objects)
    text.print_statistics(person_count, relationship_count)
    print(f"First name frequencies: {data.get_count(json_objects, 'first_name')}")
    print(f"Last name frequencies: {data.get_count(json_objects, 'last_name')}")

    # Display graph
    graph.view()

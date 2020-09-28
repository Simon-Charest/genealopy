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
    graph = Digraph(constant.__project__, filename=f'data/{constant.__project__.lower()}.gv', format='png')
    graph.attr(rankdir=constant.RANK_DIRECTION)

    # Get data from JSON files
    filenames = file.get_filenames(constant.DATA)
    json_objects = data.get_json_objects(filenames)

    # Augment data with children
    analysis.add_children(json_objects)

    # Highlight shortest path(s)
    search = list()
    search.append('Simon.Charest')
    # search.extend(get_shortest_path(json_objects, 'Aurèle.Charette', 'Jean-Baptiste3.Chorret Chaurette'))
    # search.extend(get_shortest_path(json_objects, 'Henriette.Charest', 'Jean-Baptiste3.Chorret Chaurette'))
    # search.extend(get_shortest_path(json_objects, 'Simon.Charest', 'Delphis.Charest'))
    # search.extend(get_shortest_path(json_objects, 'Dominique.Charest', 'Delphis.Charest'))
    # search.extend(get_shortest_path(json_objects, 'Delphis.Charest', 'Simon.Charest'))
    # search.extend(get_shortest_path(json_objects, 'Simon.Charest', 'Dominique.Charest'))

    if constant.DEBUG:
        print(f'Search: {search}')

    person_count = 0
    relationship_count = 0

    # Loop on every person
    for key1 in json_objects:
        # Get first person properties
        value1 = json_objects[key1]
        name1 = data.get_name(value1)
        gender1 = value1['gender']
        person_count += 1

        if gender1 in constant.GENDER:
            if 'search' in locals() and key1 in search:
                color1 = constant.SEARCH_COLOR

            else:
                if constant.HIGHLIGHT_INCOMPLETE and data.is_family(value1):
                    complete1 = data.has_parents(value1['relationship'])

                else:
                    complete1 = True

                color1 = visual.get_color(gender1, complete1)

            # Draw first person
            graph.node(key1, label=name1, color=color1, shape=constant.SHAPE, style=constant.STYLE)

            # Loop on every relationship
            for key2 in value1['relationship']:
                # Get second person properties
                gender2 = data.get_relationship_gender(json_objects, key2)

                if gender2 in constant.GENDER:
                    # Get relationship properties
                    relationship = data.get_relationship_type(value1, key2)
                    edge_color = visual.get_color(relationship)
                    edge_style = visual.get_style(relationship)

                    if relationship in constant.RELATIONSHIP:
                        # Draw relationship
                        graph.edge(key2, key1, color=edge_color, style=edge_style)

                        relationship_count += 1

    text.print_stats(person_count, relationship_count)
    graph.view()

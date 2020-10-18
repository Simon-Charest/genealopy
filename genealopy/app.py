from common import data
from common import file
from common import text
from common import visual
from common.analysis import analysis
from common.analysis import family
from common.analysis import genetic
from common.constant import constant
from pycrypt import pycrypt

from graphviz import Digraph
"""
Prerequisites:
    - Microsoft C++ Build Tools - https://visualstudio.microsoft.com/visual-cpp-build-tools/
    - Graphviz - https://graphviz.gitlab.io/_pages/Download/Download_windows.html
"""


def run():
    """ Main execution """

    backup_all_data()
    json_objects = load_data()
    graph = initialize_graph()

    # Highlight selected nodes
    search = []

    # TODO
    # search = ['Cécile.Lecour', 'Céleste.Boulianne', 'Élisabeth.Leroy', 'Luce.Boily', 'Lucien.Truchon',
    #           'Madeleine.Bouchard', 'Madeleine2.Tremblay', 'Marguerite.Labrecque', 'Marguerite.Lavoie',
    #           'Marie-Judith.Simard', 'Marie-Reine.Dufour', 'Zoé.Pagé']

    process_data(json_objects, graph, search)
    print_frequencies(json_objects)
    print_statistics(json_objects)
    print_genetics(json_objects, 'Simon.Charest', 3)
    print_families(json_objects, 'Simon.Charest', 3)

    # Display graph
    graph.view()


def decrypt_all_data():
    # Read the formatted and encrypted copy of the entire data
    string = file.read(constant.OUTPUT_FILENAME)
    string = pycrypt.decrypt(string, constant.KEY_FILENAME, constant.SALT_FILENAME)
    json_objects = file.loads(string)

    return json_objects


def backup_all_data():
    # Get all data from JSON files
    filenames = file.get_filenames(constant.ALL_FILENAMES)
    json_objects = file.load_json_objects(filenames)

    # Write a formatted and encrypted copy of the entire data
    string = file.dumps(json_objects)
    string = pycrypt.encrypt(string, constant.KEY_FILENAME, constant.SALT_FILENAME)
    file.write(constant.OUTPUT_FILENAME, string)


def initialize_graph():
    # Initialize graph
    graph = Digraph(name=constant.__project__, filename=constant.GRAPH_FILENAME, format=constant.GRAPH_FORMAT)
    graph.attr(rankdir=constant.RANK_DIRECTION)

    return graph


def load_data():
    # Get data from JSON files
    filenames = file.get_filenames(constant.INPUT_FILENAMES)
    json_objects = file.load_json_objects(filenames)

    # Augment data with children
    json_objects = analysis.add_children(json_objects)

    return json_objects


def print_families(json_objects, id_, generation_maximum=None):
    families = family.get_families(json_objects, id_)
    families = family.generate(families)
    families = family.process_families(json_objects, families)
    family.print_families(families, generation_maximum)


def print_genetics(json_objects, id_, generation_maximum=None):
    paths = analysis.get_paths(json_objects, id_)
    genetics = genetic.get_genetics(paths)
    genetic.print_genetics(json_objects, genetics, generation_maximum)


def print_frequencies(json_objects):
    print(f"First name frequencies: {data.get_count(json_objects, 'first_name')}")
    print(f"Last name frequencies: {data.get_count(json_objects, 'last_name')}")


def print_statistics(json_objects):
    # Print statistics
    person_count = len(json_objects)
    relationship_count = data.get_relationship_count(json_objects)
    text.print_statistics(person_count, relationship_count)


def process_data(json_objects, graph, search=None):
    if search is None:
        search = []

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

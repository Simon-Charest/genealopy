from genealopy.data import (
    get_count, get_name, get_relationship_count, get_relationship_gender,
    get_relationship_type, has_parents, is_complete, is_family
)
from genealopy.file import dump_collection, get_filenames, load_collection, loads, read, write
from genealopy.text import print_statistics
from genealopy.visual import get_color, get_style
from genealopy.analysis.analysis import add_children, get_details, get_paths, print_details
from genealopy.analysis.details import generate, process_details
from genealopy.analysis.genetic import process_genetics
from genealopy.constant import (
    __project__, ALL_FILENAMES, DARKEN_INCOMPLETE, DEBUG, KEY_FILENAME, GENDER,
    GRAPH_FILENAME, GRAPH_FORMAT, INPUT_FILENAMES, OUTPUT_FILENAME,
    RANK_DIRECTION, RELATIONSHIP, SALT_FILENAME, SEARCH_COLOR, SHAPE, STYLE
)
from genealopy.pycrypt import encrypt, decrypt
from graphviz import Digraph
from typing import Any


def run():
    """ Main execution """

    backup_all_data()
    collection: dict = load_data()
    graph = initialize_graph()

    # Highlight selected nodes
    search = []

    # TODO
    # search = ["Cécile.Lecour", "Céleste.Boulianne", "Élisabeth.Leroy", "Luce.Boily", "Lucien.Truchon",
    #           "Madeleine.Bouchard", "Madeleine2.Tremblay", "Marguerite.Labrecque", "Marguerite.Lavoie",
    #           "Marie-Judith.Simard", "Marie-Reine.Dufour", "Zoé.Pagé"]

    process_data(collection, graph, search)

    # Information display in console
    print_frequencies(collection)
    print_all_statistics(collection)
    print_genetics(collection, "Simon.Charest", 3)
    print_all_details(collection, "Simon.Charest", "last_name", minimum=1, maximum=3)
    print_all_details(collection, "Simon.Charest", "origin", "France", 0)
    print_all_details(collection, "Simon.Charest", "occupation", "Inconnu", 0)

    # Display graph
    graph.view()


def decrypt_all_data():
    # Read the formatted and encrypted copy of the entire data
    string = read(OUTPUT_FILENAME)
    string = decrypt(string, KEY_FILENAME, SALT_FILENAME)
    collection = loads(string)

    return collection


def backup_all_data() -> None:
    # Get all data from JSON files
    filenames: list = get_filenames(ALL_FILENAMES)
    collection: dict = load_collection(filenames)

    # Write a formatted and encrypted copy of the entire data
    string: str = dump_collection(collection)
    string: str = encrypt(string, open(KEY_FILENAME).read(), open(SALT_FILENAME).read())
    write(OUTPUT_FILENAME, string)


def initialize_graph() -> Digraph:
    # Initialize graph
    graph: Digraph = Digraph(name=__project__, filename=GRAPH_FILENAME, format=GRAPH_FORMAT)
    graph.attr(rankdir=RANK_DIRECTION)

    return graph


def load_data() -> dict:
    # Get data from JSON files
    filenames: str = get_filenames(INPUT_FILENAMES)
    collection: dict = load_collection(filenames)

    # Augment data with children
    collection = add_children(collection)

    return collection


def print_all_details(collection: dict, id: str, field: str, default: Any = None, minimum: int = 1, maximum: int = None) -> None:
    collection: list = get_details(collection, id, field, default)
    collection = generate(collection)
    collection = process_details(collection, minimum)
    print_details(collection, collection, id, maximum)


def print_genetics(collection, id, maximum=None) -> None:
    paths: list = get_paths(collection, id)
    paths = generate(paths)
    genetics: list = process_genetics(collection, paths)
    print_details(genetics, collection, id, maximum)


def print_frequencies(collection):
    print(f"First name frequencies: {get_count(collection, 'first_name')}")
    print(f"Last name frequencies: {get_count(collection, 'last_name')}")


def print_all_statistics(collection):
    person_count = len(collection)
    relationship_count = get_relationship_count(collection)
    print_statistics(person_count, relationship_count)


def process_data(collection: dict, graph, search=None):
    if search is None:
        search = []

    if DEBUG and "search" in locals():
        print(f"Search: {search}")

    # Loop on every person
    for key1 in collection:
        # Get first person properties
        value1 = collection[key1]
        name1 = get_name(value1)
        gender1 = value1["gender"]

        # Display nodes of certain genders only...
        if gender1 in GENDER:
            # Highlight selected persons
            if "search" in locals() and key1 in search:
                color1 = SEARCH_COLOR

            else:
                # Darken persons with missing parents but only if they are direct family
                if DARKEN_INCOMPLETE and is_family(value1) and is_complete(value1):
                    complete1 = has_parents(collection, key1)

                else:
                    complete1 = True

                color1 = get_color(gender1, complete1)

            # Draw first person
            graph.node(key1, label=name1, color=color1, shape=SHAPE, style=STYLE)

            # Loop on every relationship
            for key2 in value1["relationship"]:
                # Get second person properties
                gender2 = get_relationship_gender(collection, key2)

                # Display edges of certain genders only...
                if gender2 in GENDER:
                    # Get relationship properties
                    relationship = get_relationship_type(value1, key2)

                    # Display edges of certain relationship types only...
                    if relationship in RELATIONSHIP:

                        # Highlight relationships between selected persons
                        if "search" in locals() and key1 in search and key2 in search:
                            edge_color = SEARCH_COLOR

                        else:
                            edge_color = get_color(relationship)

                        edge_style = get_style(relationship)

                        # Draw relationship
                        graph.edge(key2, key1, color=edge_color, style=edge_style)

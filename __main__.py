from argparse import ArgumentParser, Namespace
from collections import deque
from datetime import datetime
from pathlib import Path
from typing import Any

from src.crawl import crawl
from src.datetime import get_datetime, print_execution_time
from src.delete import delete
from src.load_configuration import load_configuration
from src.read import read


def main() -> None:
    start: datetime = get_datetime()
    arguments: Namespace = parse_arguments()
    configuration: dict[str, Any] = load_configuration("config.json")

    if arguments.crawl:
        crawl(
            configuration["login_url"],
            configuration["email"],
            configuration["password"],
            configuration["url"],
            deque(configuration["references"]),
            configuration["path"],
            verbose=arguments.verbose
        )

    if arguments.delete:
        delete(str(Path(configuration["path"]).joinpath("*.html")), arguments.verbose)

    if arguments.read:
        #read(str(Path(configuration["path"]).joinpath("*.html")))
        read(str(Path(configuration["path"]).joinpath("214_227835.html")), arguments.verbose)

    """
    if arguments.backup:
        backup_all_data(configuration["paths"])

    collection: dict = load_data()

    graph = initialize_graph()

    # Highlight selected nodes
    search = [
        "Cécile.Lecour", "Céleste.Boulianne", "Élisabeth.Leroy", "Luce.Boily",
        "Lucien.Truchon", "Madeleine.Bouchard", "Madeleine2.Tremblay",
        "Marguerite.Labrecque", "Marguerite.Lavoie", "Marie-Judith.Simard",
        "Marie-Reine.Dufour", "Zoé.Pagé"
    ]

    process_data(collection, graph, search)

    # Information display in console
    print_frequencies(collection)
    print_all_statistics(collection)
    print_genetics(collection, "Simon.Charest", 3)
    print_all_details(collection, "Simon.Charest", "last_name", minimum=1, maximum=3)
    print_all_details(collection, "Simon.Charest", "origin", "France", 0)
    print_all_details(collection, "Simon.Charest", "occupation", "Inconnu", 0)

    # Display graph
    if arguments.view_graph:
        graph.view()
    """
    
    print_execution_time(start)


def parse_arguments() -> Namespace:
    argument_parser: ArgumentParser = ArgumentParser(description="Genealopy: Python genealogy database crawler")
    #argument_parser.add_argument("-b", "--backup", action="store_true", help="Backup data")
    argument_parser.add_argument("-c", "--crawl", action="store_true", help="Crawl")
    argument_parser.add_argument("-d", "--delete", action="store_true", help="Delete")
    argument_parser.add_argument("-r", "--read", action="store_true", help="Read")
    #argument_parser.add_argument("-g", "--view_graph", action="store_true", help="View graph")
    argument_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose")
    arguments: Namespace = argument_parser.parse_args()

    return arguments


if __name__ == "__main__":
    main()

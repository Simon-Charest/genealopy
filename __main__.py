from argparse import ArgumentParser, Namespace
from collections import deque
from datetime import date, datetime
from glob import glob
from pandas import DataFrame
from pathlib import Path
from sqlite3 import Connection
from typing import Any

from src.crawl import crawl
from src.datetime import get_datetime, print_execution_time
from src.delete import delete
from src.get_data import get_data
from src.load_configuration import load_configuration
from src.read import read
from src.sqlite import disconnect, get_connection, query, write


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
            configuration["encoding"],
            configuration["seconds"],
            verbose=arguments.verbose
        )

    if arguments.delete:
        delete(str(Path(configuration["path"]).joinpath("*.html")), arguments.verbose)

    if arguments.get_persons:
        persons: list[dict[str, Any]] = get_data(str(Path(configuration["path"]).joinpath("*.html")), arguments.verbose)
        #persons: list[dict[str, Any]] = get_persons(str(Path(configuration["path"]).joinpath("214_227835.html")), configuration["database"], arguments.verbose)

        # Import to database
        data_frame: DataFrame = DataFrame(persons)
        connection: Connection = get_connection(configuration["database"])
        write(data_frame, connection, "persons", "replace", False, dtype={
            "id": "INTEGER NOT NULL",
            "owner_id": "INTEGER NOT NULL",
            "first_name": "TEXT",
            "last_name": "TEXT",
            "gender": "TEXT",
            "birthdate": "TEXT",
            "birthplace": "TEXT",
            "mother_id": "INTEGER",
            "father_id": "INTEGER"
        })
        disconnect(connection)

    if arguments.list:
        paths: list[str] = glob("sql/**/*.sql", recursive=True)
        path: str
       
        for path in paths:  
            print(Path(path).as_posix())

    if arguments.query:
        sql: str = read(Path(__file__).parent.joinpath(arguments.query))
        connection: Connection = get_connection(configuration["database"])
        data: DataFrame = query(sql, connection, arguments.verbose)
        disconnect(connection)
        print(data)
        print(f"{len(data)} record(s)")

        # Prepare export path
        #file_path: Path = Path(str(arguments.query).replace("\\", "/").replace("sql/", "data/"))
        #file_path.parent.mkdir(parents=True, exist_ok=True)

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
    print("** DONE **")


def parse_arguments() -> Namespace:
    argument_parser: ArgumentParser = ArgumentParser(description="Genealopy: Python genealogy database crawler")
    #argument_parser.add_argument("-b", "--backup", action="store_true", help="Backup data")
    argument_parser.add_argument("-c", "--crawl", action="store_true", help="Crawl")
    argument_parser.add_argument("-d", "--delete", action="store_true", help="Delete")
    argument_parser.add_argument("-l", "--list", action="store_true", help="List queries")
    argument_parser.add_argument("-p", "--get_persons", action="store_true", help="Get persons")
    argument_parser.add_argument("-q", "--query", help="Query")
    #argument_parser.add_argument("-g", "--view_graph", action="store_true", help="View graph")
    argument_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose")
    arguments: Namespace = argument_parser.parse_args()

    return arguments


if __name__ == "__main__":
    main()

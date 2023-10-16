from datetime import datetime, timedelta
from genealopy.text import pluralize
from typing import Any


def get_execution_time(start: datetime, ndigits: int = 3) -> float:
    end: datetime = datetime.now()
    difference: timedelta = end - start

    return round(difference.total_seconds(), ndigits)


def get_start_time() -> datetime:
    return datetime.now()


def get_year() -> int:
    return datetime.now().year


def get_years(first_year: int) -> (int | str):
    current_year: int = get_year()
    years: int

    if current_year == first_year:
        years = current_year

    else:
        years = f"{first_year}-{current_year}"

    return years


def print_execution_time(start: datetime) -> None:
    seconds: float = get_execution_time(start)
    print(f"Execution time: {seconds} {pluralize('second', seconds)}")

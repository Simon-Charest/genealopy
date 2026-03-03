from datetime import datetime, timedelta


def get_execution_time(start: datetime, ndigits: int = 3) -> float:
    end: datetime = datetime.now()
    difference: timedelta = end - start

    return round(difference.total_seconds(), ndigits)


def get_datetime() -> datetime:
    return datetime.now()


def print_execution_time(start: datetime) -> None:
    seconds: float = get_execution_time(start)
    print(f"Execution time: {seconds} {pluralize('second', seconds)}")


def pluralize(word: str, count: float = 2) -> str:
    return word if count <= 1 else f"{word}s"

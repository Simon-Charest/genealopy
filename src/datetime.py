from datetime import date, datetime, timedelta

MONTHS: dict[str, int] = {"JAN": 1, "FEV": 2, "MAR": 3, "AVR": 4, "MAI": 5, "JUN": 6, "JUL": 7, "AOU": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}


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


def parse_date(birthdate: str) -> str:
    try:
        parts: list[str] = birthdate.strip().split()
        day: int = int(parts[0])
        month: int = MONTHS[parts[1]]
        year: int = int(parts[2])

        return date(year, month, day).isoformat()
    
    except:
        return ""

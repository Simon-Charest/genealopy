from common import text

import datetime


def get_execution_time(start, ndigits=3):
    end = datetime.datetime.now()
    difference = end - start
    return round(difference.total_seconds(), ndigits)


def get_start_time():
    return datetime.datetime.now()


def get_year():
    return datetime.datetime.now().year


def get_years(first_year):
    current_year = get_year()

    if current_year == first_year:
        years = current_year

    else:
        years = f'{first_year}-{current_year}'

    return years


def print_execution_time(start):
    seconds = get_execution_time(start)
    print(f"Execution time: {seconds} {text.pluralize('second', seconds)}")

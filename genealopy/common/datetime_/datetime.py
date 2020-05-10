import datetime


def get_year():
    return datetime.datetime.now().year


def get_years(first_year):
    current_year = get_year()

    if current_year == first_year:
        years = current_year

    else:
        years = f'{first_year}-{current_year}'

    return years

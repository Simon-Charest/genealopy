from genealopy.text import get_full_name


def process_genetics(collection, genetics):
    list_: list = []

    for genetic in genetics:
        generation = len(genetic) - 1

        if generation > 0:
            ratio = 1 / pow(2, generation)
            integer_ratio = ratio.as_integer_ratio()
            integer_ratio_string = f'{integer_ratio[0]}/{integer_ratio[1]}'
            percentage_string = f'{round(100 * ratio, 1)}%'
            id = genetic[-1]

            if id in collection:
                full_name = get_full_name(collection[id])

            else:
                full_name = id

            element = [integer_ratio_string, percentage_string, full_name, generation]
            list_.append(element)

    # Sort values by generation, then alphabetically
    list_ = sorted(list_, key=lambda values: (values[3], values[2]))

    return list_

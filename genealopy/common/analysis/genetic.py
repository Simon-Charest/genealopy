from common import text


def process_genetics(json_objects, genetics):
    list_ = list()

    for genetic in genetics:
        generation = len(genetic) - 1

        if generation > 0:
            ratio = 1 / pow(2, generation)
            integer_ratio = ratio.as_integer_ratio()
            integer_ratio_string = f'{integer_ratio[0]}/{integer_ratio[1]}'
            percentage_string = f'{round(100 * ratio, 1)}%'
            id_ = genetic[-1]

            if id_ in json_objects:
                full_name = text.get_full_name(json_objects[id_])

            else:
                full_name = id_

            element = [integer_ratio_string, percentage_string, full_name, generation]
            list_.append(element)

    # Sort values by generation, then alphabetically
    list_ = sorted(list_, key=lambda values: (values[3], values[2]))

    return list_

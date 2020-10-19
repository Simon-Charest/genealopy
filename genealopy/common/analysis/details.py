from common.analysis import analysis


def generate(generator_object):
    list_ = list()

    for element in generator_object:
        list_.append(element)

    return list_


def get_details(json_objects, start, field, default=None, path=[], details=[]):
    path = path + [start]

    if start in json_objects:
        if not details:
            if default:
                details = [default]

            else:
                details = [start]

        elif field not in json_objects[start]:
            details = details + [default]

        else:
            details = details + [json_objects[start][field]]

    yield details

    if start not in json_objects:
        return

    parents = analysis.get_parents(json_objects[start]['relationship'])

    for parent in parents:
        if parent not in path:
            yield from get_details(json_objects, parent, field, default, path, details)


def process_details(families, minimum=1):
    list_ = list()

    for family in families:
        generation = len(family) - 1

        if generation >= minimum:
            ratio = 1 / pow(2, generation)
            integer_ratio = ratio.as_integer_ratio()
            integer_ratio_string = f'{integer_ratio[0]}/{integer_ratio[1]}'
            percentage_string = f'{round(100 * ratio, 1)}%'
            last_name = family[-1]

            if not any(last_name in element for element in list_):
                element = [integer_ratio_string, percentage_string, last_name, generation]
                list_.append(element)

    # Sort values by generation, then alphabetically
    list_ = sorted(list_, key=lambda values: (values[3], values[2]))

    return list_

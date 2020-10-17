from common import text
from common.analysis import analysis


def generate(generator_object):
    list_ = list()

    for element in generator_object:
        list_.append(element)

    return list_


def get_families(json_objects, start, path=[], family=[]):
    path = path + [start]

    if start in json_objects:
        if not family:
            family = [start]

        else:
            family = family + [json_objects[start]['last_name']]

    yield family

    if start not in json_objects:
        return

    parents = analysis.get_parents(json_objects[start]['relationship'])

    for parent in parents:
        if parent not in path:
            yield from get_families(json_objects, parent, path, family)


def print_families(json_objects, families, generation_maximum=None):
    id_ = families[0][0]
    full_name = text.get_full_name(json_objects[id_])
    list_ = list()

    print('Families:')
    print(f'{full_name} is...')

    for family in families:
        generation = len(family) - 1

        if generation > 0:
            last_name = family[-1]
            ratio = 1 / pow(2, generation)
            integer_ratio = ratio.as_integer_ratio()
            integer_ratio_string = f'{integer_ratio[0]}/{integer_ratio[1]}'
            percentage_string = f'{round(100 * ratio, 1)}%'

            if not any(last_name in element for element in list_):
                element = [integer_ratio_string, percentage_string, last_name, generation]
                list_.append(element)

    # Sort values alphabetically
    list_ = sorted(list_, key=lambda values: values[2])

    # Sort values by generation
    list_ = sorted(list_, key=lambda values: values[3])

    # Print
    for element in list_:
        if generation_maximum is None or element[3] <= generation_maximum:
            print(f'{element[0]} ({element[1]}) {element[2]} (g={element[3]})')

from common import text
from common.analysis import analysis

import numpy


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


def get_unique(list_):
    return numpy.unique(list_)


def print_families(json_objects, families, generation_maximum=None):
    first_node = families[0][0]
    full_name = text.get_full_name(json_objects[first_node])

    print('Families:')
    print(f'{full_name} is...')

    for family in families:
        if family[2] <= generation_maximum:
            full_name = family[1]
            generation = family[2]
            ratio = family[3]
            integer_ratio = ratio.as_integer_ratio()
            integer_ratio_string = f'{integer_ratio[0]}/{integer_ratio[1]}'
            percentage_string = f'{round(100 * ratio, 1)}%'

            print(f'{integer_ratio_string} ({percentage_string}) {full_name} (g={generation})')


def process_families(families):
    list_ = list()

    for family in families:
        generation = len(family) - 1

        if 0 < generation:
            start_last_name = family[0]
            end_last_name = family[-1]
            ratio = 1 / pow(2, generation)

            if not any(end_last_name in element for element in list_):
                list_.append([start_last_name, end_last_name, generation, ratio])

    # Sort values alphabetically
    list_ = sorted(list_, key=lambda values: values[1])

    # Sort values by generation
    list_ = sorted(list_, key=lambda values: values[2])

    return list_

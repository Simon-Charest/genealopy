from common import text


def get_genetics(paths):
    genetics = list()

    for path in paths:
        end = path[-1]
        generation = len(path) - 1
        ratio = 1 / pow(2, generation)

        genetics.append([end, ratio, generation])

    # Sort values alphabetically
    genetics = sorted(genetics, key=lambda values: values[0])

    # Sort values by descending ratio
    genetics = sorted(genetics, key=lambda values: values[1], reverse=True)

    return genetics


def print_genetics(json_objects, genetics, generation_maximum=None):
    first_node = genetics[0][0]
    full_name = text.get_full_name(json_objects[first_node])

    print('Genetics:')
    print(f'{full_name} is...')

    for genetic in genetics:
        if genetic[1] < 1 and (generation_maximum is None or genetic[2] <= generation_maximum):
            integer_ratio = genetic[1].as_integer_ratio()
            integer_ratio_string = f'{integer_ratio[0]}/{integer_ratio[1]}'
            percentage_string = f'{round(100 * genetic[1], 1)}%'

            if genetic[0] in json_objects:
                full_name = text.get_full_name(json_objects[genetic[0]])

            else:
                full_name = genetic[0]

            generation = genetic[2]

            print(f'{integer_ratio_string} ({percentage_string}) {full_name} (g={generation})')

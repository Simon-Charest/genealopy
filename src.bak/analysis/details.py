def generate(generator_object):
    list_: list = []

    for element in generator_object:
        list_.append(element)

    return list_


def process_details(families, minimum=1):
    collection: list = []

    for family in families:
        generation = len(family) - 1

        if generation >= minimum:
            ratio = 1 / pow(2, generation)
            integer_ratio = ratio.as_integer_ratio()
            integer_ratio_string = f"{integer_ratio[0]}/{integer_ratio[1]}"
            percentage_string = f"{round(100 * ratio, 1)}%"
            last_name = family[-1]

            if not any(last_name in element for element in collection):
                element = [integer_ratio_string, percentage_string, last_name, generation]
                collection.append(element)

    # Sort values by generation, then alphabetically
    collection = sorted(collection, key=lambda values: (values[3], values[2]))

    return collection

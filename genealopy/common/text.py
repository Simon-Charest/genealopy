def get_full_name(json_object, last_name_first=False):
    first_name = json_object['first_name']
    last_name = json_object['last_name']

    if last_name_first:
        full_name = f'{last_name}, {first_name}'

    else:
        full_name = f'{first_name} {last_name}'

    return full_name


def is_none(string):
    if string is None:
        return ''

    return str(string)


def pluralize(word, count=2):
    return word if count <= 1 else f"{word}s"


def print_statistics(node_count, edge_count, node_label='family member', edge_label='relationship'):
    print('Statistics:')
    print(f'{node_count} {pluralize(node_label)}')
    print(f'{edge_count} {pluralize(edge_label)}')

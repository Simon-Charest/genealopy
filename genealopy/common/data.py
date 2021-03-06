from common import text
from common.constant import constant


def exists_in(json_object, key, value=None):
    if value:
        return key in json_object and json_object[key] == value

    else:
        return key in json_object


def get_count(json_objects, field, minimum=1):
    dictionary = {}

    for json_object in json_objects:
        if json_objects[json_object][field] in dictionary:
            dictionary[json_objects[json_object][field]] += 1

        else:
            dictionary[json_objects[json_object][field]] = 1

    # Filter values by minimal frequency
    if minimum > 1:
        dictionary = dict(filter(lambda values: values[1] >= minimum, dictionary.items()))

    # Sort values alphabetically
    sorted_list = sorted(dictionary.items(), key=lambda values: text.is_none(values[0]))

    # Sort values by descending frequency
    sorted_list = sorted(sorted_list, key=lambda values: values[1], reverse=True)

    return sorted_list


def get_gender(json_objects, id_):
    for key in json_objects:
        value = json_objects[key]

        if f"{value['first_name']}\n{value['last_name']}" == id_:
            return value['gender']

    return None


def get_name(value):
    first_name = value['first_name']
    last_name = value['last_name']

    if first_name in [None, '']:
        first_name = constant.NAME_UNKNOWN

    if last_name in [None, '']:
        last_name = constant.NAME_UNKNOWN

    return f"{first_name}\n{last_name}"


def get_node(json_objects, id_):
    # Loop on every person
    for key in json_objects:
        value = json_objects[key]

        if key == id_:
            return value

    return None


def get_relationship(node, type_):
    for key in node['relationship']:
        if node['relationship'][key]['type'] == type_:
            return key

    return None


def get_relationship_count(json_objects):
    relationship_count = 0

    for key, value in json_objects.items():
        relationship_count += len(value['relationship'])

    return relationship_count


def get_relationship_gender(json_objects, id_):
    for key in json_objects:
        value = json_objects[key]

        if key == id_:
            return f"{value['gender']}"

    return None


def get_relationship_name(json_objects, id_):
    for key in json_objects:
        value = json_objects[key]

        if key == id_:
            return f"{value['first_name']}\n{value['last_name']}"

    return None


def get_relationship_type(value, id_):
    return value['relationship'][id_]['type']


def has_parents(json_objects, key):
    relationships = json_objects[key]['relationship']
    mother = False
    father = False

    # Check if both parents are present in relationships
    for id_ in relationships:
        # Check if parent node is in graph
        if id_ not in json_objects:
            return False

        if 'mother' in relationships[id_]['type']:
            mother = True

        elif 'father' in relationships[id_]['type']:
            father = True

    return mother and father


def is_complete(value):
    if 'complete' in value:
        return value['complete']

    return True


def is_family(value):
    if 'family' in value:
        return value['family']

    return True

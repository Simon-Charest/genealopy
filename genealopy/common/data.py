from common import text
from common.constant import constant

import json


def exists_in(json_object, key, value=None):
    if value:
        return key in json_object and json_object[key] == value

    else:
        return key in json_object


def get_count(json_objects, field):
    dictionary = {}

    for json_object in json_objects:
        if json_objects[json_object][field] in dictionary:
            dictionary[json_objects[json_object][field]] += 1

        else:
            dictionary[json_objects[json_object][field]] = 1

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


def get_json_objects(filenames, encoding='utf-8'):
    json_objects = {}

    for filename in filenames:
        if constant.DEBUG:
            print(f'Filename: {filename}')

        # Read JSON data
        with open(filename, encoding=encoding) as stream:
            json_document = json.load(stream)

            if constant.DEBUG:
                print(f'JSON Document: {json_document}')

            json_objects.update(json_document)

    return json_objects


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


def has_parents(values):
    mother = False
    father = False

    for id_ in values:
        if 'mother' in values[id_]['type']:
            mother = True

        if 'father' in values[id_]['type']:
            father = True

    return mother and father


def is_complete(value):
    if 'complete' in value:
        return value['complete'] == 'true'

    return True


def is_family(value):
    if 'family' in value:
        return value['family'] == 'true'

    return True

from common.constant import constant

import glob
import json


def dump_json_objects(filename, json_objects, encoding='utf-8', ensure_ascii=False, indent=2):
    """ Write a JSON dictionary object to a file """

    with open(filename, 'w', encoding=encoding) as stream:
        json.dump(json_objects, stream, ensure_ascii=ensure_ascii, indent=indent)


def dumps(json_objects, ensure_ascii=False, indent=2):
    """ Serialize JSON dictionary object and return it as a JSON formatted string """

    return json.dumps(json_objects, ensure_ascii=ensure_ascii, indent=indent)


def get_filenames(paths, recursive=True):
    """ Get a list of filenames """

    list_ = list()

    for path in paths:
        filenames = glob.glob(path, recursive=recursive)
        list_.extend(filenames)

    return list_


def loads(string):
    """ Deserialize a JSON formatted string and return is as a JSON dictionary object  """

    json_objects = json.loads(string)

    return json_objects


def load_json_objects(filenames, encoding='utf-8'):
    """ Read a file and return its content as a JSON dictionary object """

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


def write(filename, string, encoding='utf-8'):
    """ Write to a file """

    with open(filename, 'w', encoding=encoding) as stream:
        stream.write(string)


def write_json_objects(filename, json_objects, encoding='utf-8', ensure_ascii=False):
    """ Serialize JSON dictionary object to a JSON formatted string and write it to a file """

    with open(filename, 'w', encoding=encoding) as stream:
        # Serialize JSON dictionary object to a JSON formatted string
        string = json.dumps(json_objects, ensure_ascii=ensure_ascii)

        stream.write(string)


def read(filename, encoding='utf-8'):
    """ Read from a file """

    with open(filename, 'r', encoding=encoding) as stream:
        return stream.read()

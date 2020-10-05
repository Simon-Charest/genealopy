from common.constant import constant

import glob
import json


def dump_json_objects(filename, json_objects, encoding='utf-8', ensure_ascii=False):
    with open(filename, 'w', encoding=encoding) as stream:
        json.dump(json_objects, stream, ensure_ascii=ensure_ascii)


def dumps(json_objects, ensure_ascii=False):
    return json.dumps(json_objects, ensure_ascii=ensure_ascii)


def get_filenames(paths, recursive=True):
    list_ = list()

    for path in paths:
        filenames = glob.glob(path, recursive=recursive)
        list_.extend(filenames)

    return list_


def load_json_objects(filenames, encoding='utf-8'):
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
    with open(filename, 'w', encoding=encoding) as stream:
        stream.write(string)


def write_json_objects(filename, json_objects, encoding='utf-8', ensure_ascii=False):
    with open(filename, 'w', encoding=encoding) as stream:
        # Serialize JSON dictionary object to a JSON formatted string
        string = json.dumps(json_objects, ensure_ascii=ensure_ascii)

        stream.write(string)


def read(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as stream:
        return stream.read()

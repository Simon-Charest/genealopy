from common import analysis
from common import data
from common import file
from common import test
from common.constant import constant

import app


def setup():
    # Get data from JSON files
    filenames = file.get_filenames(constant.DATA)
    json_objects = data.get_json_objects(filenames)

    # Augment data with children
    analysis.add_children(json_objects)

    return json_objects


if __name__ == '__main__':
    json_objects = setup()
    test.run(json_objects)
    app.run(json_objects)

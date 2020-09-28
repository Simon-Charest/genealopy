import glob


def get_filenames(paths):
    list_ = list()

    for path in paths:
        filenames = glob.glob(path)
        list_.extend(filenames)

    return list_

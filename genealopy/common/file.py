import glob


def get_filenames(paths, recursive=True):
    list_ = list()

    for path in paths:
        filenames = glob.glob(path, recursive=recursive)
        list_.extend(filenames)

    return list_

from genealopy.constant import ALL_FILENAMES
from genealopy.file import get_filenames


class TestGenealopy:
    def test_get_filenames(self) -> None:
        # Act
        actual: list = get_filenames(ALL_FILENAMES)

        # Assert
        assert isinstance(actual, list)
        assert len(actual) > 0

"""
from genealopy.common import file
from genealopy.common.analysis import analysis
from genealopy.common.constant import constant
from pycrypt import pycrypt
from genealopy.common import constant, file


def run():
    json_objects = load_data()
    run_tests(json_objects)


def load_data():
    # Get data from JSON files
    filenames = file.get_filenames(constant.ALL_FILENAMES)
    json_objects = file.load_json_objects(filenames)

    # Augment data with children
    json_objects = analysis.add_children(json_objects)

    return json_objects


def print_result(result, actual, expected, parameters=''):
    print(f"{result} ← {get_function_name()}({parameters})")

    if result is False:
        print(f'→ Actual: {actual}')
        print(f'→ Expected: {expected}')


def run_tests(json_objects):
    print('Unit tests:')
    test_add_children()
    test_get_shortest_path(json_objects, 'Simon.Charest', 'Dominique.Charest',
                           ['Simon.Charest', 'Michel.Charest', 'Clément.Charest', 'Hélène.Sigouin', 'Denis.Charest',
                            'Robert.Charest', 'Dominique.Charest'])
    test_get_shortest_path(json_objects, 'Aurèle.Charette', 'Jean-Baptiste3.Chorret Chaurette',
                           ['Aurèle.Charette', 'Albert.Charette', 'Servini.Charette', 'Servini2.Charette',
                            'Damase.Chauret', 'Théodore.Choret Chaurette', 'Jean-Baptiste3.Chorret Chaurette'])
    test_get_shortest_path(json_objects, 'Henriette.Charest', 'Jean-Baptiste3.Chorret Chaurette',
                           ['Henriette.Charest', 'Delphis.Charest', 'Adélard.Charest', 'Joseph.Charette',
                            'Joseph.Chorret Chaurette', 'Jean-Baptiste3.Chorret Chaurette'])
    test_get_shortest_path(json_objects, 'Delphis.Charest', 'Simon.Charest',
                           ['Delphis.Charest', 'Clément.Charest', 'Michel.Charest', 'Simon.Charest'])
    test_get_shortest_path(json_objects, 'Dominique.Charest', 'Delphis.Charest',
                           ['Dominique.Charest', 'Robert.Charest', 'Denis.Charest', 'Delphis.Charest'])
    test_get_shortest_path(json_objects, 'Simon.Charest', 'Delphis.Charest',
                           ['Simon.Charest', 'Michel.Charest', 'Clément.Charest', 'Delphis.Charest'])
    test_get_shortest_path(json_objects, 'Henriette.Charest', 'Jean-Baptiste3.Chorret Chaurette',
                           ['Henriette.Charest', 'Delphis.Charest', 'Adélard.Charest', 'Joseph.Charette',
                            'Joseph.Chorret Chaurette', 'Jean-Baptiste3.Chorret Chaurette'])
    test_pycrypt()


def test_add_children():
    actual = {
        "a": {
            "relationship": {
                "b": {"type": "mother"},
                "c": {"type": "father"}
            }
        },
        "b": {
            "relationship": {
                "c": {"type": "union"}
            }
        },
        "c": {
            "relationship": {
                "d": {"type": "mother"},
                "e": {"type": "father"},
                "b": {"type": "union"}
            }
        },
        "d": {
            "relationship": {
                "e": {"type": "union"}
            }
        },
        "e": {
            "relationship": {
                "d": {"type": "union"}
            }
        }
    }
    actual = analysis.add_children(actual)
    expected = {
        "a": {
            "relationship": {
                "b": {"type": "mother"},
                "c": {"type": "father"}
            }
        },
        "b": {
            "relationship": {
                "c": {"type": "union"},
                "a": {"type": "child"}
            }
        },
        "c": {
            "relationship": {
                "d": {"type": "mother"},
                "e": {"type": "father"},
                "b": {"type": "union"},
                "a": {"type": "child"}
            }
        },
        "d": {
            "relationship": {
                "e": {"type": "union"},
                "c": {"type": "child"}
            }
        },
        "e": {
            "relationship": {
                "d": {"type": "union"},
                "c": {"type": "child"}
            }
        }
    }
    result = actual == expected
    print_result(result, actual, expected, '[a, b, c, d, e]')


def test_get_shortest_path(json_objects, start, end, expected):
    actual = analysis.get_shortest_path(json_objects, start, end)
    result = actual == expected
    print_result(result, actual, expected, f"'{start}', '{end}'")


def test_pycrypt():
    expected = 'Secret message'
    key = 'Th1s 1s an 3ncrypt10n k3y.'
    salt = 'Why so salty?'
    actual = pycrypt.decrypt(pycrypt.encrypt(expected, key, salt), key, salt)
    result = actual == expected
    print_result(result, actual, expected)
"""

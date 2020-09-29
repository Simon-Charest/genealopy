from common import analysis
from common import text
from common.constant import constant
from common.datetime_ import datetime_

import datetime
import inspect
import json


def run(json_objects):
    # Unit tests test_get_shortest_path function
    print('Unit tests:')
    start = datetime.datetime.now()
    test_add_children()
    test_get_shortest_path(json_objects, 'Simon.Charest', 'Dominique.Charest', [['Simon.Charest', 'Michel.Charest', 'Clément.Charest', 'Hélène.Sigouin', 'Denis.Charest', 'Robert.Charest', 'Dominique.Charest'], ['Simon.Charest', 'Michel.Charest', 'Clément.Charest', 'Delphis.Charest', 'Denis.Charest', 'Robert.Charest', 'Dominique.Charest']])
    test_get_shortest_path(json_objects, 'Aurèle.Charette', 'Jean-Baptiste3.Chorret Chaurette', [['Aurèle.Charette', 'Albert.Charette', 'Servini.Charette', 'Servini2.Charette', 'Damase.Chauret', 'Théodore.Choret Chaurette', 'Jean-Baptiste3.Chorret Chaurette']])
    test_get_shortest_path(json_objects, 'Henriette.Charest', 'Jean-Baptiste3.Chorret Chaurette', [['Henriette.Charest', 'Delphis.Charest', 'Adélard.Charest', 'Joseph.Charette', 'Joseph.Chorret Chaurette', 'Jean-Baptiste3.Chorret Chaurette']])
    test_get_shortest_path(json_objects, 'Delphis.Charest', 'Simon.Charest', [['Delphis.Charest', 'Clément.Charest', 'Michel.Charest', 'Simon.Charest']])
    test_get_shortest_path(json_objects, 'Dominique.Charest', 'Delphis.Charest', [['Dominique.Charest', 'Robert.Charest', 'Denis.Charest', 'Delphis.Charest']])
    test_get_shortest_path(json_objects, 'Simon.Charest', 'Delphis.Charest', [['Simon.Charest', 'Michel.Charest', 'Clément.Charest', 'Delphis.Charest']])
    test_get_shortest_path(json_objects, 'Henriette.Charest', 'Jean-Baptiste3.Chorret Chaurette', [['Henriette.Charest', 'Delphis.Charest', 'Adélard.Charest', 'Joseph.Charette', 'Joseph.Chorret Chaurette', 'Jean-Baptiste3.Chorret Chaurette']])
    datetime_.print_execution_time(start)
    print('\n')


def test_add_children():
    dictionary = {
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
    dictionary = analysis.add_children(dictionary)
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
    result = dictionary == expected
    function_name = inspect.currentframe().f_code.co_name
    print(f"{result} <= {function_name}([a, b, c, d, e])")


def test_get_shortest_path(json_objects, start, end, expected):
    shortest_path = analysis.get_shortest_path(json_objects, start, end)

    if constant.DEBUG:
        print(shortest_path)

    result = shortest_path in expected
    function_name = inspect.currentframe().f_code.co_name
    print(f"{result} <= {function_name}('{start}', '{end}')")

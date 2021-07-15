import json
from typing import Any

import pytest

from boj import BOJProblem


def test_BOJProblem_readonly_properties():
    problem = BOJProblem(1000)

    # Test read only properties
    assert isinstance(problem.url, str)
    assert problem.url == 'https://www.acmicpc.net/problem/1000'
    with pytest.raises(AttributeError):
        problem.url = 'https://www.acmicpc.net/problem/1001'

    assert isinstance(problem.data, list)
    assert isinstance(problem.data[0], dict)
    with pytest.raises(AttributeError):
        problem.data = []

    assert isinstance(problem.json, bytes)
    assert problem.data == json.loads(problem.json)
    with pytest.raises(AttributeError):
        problem.json = b'[{\'problem_id\': \'localhost\'}}]'

    assert isinstance(problem.problem_id, int)
    assert problem.problem_id == 1000
    with pytest.raises(AttributeError):
        problem.problem_id = 1001

    assert isinstance(problem.title, str)
    assert problem.title == 'A+B'
    with pytest.raises(AttributeError):
        problem.title = 'Lorem ipsum'

    assert isinstance(problem.description, str)
    with pytest.raises(AttributeError):
        problem.description = 'Lorem ipsum'

    assert isinstance(problem.input, str)
    with pytest.raises(AttributeError):
        problem.input = 'Lorem ipsum'

    assert isinstance(problem.output, str)
    with pytest.raises(AttributeError):
        problem.output = 'Lorem ipsum'

    assert isinstance(problem.hint, str)
    with pytest.raises(AttributeError):
        problem.hint = 'Lorem ipsum'

    assert isinstance(problem.original, int)
    assert isinstance(problem.html_title, int)
    assert isinstance(problem.problem_lang_tcode, str)

    for key, value in problem.document.items():
        assert isinstance(key, str)
        assert isinstance(value, str)

from collections import deque
from typing import Deque

from boj.python.core.classes.TestCase import TestCase
from boj.python.core.definition_groups.type_aliases import _Path, _MiliSeconds, _MegaBytes


class ScoringCriteria:
    def __init__(self) -> None:
        self._input_type: str = ''
        self._output_type: str = ''
        self._time_limit: _MiliSeconds = 0
        self._memory_limit: _MegaBytes = 0
        self._test_case_queue: Deque[TestCase] = deque()

    @property
    def input_type(self) -> str:
        return self._input_type

    @input_type.setter
    def input_type(self, input_type: str) -> None:
        self._input_type = input_type

    @property
    def output_type(self) -> str:
        return self._output_type

    @output_type.setter
    def output_type(self, output_type: str) -> None:
        self._output_type = output_type

    @property
    def time_limit(self) -> float:
        return self._time_limit

    @time_limit.setter
    def time_limit(self, time_limit: _MiliSeconds) -> None:
        self._time_limit = time_limit

    @property
    def memory_limit(self) -> float:
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit: _MegaBytes) -> None:
        self._memory_limit = memory_limit

    @property
    def test_case_queue(self) -> Deque[TestCase]:
        return self._test_case_queue

    def add_test_case(self, input_file: _Path, output_file: _Path) -> None:
        tc = TestCase()
        tc.input_file = input_file
        tc.output_file = output_file
        self.test_case_queue.append(tc)

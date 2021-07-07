from boj.python.core.definition_groups.type_aliases import _Path, _JudgeResultCode


class TestCase:
    def __init__(self) -> None:
        self._input_file: _Path = ''
        self._output_file: _Path = ''

    @property
    def input_file(self) -> _Path:
        return self._input_file

    @input_file.setter
    def input_file(self, input_file: _Path) -> None:
        self._input_file = input_file

    @property
    def output_file(self) -> _Path:
        return self._output_file

    @output_file.setter
    def output_file(self, output_file: _Path) -> None:
        self._output_file = output_file

    def run_test(self, code_file: _Path) -> _JudgeResultCode:
        raise NotImplementedError()

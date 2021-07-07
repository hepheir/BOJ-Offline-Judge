from boj.python.core.classes.ScoringCriteria import ScoringCriteria
from boj.python.core.definition_groups.type_aliases import _Document, _Path, _JudgeResultCode


class BaseProblem:
    def __init__(self) -> None:
        self._title: str = ''
        self._criteria: ScoringCriteria = ScoringCriteria()
        self._document: _Document = dict()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title) -> None:
        self._title = title

    @property
    def criteria(self) -> ScoringCriteria:
        return self._criteria

    @property
    def document(self) -> _Document:
        return self._document

    def run_all_tests(self, code_file: _Path) -> _JudgeResultCode:
        raise NotImplementedError()

    def save(self, directory: _Path) -> None:
        raise NotImplementedError()

    def load(self, directory: _Path) -> None:
        raise NotImplementedError()

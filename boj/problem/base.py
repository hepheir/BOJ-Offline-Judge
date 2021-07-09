from typing import Dict


class BaseProblem:
    def __init__(self) -> None:
        self._id: str = ''
        self._document: Dict[str, str] = dict()

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str) -> None:
        self._id = value

    @property
    def document(self) -> Dict[str, str]:
        return self._document

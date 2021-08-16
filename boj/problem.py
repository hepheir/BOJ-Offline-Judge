
from abc import ABCMeta, abstractmethod
from typing import Optional


from boj.document import Document, BOJDocument, browse_boj_document_from_web


class Problem(metaclass=ABCMeta):
    @property
    @abstractmethod
    def id(self) -> str:
        ...

    @id.setter
    @abstractmethod
    def id(self, value: str) -> None:
        ...

    @property
    @abstractmethod
    def document(self) -> Document:
        ...


LANGUAGE_KOREAN = "0"
LANGUAGE_ENGLISH = "1"

class BOJProblem(Problem):
    def __init__(self, number: int, language: Optional[str] = LANGUAGE_KOREAN) -> None:
        self._problem_url = f"https://www.acmicpc.net/problem/{number:d}"
        self._documents = browse_boj_document_from_web(self._problem_url)
        self.lang = language

    @property
    def id(self) -> str:
        return self._problem_url

    @property
    def document(self) -> BOJDocument:
        return self._documents[self.lang]


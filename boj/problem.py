from abc import ABCMeta, abstractmethod

from boj.document import Document, BOJDocument
from boj.api.net.acmicpc import get_problem_data, get_problem_url


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
    def __init__(self,
                 number: int,
                 language: str = LANGUAGE_KOREAN,
                 use_cache: bool = True) -> None:
        self.lang = language
        self._problem_url = get_problem_url(boj_problem_number=number)
        self._documents = {}
        for data in get_problem_data(boj_problem_number=number,
                                     use_cache=use_cache):
            lang_code = data['problem_lang']
            self._documents[lang_code] = BOJDocument(**data)

    @property
    def id(self) -> str:
        return self._problem_url

    @property
    def document(self) -> BOJDocument:
        return self._documents[self.lang]

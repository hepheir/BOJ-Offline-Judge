import base64
import json
from typing import Dict, List

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import request


class BaseProblem:
    def __init__(self, id: str) -> None:
        self._id: str = id
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


class BOJProblem(BaseProblem):
    LANGUAGE_KOREAN = 0
    LANGUAGE_ENGLISH = 1

    def __init__(self, number: int, language: int = 0) -> None:
        # Use problem url as id
        self._url = f'https://www.acmicpc.net/problem/{number:d}'
        super().__init__(id=self._url)
        self._language: int = language
        self._data: List[Dict[str, str]]
        self._set_data()
        # Use Korean as default language
        if self._language >= len(self._data):
            self._language = self.LANGUAGE_KOREAN
        # Make document aliases
        for key, value in self._data[self._language].items():
            self._document[key] = value

    def _set_data(self) -> List[Dict[str, str]]:
        """백준 온라인 저지로 부터 문제 데이터를 읽어옵니다.

        문제 페이지에서 base64 인코딩 형태로 저장된 json 데이터를 사용합니다.
        데이터는 리스트로 이루어져 있으며, 각 원소는 언어별 문제 데이터를 담고 있습니다.
        """
        response = request('GET', self._url)
        text_html = response.text
        soup = BeautifulSoup(text_html, 'html.parser')
        soup_tag: Tag = soup.select_one('#problem-lang-base64')  # type: ingore
        text_base64 = soup_tag.text
        text_json = base64.b64decode(text_base64)
        data_dict = json.loads(text_json)
        self._data = data_dict

    @property
    def data(self) -> List[Dict[str, str]]:
        return self._data

    @property
    def problem_id(self) -> int:
        return int(self._document['problem_id'])

    @property
    def problem_lang(self) -> int:
        return int(self._document['problem_lang'])

    @property
    def title(self) -> str:
        return self._document['title']

    @property
    def description(self) -> str:
        return self._document['description']

    @property
    def input(self) -> str:
        return self._document['input']

    @property
    def output(self) -> str:
        return self._document['output']

    @property
    def hint(self) -> str:
        return self._document['hint']

    @property
    def original(self) -> int:
        return int(self._document['original'])

    @property
    def html_title(self) -> int:
        return int(self._document['html_title'])

    @property
    def problem_lang_tcode(self) -> str:
        return self._document['problem_lang_tcode']

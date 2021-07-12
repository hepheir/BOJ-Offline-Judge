import base64
import json
from typing import Dict, List

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import request

from boj.problem.base import BaseProblem


class Language:
    KOREAN = 0
    ENGLISH = 1


class BOJProblem(BaseProblem):
    def __init__(self, number:int, language:int=0) -> None:
        super().__init__()
        self._data: List[Dict[str, str]] = _get_problem_data(number)
        self._language: int = language if language < len(self._data) else Language.KOREAN
        for key, value in self._data[self._language].items():
            self._document[key] = value

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


def _get_problem_data(problem_id: int) -> List[Dict[str, str]]:
    """백준 온라인 저지로 부터 문제 데이터를 읽어옵니다.

    문제 페이지에서 base64 인코딩 형태로 저장된 json 데이터를 사용합니다.
    데이터는 리스트로 이루어져 있으며, 각 원소는 언어별 문제 데이터를 담고 있습니다.

    Args:
        problem_id: 데이터를 가져올 문제의 번호입니다

    Returns:
        문제 데이터를 반환합니다.
    """
    response = request('GET', f'https://www.acmicpc.net/problem/{problem_id:d}')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    tag:Tag = soup.select_one('#problem-lang-base64') #type: ingore
    data_base64 = tag.text
    data_json = base64.b64decode(data_base64)
    data_dict = json.loads(data_json)
    return data_dict

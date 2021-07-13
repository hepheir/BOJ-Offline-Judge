import base64
import json
from textwrap import dedent
from typing import Dict, List, Optional

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import request
from requests.sessions import InvalidSchema


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

    def __init__(self, number: int, language: Optional[int] = None) -> None:
        self._json: str
        self._data: List[Dict[str, str]]
        super().__init__(
            id=f"https://www.acmicpc.net/problem/{number:d}"
        )
        self._load_data(language)

    @property
    def url(self) -> str:
        return self.id

    @property
    def data(self) -> List[Dict[str, str]]:
        return self._data

    @property
    def json(self) -> str:
        return self._json

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

    def _load_data(self, language: Optional[int] = None) -> None:
        """백준 온라인 저지로 부터 문제 데이터를 읽어옵니다.

        문제 페이지에서 base64 인코딩 형태로 저장된 json 데이터를 사용합니다.
        데이터는 리스트로 이루어져 있으며, 각 원소는 언어별 문제 데이터를 담고 있습니다.
        """
        if language is None:
            language = self.LANGUAGE_KOREAN
        try:
            response = request('GET', self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            soup_tag: Tag = soup.select_one(
                '#problem-lang-base64')  # type: ingore
            if soup_tag is None:
                raise Exception
            text_base64 = soup_tag.text
            text_json = base64.b64decode(text_base64)
            dict_data = json.loads(text_json)
            if not dict_data:
                raise Exception
        except InvalidSchema:
            raise InvalidSchema(dedent('''
                URL 스키마가 올바르지 않습니다.
                올바른 프로토콜(http, https)을 사용중인지 확인하세요.
            '''))
        except ConnectionError:
            raise ConnectionError(dedent('''
                URL로 부터 데이터를 읽어올 수 없습니다.
                {url}
            '''.format(url=self._url)))
        except Exception as exception:
            raise Exception(dedent('''
                    문제 데이터를 읽어올 수 없습니다.
                    백준 온라인 저지의 사이트 구조가 변경되었거나,
                    주소가 이전 되었을 수도 있습니다.
                '''),
                exception
            )
        finally:
            self._json = text_json
            self._data = dict_data
            self._language = language
            self._document.clear()
            for key, value in dict_data[language].items():
                self._document[key] = value

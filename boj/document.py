from __future__ import annotations

import base64
import json
from dataclasses import dataclass, field
from textwrap import dedent
from typing import Dict, List, Union

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import request
from requests.sessions import InvalidSchema


class Document(dict):
    pass


@dataclass
class BOJDocument:
    problem_id: str
    title: str
    description: str = field(default='')
    input: str = field(default='')
    output: str = field(default='')
    hint: str = field(default='')
    original: str = field(default='')
    html_title: str = field(default='')
    problem_lang: str = field(default='')
    problem_lang_tcode: str = field(default='')



def browse_boj_document_from_web(boj_problem_url: str) -> Dict[str, BOJDocument]:
    """백준 온라인 저지로 부터 문제 데이터를 읽어옵니다.

    문제 페이지에서 base64 인코딩 형태로 저장된 json 데이터를 사용합니다.
    데이터는 리스트로 이루어져 있으며, 각 원소는 언어별 문제 데이터를 담고 있습니다.
    """
    try:
        response = request(method='GET', url=boj_problem_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Base64 인코딩 되어있는 문제 JSON 데이터를 담고 있는 태그를 검색한다.
        soup_tag: Union[Tag, None]
        soup_tag = soup.select_one('#problem-lang-base64')
        if soup_tag is None:
            raise Exception

        # 가져온 데이터를 JSON에서 Python - dict 형식으로 변환한다.
        boj_prob_data: List[Dict[str, str]]
        boj_prob_data = json.loads(base64.b64decode(soup_tag.text))
        if not boj_prob_data:
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
        '''.format(url=boj_problem_url)))

    except Exception as exception:
        raise Exception(dedent('''
            문제 데이터를 읽어올 수 없습니다.
            백준 온라인 저지의 사이트 구조가 변경되었거나,
            주소가 이전 되었을 수도 있습니다.
        '''), exception)

    finally:
        pass

    retval = {}
    for data in boj_prob_data:
        lang_code = data['problem_lang']
        retval[lang_code] = BOJDocument(**data)
    return retval

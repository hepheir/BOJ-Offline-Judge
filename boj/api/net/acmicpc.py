import base64
import json
from textwrap import dedent
from typing import Dict, List, Union

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import request
from requests.sessions import InvalidSchema


_CACHED_PAGES = {}


def get_problem_url(boj_problem_number: int) -> str:
    """문제 번호로 부터 백준 온라인 저지에서의 문제 URL을 조합합니다.

    Args:
        boj_problem_number: (int) 문제 번호

    Returns:
        문제를 볼 수 있는 URL 주소
    """
    return f"https://www.acmicpc.net/problem/{boj_problem_number:d}"


def get_problem_page_html(boj_problem_number: int,
                          use_cache: bool = True) -> str:
    """백준 온라인 저지로 부터 문제 페이지 HTML을 불러옵니다.

    `use_cache` 값을 `False`로 설정하거나, 이전에 같은 페이지를 불러온 적이 없다면,
    백준 온라인 저지로 부터 최신 페이지 정보를 불러옵니다.

    Args:
        boj_problem_number: (int) 문제 번호
        use_cache: (bool) 웹페이지 캐시 사용 여부

    Returns:
        문제 페이지의 HTML 문서를 텍스트로 반환한다.
    """
    boj_problem_url = get_problem_url(boj_problem_number)

    if use_cache and boj_problem_url in _CACHED_PAGES:
        return _CACHED_PAGES[boj_problem_url]

    try:
        response = request(method='GET', url=boj_problem_url)
    except InvalidSchema:
        raise InvalidSchema(dedent('''
            URL 스키마가 올바르지 않습니다.
            올바른 프로토콜(http, https)을 사용중인지 확인하세요.
            [{url}]
        '''.format(url=boj_problem_url)))
    except ConnectionError:
        raise ConnectionError(dedent('''
            인터넷에 연결할 수 없습니다.
            네트워크 상태를 확인하세요.
        '''))
    except Exception as exception:
        raise Exception(dedent('''
            문제 데이터를 읽어올 수 없습니다.
            백준 온라인 저지의 사이트 구조가 변경되었거나,
            주소가 이전 되었을 수도 있습니다.
        '''), exception)
    if use_cache:
        _CACHED_PAGES[boj_problem_url] = response.text
    return response.text


def get_problem_data(boj_problem_number: int,
                     use_cache: bool = True) -> List[Dict[str, str]]:
    """백준 온라인 저지로 부터 문제 데이터를 읽어옵니다.

    문제 페이지에서 base64 인코딩 형태로 저장된 json 데이터를 사용합니다.
    데이터는 리스트로 이루어져 있으며, 각 원소는 언어별 문제 데이터를 담고 있습니다.

    `use_cache` 값을 `False`로 설정하거나, 이전에 같은 페이지를 불러온 적이 없다면,
    백준 온라인 저지로 부터 최신 페이지 정보를 불러와 가공합니다.

    Args:
        boj_problem_number: (int) 문제 번호
        use_cache: (bool) 웹페이지 캐시 사용 여부

    Returns:
        문제에 대한 정보를 담고있는 딕셔너리의 리스트
    """
    html = get_problem_page_html(boj_problem_number=boj_problem_number,
                                use_cache=use_cache)
    soup = BeautifulSoup(html, 'html.parser')

    # Base64 인코딩 되어있는 문제 JSON 데이터를 담고 있는 태그를 검색한다.
    soup_tag: Union[Tag, None]
    soup_tag = soup.select_one('#problem-lang-base64')
    if soup_tag is None:
        raise Exception

    # 가져온 데이터를 JSON에서 Python - dict 형식으로 변환한다.
    boj_prob_data: List[Dict[str, str]]
    boj_prob_data = json.loads(base64.b64decode(soup_tag.text))
    if not boj_prob_data:
        raise Exception(dedent('''
            문제 데이터를 읽어올 수 없습니다.
            백준 온라인 저지의 사이트 구조가 변경되었거나,
            주소가 이전 되었을 수도 있습니다.
        '''))

    return boj_prob_data

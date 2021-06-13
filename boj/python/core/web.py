"""web.py에서는 웹으로 부터 데이터를 받아오고 처리하기 위한 인터페이스를 제공합니다.
받아온 HTML 문서를 파싱하고 다룹니다.
"""

from typing import Callable
import requests

class Crawler:
    @classmethod
    def get(cls, url: str) -> str:
        html = requests.get(url).text
        return str(html)


class HTMLElement:
    inner_HTML: str
    to_markdown: Callable[[], str]



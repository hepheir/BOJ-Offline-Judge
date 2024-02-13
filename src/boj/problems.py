from __future__ import annotations

import dataclasses

import bs4
import requests

import boj.persistence


__database__ = boj.persistence.Database('problems')


@dataclasses.dataclass
class Problem:
    id: int
    title: str
    description: str
    input: str
    output: str


def get(id: str | int) -> Problem:
    id = str(id)
    if id not in __database__:
        update(id)
    return __database__[id]


def update(id: str | int) -> Problem:
    id = str(id)
    __database__[id] = _get_web_snapshot(id)
    __database__.sync()
    return __database__[id]


def _get_web_snapshot(id: str) -> Problem:
    def inner_html(tag: bs4.Tag) -> str:
        return ''.join(map(str, tag.contents)).strip()
    url = 'https://www.acmicpc.net/problem/%s' % id
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0' }
    html = requests.get(url, headers=headers).text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return Problem(
        id=int(id),
        title=soup.select_one('span#problem_title').get_text(strip=True),
        description=inner_html(soup.select_one('div#problem_description')),
        input=inner_html(soup.select_one('div#problem_input')),
        output=inner_html(soup.select_one('div#problem_output')),
    )

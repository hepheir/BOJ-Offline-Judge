from __future__ import annotations

import dataclasses
import functools
import types
import typing

import bs4
import requests

import boj.persistence


__database__ = boj.persistence.Database('tags')


@dataclasses.dataclass
class Tag:
    id: int
    name_ko: str
    name_en: str
    count: int


def get(id: str | int) -> Tag:
    id = str(id)
    if id not in __database__:
        update(id)
    return __database__[id]


def update(id: str | int) -> Tag:
    id = str(id)
    __database__[id] = _get_web_snapshot()[id]
    __database__.sync()
    return __database__[id]


@functools.cache
def _get_web_snapshot() -> typing.Dict[str, Tag]:
    data = {}
    url = 'https://www.acmicpc.net/problem/tags'
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0' }
    html = requests.get(url, headers=headers).text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for tr in soup.select('body > div.wrapper > div.container.content > div:nth-child(5) > div > div > table > tbody > tr'):
        entity = Tag(
            id=int(tr.select_one('a').attrs['href'].split('/')[-1]),
            name_ko=tr.select_one('td:nth-child(1)').get_text(strip=True),
            name_en=tr.select_one('td:nth-child(2)').get_text(strip=True),
            count=int(tr.select_one('td:last-child').get_text(strip=True)),
        )
        data[str(entity.id)] = entity
    return types.MappingProxyType(data)

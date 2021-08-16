from __future__ import annotations

from dataclasses import dataclass, field


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

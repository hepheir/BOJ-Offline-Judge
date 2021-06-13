from __future__ import annotations
from typing import Callable

from boj.python.core.web import HTMLElement


class Document:
    title: str
    desc: HTMLElement
    input: HTMLElement
    output: HTMLElement
    hint: HTMLElement


class Rule:
    judge_method: int
    time_limit: float
    memory_limit: float


class Problem:
    number: int
    document: Document
    rule: Rule

    save: Callable[[str], None]
    load: Callable[[str], None]

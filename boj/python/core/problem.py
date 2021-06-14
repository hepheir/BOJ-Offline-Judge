from __future__ import annotations

import dataclasses
from typing import Callable

from boj.python.core.web import HTMLElement


@dataclasses.dataclass
class Document:
    desc: HTMLElement
    input: HTMLElement
    output: HTMLElement
    hint: HTMLElement


@dataclasses.dataclass
class Rule:
    # Definition Group JudgeMethod
    DEFAULT = 1
    SPECIAL_JUDGE = 2

    judge_method: int
    time_limit: float
    memory_limit: float


class Problem:
    number: int
    title: str
    document: Document
    rule: Rule

    save: Callable[[str], None]
    load: Callable[[str], None]

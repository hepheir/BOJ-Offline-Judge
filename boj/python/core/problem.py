from __future__ import annotations

import dataclasses
from typing import Callable, Optional, overload

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

    judge_method: int = dataclasses.field(default=None)
    time_limit: float = dataclasses.field(default=None)
    memory_limit: float = dataclasses.field(default=None)

@dataclasses.dataclass
class Problem:
    def __init__(self) -> None:
        self.number: Optional[int] = None
        self.title: Optional[str] = None
        self.document: Document = Document()
        self.rule: Rule = Rule()

    save: Callable[[str], None]

    @overload
    def load(self) -> None:
        """문제 정보를 백준 온라인 저지로 부터 불러옵니다.

        문제를 불러오기 위해서는 문제의 번호가 반드시 주어져야 합니다.
        문제의 번호가 주어지지 않은 상태로 불러오기를 시도할 경우 `AssertionError`를 발생시킵니다.

        Raises:
            AssertionError: 문제 번호가 올바르지 않거나 존재하지 않으면 발생.
        """
        ...

    @overload
    def load(self, path: str) -> None:
        """문제 정보를 `path`에 해당하는 경로로 부터 불러옵니다.

        문제 정보는 반드시 다음의 형식에 맞게 저장되어 있어야 합니다.
        ```text
            path/
            ├─ info.json
            ├─ rule.json
            ├─ document/
            │  ├─ desc.html
            │  ├─ input.html
            │  ├─ output.html
            │  └─ hint.html
            └─ data/
                ├─ sample-1.in
                ├─ sample-1.out
                └─ ...
        ```

        Raises:
            FileNotFoundError: `path`로 부터 파일을 찾지 못하였을 때 발생.
        """
        ...

    def load(self, path: Optional[str] = None) -> None:
        if path is None:
            return self._load_from_web()
        else:
            return self._load_from_local(path)

    def _load_from_web(self) -> None:
        # TODO
        pass

    def _load_from_local(self, path: str) -> None:
        # TODO
        pass

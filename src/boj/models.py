import dataclasses

from typing import List


@dataclasses.dataclass
class ProblemDTO:
    id: int
    title: str
    sections: List['SectionDTO'] = dataclasses.field(default_factory=list)
    testcases: List['TestCaseDTO'] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class TestCaseDTO:
    name: str
    input: str
    output: str


@dataclasses.dataclass
class SectionDTO:
    name: str
    text: str

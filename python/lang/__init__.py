import os
import typing

from . import Cpp
from . import Python3


AVAILABLE_LANGUAGES = [Cpp, Python3]


class LanguageNotSupported(BaseException): pass


class BaseLanguage:
    EXTENSION: str
    COMPILE: typing.List[str]
    RUN: typing.List[str]


def detect_language(src: os.PathLike) -> BaseLanguage:
    ext = '.'+src.split('.')[-1]
    for language in AVAILABLE_LANGUAGES:
        if language.EXTENSION == ext:
            return language
    raise LanguageNotSupported()

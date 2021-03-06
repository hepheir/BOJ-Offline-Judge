import pathlib

from boj.lang.BaseLanguage import BaseLanguage
from boj.lang.Cpp import Cpp
from boj.lang.Python3 import Python3


AVAILABLE_LANGUAGES = [Cpp, Python3]


class LanguageNotSupported(BaseException):
    pass


def detect_language(src: pathlib.Path) -> BaseLanguage:
    ext = '.'+str(src).split('.')[-1]
    for language in AVAILABLE_LANGUAGES:
        if language.EXTENSION == ext:
            return language
    raise LanguageNotSupported()

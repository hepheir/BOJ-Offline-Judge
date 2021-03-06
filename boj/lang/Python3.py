import pathlib
import typing

from boj.lang import BaseLanguage


class Python3(BaseLanguage):
    EXTENSION = '.py'

    def compile(src:pathlib.Path, *args, **kwargs) -> typing.List[str]:
        src = src.replace('\\','/')
        return [ "python3", "-c", f"import py_compile; py_compile.compile('{src}')" ]

    def run(src:pathlib.Path, *args, **kwargs) -> typing.List[str]:
        src = src.replace('\\','/')
        return [ "python3", src ]

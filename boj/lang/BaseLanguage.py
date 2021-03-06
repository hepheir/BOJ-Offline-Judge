import pathlib
import typing


class BaseLanguage:
    EXTENSION: str

    def compile(src:pathlib.Path, *args, **kwargs) -> typing.List[str]:
        pass

    def run(src:pathlib.Path, *args, **kwargs) -> typing.List[str]:
        pass

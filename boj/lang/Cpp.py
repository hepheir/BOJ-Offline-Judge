import typing

from boj.config import config
from boj.lang import BaseLanguage
from boj.util import temp_filename

__COMPILER = config['language']['cpp.compilerPath']
__EXECUTABLE_FILE = temp_filename('.exe')


class Cpp(BaseLanguage):
    EXTENSION = '.cpp'

    def compile(src, *args, **kwargs) -> typing.List[str]:
        return [__COMPILER, "-g", src, "-o", __EXECUTABLE_FILE]

    def run(*args, **kwargs) -> typing.List[str]:
        return [__EXECUTABLE_FILE]

import os
import sys

PACKAGE_ROOT = os.path.dirname(sys.modules['boj'].__file__)


class units:
    class ms(int):
        pass

    class KB(int):
        pass


def shorten_path(path:str):
    abspath = os.path.abspath(path)
    common_path = os.path.commonpath([abspath, os.getcwd()])
    return abspath.replace(common_path, "")

import os
import sys

PACKAGE_ROOT = os.path.dirname(sys.modules['boj'].__file__)


class units:
    class ms(int):
        pass

    class KB(int):
        pass


def shorten_path(path:str):
    common_path = os.path.commonpath([path, os.getcwd()])
    return path.replace(common_path, "")

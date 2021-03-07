import pathlib
import os
import shutil

from boj.config import config


tempDirname = config.get('user', 'path.temp.dirname')


def shorten_path(path: pathlib.Path):
    abspath = os.path.abspath(path)
    return abspath.replace(os.path.commonpath([abspath, os.getcwd()]), "")


if not os.path.exists(tempDirname):
    os.makedirs(tempDirname)

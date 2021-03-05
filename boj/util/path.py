from boj.util import TMP_DIRECTORY
import pathlib
import os
import shutil

from boj.config import config

TEMP_DIRECTORY = config.get('Paths', 'tempDirectory')


def shorten_path(path: pathlib.Path):
    abspath = os.path.abspath(path)
    return abspath.replace(os.path.commonpath([abspath, os.getcwd()]), "")


def temp_filename(file: pathlib.Path) -> pathlib.Path:
    ext = file.split('.')[-1]
    return os.path.join(TEMP_DIRECTORY, ext)


def temp_makecopy(file: pathlib.Path) -> pathlib.Path:
    tempfile = temp_filename(file)
    shutil.copy(file, tempfile)
    return tempfile


if not os.path.exists(TEMP_DIRECTORY):
    os.makedirs(TEMP_DIRECTORY)

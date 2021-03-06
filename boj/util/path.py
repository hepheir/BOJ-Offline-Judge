import pathlib
import os
import shutil

from boj.config import config

TEMP_DIRECTORY = config['path']['tempDirectory']


def shorten_path(path: pathlib.Path):
    abspath = os.path.abspath(path)
    return abspath.replace(os.path.commonpath([abspath, os.getcwd()]), "")


def temp_filename(file: pathlib.Path) -> pathlib.Path:
    ext = '.'+str(file).split('.')[-1]
    return os.path.join(TEMP_DIRECTORY, ext)


def temp_makecopy(file: pathlib.Path) -> pathlib.Path:
    tempfile = temp_filename(file)
    shutil.copy(file, tempfile)
    return tempfile


def temp_makefile(file: pathlib.Path) -> pathlib.Path:
    tempfile = temp_filename(file)
    with open(tempfile, 'w'):
        pass
    return tempfile


def temp_exists(file: pathlib.Path) -> bool:
    tempfile = temp_filename(file)
    return os.path.exists(tempfile)


if not os.path.exists(TEMP_DIRECTORY):
    os.makedirs(TEMP_DIRECTORY)

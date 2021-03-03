import os

from .. import config

EXTENSION = '.cpp'

__CONFIG_TMP_DIRECTORY = config.from_json('tmp.directory')
__CONFIG_COMPILER_PATH = config.from_json('cpp.compiler.path')

__SOURCE_FILE = os.path.join(__CONFIG_TMP_DIRECTORY, EXTENSION)
__EXECUTABLE_FILE = os.path.join(__CONFIG_TMP_DIRECTORY, '.exe')

COMPILE = [ __CONFIG_COMPILER_PATH, "-g", __SOURCE_FILE, "-o", __EXECUTABLE_FILE ]
RUN = [ __EXECUTABLE_FILE ]

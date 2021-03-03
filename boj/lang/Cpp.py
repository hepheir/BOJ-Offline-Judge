import os

from boj import util
from boj import config

EXTENSION = '.cpp'

__CONFIG_COMPILER_PATH = config.from_json('cpp.compiler.path')
__SOURCE_FILE = os.path.join(util.TMP_DIRECTORY, EXTENSION)
__EXECUTABLE_FILE = os.path.join(util.TMP_DIRECTORY, '.exe')

COMPILE = [ __CONFIG_COMPILER_PATH, "-g", __SOURCE_FILE, "-o", __EXECUTABLE_FILE ]
RUN = [ __EXECUTABLE_FILE ]

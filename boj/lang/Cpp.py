import os

from boj.util import TMP_DIRECTORY
from boj.config import from_json

EXTENSION = '.cpp'

__CONFIG_COMPILER_PATH = from_json('cpp.compiler.path')
__SOURCE_FILE = os.path.join(TMP_DIRECTORY, EXTENSION)
__EXECUTABLE_FILE = os.path.join(TMP_DIRECTORY, '.exe')

COMPILE = [ __CONFIG_COMPILER_PATH, "-g", __SOURCE_FILE, "-o", __EXECUTABLE_FILE ]
RUN = [ __EXECUTABLE_FILE ]

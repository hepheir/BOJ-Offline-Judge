from boj.util.path import temp_filename
from boj.config import config

__COMPILER = config.get('Languages', 'c', 'compilerPath')
__EXECUTABLE_FILE = temp_filename('.exe')

EXTENSION = '.cpp'
COMPILE = [ __COMPILER, "-g", "{src}", "-o", __EXECUTABLE_FILE ]
RUN = [ __EXECUTABLE_FILE ]

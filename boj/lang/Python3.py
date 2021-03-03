import os

from boj import util

EXTENSION = '.py'

__SOURCE_FILE = os.path.join(util.TMP_DIRECTORY, EXTENSION).replace('\\', '/')

COMPILE = [ "python3", "-c", f"import py_compile; py_compile.compile('{__SOURCE_FILE}')" ]
RUN = [ "python3", __SOURCE_FILE ]

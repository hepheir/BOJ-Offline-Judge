import os

from .. import config

EXTENSION = '.py'

__CONFIG_TMP_DIRECTORY = config.from_json('tmp.directory')

__SOURCE_FILE = os.path.join(__CONFIG_TMP_DIRECTORY, EXTENSION)

COMPILE = [ "python3", "-c", f"import py_compile; py_compile.compile('{__SOURCE_FILE}')" ]
RUN = [ "python3", __SOURCE_FILE ]

from boj.lang.Cpp import EXTENSION


EXTENSION = '.py'
COMPILE = [ "python3", "-c", "import py_compile; py_compile.compile('{src}')" ]
RUN = [ "python3", "{src}" ]

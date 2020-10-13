from ..util.unit import MB, SECOND
from ..lang import Language

class Python3(Language):
    CODE = 'Main.py'
    COMPILE = f'''python3 -c "import py_compile; py_compile.compile(r'{CODE}')"'''
    EXECUTE = f'''python3 {CODE}'''
    timelimit = lambda seconds: (3*seconds + 2*SECOND)
    memlimit = lambda bytes: (2*bytes + 32*MB)
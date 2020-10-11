from ..util.datatypes import *

STDOUT = 'tmp/stdout'

def load_stdout():
    open(STDOUT, 'w').close()
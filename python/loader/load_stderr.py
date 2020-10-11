from ..util.datatypes import *

STDERR = 'tmp/stderr'

def load_stderr():
    open(STDERR, 'w').close()
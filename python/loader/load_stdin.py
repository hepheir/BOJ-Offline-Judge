from ..util.datatypes import *

STDIN = 'tmp/stdin'

def load_stdin(file:Path):
    with open(file, 'r') as f:
        content = f.read()
    with open(STDIN, 'w') as f:
        f.write(content)
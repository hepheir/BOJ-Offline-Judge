from ..util.datatypes import *

SCRIPT = 'tmp/main'

def load_script(file:path):
    with open(file, 'r') as f:
        content = f.read()
    with open(SCRIPT, 'w') as f:
        f.write(content)

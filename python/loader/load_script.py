from ..util.datatypes import *

SCRIPT = 'tmp/main'

def load_script(file:Path):
    with open(file, 'r') as f:
        content = f.read()
    with open(SCRIPT, 'w') as f:
        f.write(content)

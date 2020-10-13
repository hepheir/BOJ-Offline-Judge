# 확장자를 통해 언어를 유추
import os

from ..lang import *

EXTENSIONS = {
    '.py': Python3
}

class LanguageNotGuessable(Exception):
    pass

def guess_from_ext(file:os.PathLike) -> Language:
    _, ext = os.path.splitext(file)
    ext = ext.lower()
    if ext not in EXTENSIONS:
        raise LanguageNotGuessable()
    return EXTENSIONS[ext]
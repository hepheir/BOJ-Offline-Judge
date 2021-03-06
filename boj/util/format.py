import os
import pathlib

def format_src(string:str, src:pathlib.Path) -> str:
    return string.format(
        src=src,
        srcDirname=os.path.dirname(src)
    )

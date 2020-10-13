import os
from types import LambdaType

class ShellCommand(str):
    pass

class Language:
    CODE = os.PathLike
    COMPILE = ShellCommand
    EXECUTE = ShellCommand
    timelimit = LambdaType
    memlimit = LambdaType
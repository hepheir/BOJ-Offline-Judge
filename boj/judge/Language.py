import pathlib
import os
import shutil
import subprocess
import typing


from boj.config import config

class BaseLanguage:
    def __init__(
        self,
        languageName:str,
        languageId:int,
        submitFile:pathlib.Path,
        compileArgs:typing.List[str],
        runArgs:typing.List[str],
        version:str = None,
        timelimit:typing.Callable[[float], float] = lambda ms: ms,
        memorylimit:typing.Callable[[float], float] = lambda KB: KB,
    ):
        self.languageName = languageName
        self.languageId = languageId
        self.submitFile = submitFile
        self.compileArgs = compileArgs
        self.runArgs = runArgs
        self.version = version
        self.timelimit = timelimit
        self.memorylimit = memorylimit


    def compile(self, source_file:pathlib.Path):
        tempDirname = config.get('path', 'tempDirname', fallback='%TEMP%')
        submitFile = os.path.join(tempDirname, self.submitFile)
        shutil.copyfile(source_file, submitFile)
        subprocess.run(
            args=self.compileArgs,
            cwd=tempDirname,
            check=True
        )
    

    def run(self, input_file:pathlib.Path, output_file:pathlib.Path):
        tempDirname = config.get('path', 'tempDirname', fallback='%TEMP%')
        subprocess.run(
            args=self.runArgs,
            cwd=tempDirname,
            stdin=open(input_file, 'r'),
            stdout=open(output_file, 'w'),
            timeout=self.timelimit(config.get('judge', 'defaultTimeLimit', fallback=4000) / 1000),
            check=True
        )


Python3 = BaseLanguage(
    languageName='Python 3',
    languageId=28,
    submitFile='Main.py',
    compileArgs=[config.get('language', 'python.pythonPath', fallback='python'), "-c", "\"import py_compile; py_compile.compile(r'Main.py')\""],
    runArgs=[config.get('language', 'python.pythonPath', fallback='python'), "Main.py"],
    timelimit=lambda ms: (ms*3+2000),
    memorylimit=lambda KB: (KB*2+32000)
)


Cpp = BaseLanguage(
    languageName='C++ 14',
    languageId=88,
    submitFile='Main.cc',
    compileArgs=[config.get('language', 'cpp.compilerPath', fallback='g++'), "Main.cc", "-o", "Main", "-std=gnu++14"],
    runArgs=["./Main"]
)

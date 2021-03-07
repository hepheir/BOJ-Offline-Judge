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
        self.name = languageName
        self.id = languageId
        self.submitFile = submitFile
        self.compileArgs = compileArgs
        self.runArgs = runArgs
        self.version = version
        self.timelimit = timelimit
        self.memorylimit = memorylimit


    def compile(self, source_file:pathlib.Path):
        tempDirname = config.get('user', 'path.temp.dirname')
        submitFile = os.path.join(tempDirname, self.submitFile)
        shutil.copyfile(source_file, submitFile)
        subprocess.run(
            args=self.compileArgs,
            cwd=tempDirname,
            check=True
        )
    

    def run(self, input_file:pathlib.Path, output_file:pathlib.Path):
        tempDirname = config.get('user', 'path.temp.dirname')
        timeLimit_ms = config.getfloat('user', 'judge.run.timelimit')
        subprocess.run(
            args=self.runArgs,
            cwd=tempDirname,
            stdin=open(input_file, 'r'),
            stdout=open(output_file, 'w'),
            timeout=self.timelimit(timeLimit_ms) / 1000,
            check=True
        )


class LanguageNotSupported(BaseException):
    pass


class Language:
    def __init__(self, source_file:pathlib.Path):
        self.language = self.detect_language(source_file=source_file)
        self.compile = self.language.compile
        self.run = self.language.run
        self.name = self.language.name
        self.id = self.language.id
        self.version = self.language.version


    def detect_language(self, source_file:pathlib.Path) -> BaseLanguage:
        filenameNoExt, ext = os.path.splitext(source_file)
        if not ext:
            ext = os.path.basename(filenameNoExt)
        if ext == '.py':
            return Python3
        if ext == '.cpp' or ext == '.cc':
            return Cpp
        else:
            raise LanguageNotSupported('지원되지 않는 언어입니다.')


Python3 = BaseLanguage(
    languageName='Python 3',
    languageId=28,
    submitFile='Main.py',
    compileArgs=[
        config.get('user', 'language.python3.python.path'),
        "-c",
        "\"import py_compile; py_compile.compile(r'Main.py')\""
    ],
    runArgs=[
        config.get('user', 'language.python3.python.path'),
        "Main.py"
    ],
    timelimit=lambda ms: (ms*3+2000),
    memorylimit=lambda KB: (KB*2+32000)
)


Cpp = BaseLanguage(
    languageName='C++ 14',
    languageId=88,
    submitFile='Main.cc',
    compileArgs=[
        config.get('user', 'language.cpp.compiler.path'),
        "Main.cc",
        "-o",
        "Main",
        "-std=gnu++14"
    ],
    runArgs=[
        "./Main"
    ]
)

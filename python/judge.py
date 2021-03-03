import glob
import os
import shutil
import subprocess
import time

from . import lang
from . import config
from . import util


__CONFIG_TMP_DIRECTORY: str = config.from_json('tmp.directory')
__CONFIG_TIMEOUT: float = config.from_json("timelimit.ms") / 1000
__CONFIG_RESULT_INCLUDES_TIME: bool = config.from_json("result.include.time")
__CONFIG_RESULT_INCLUDES_DATAPATH: bool = config.from_json("result.include.datapath")

__CONFIG_DATA_IN_PATH_PATTERN: str = config.from_json("data.in.path.pattern")
__CONFIG_DATA_OUT_PATH_PATTERN: str = config.from_json("data.out.path.pattern")


class TimeRecorder:
    STACK = [time.time()]

    @classmethod
    def check(cls):
        cls.STACK.append(time.time())

    @classmethod
    def pop(cls) -> util.units.ms:
        if len(cls.STACK) == 1:
            return -1
        else:
            return round((cls.STACK.pop() - cls.STACK[-1]) * 1000)


class TestCase:
    def __init__(self):
        self.input_file: os.PathLike
        self.output_file: os.PathLike
        self.language: lang.BaseLanguage

def load_testcases(src: os.PathLike):
    VARIABLES = {
        'src': src,
        'srcDirname': os.path.dirname(src),
    }
    language = lang.detect_language(src)
    input_files = glob.glob(__CONFIG_DATA_IN_PATH_PATTERN.format(**VARIABLES), recursive=True)
    output_files = glob.glob(__CONFIG_DATA_OUT_PATH_PATTERN.format(**VARIABLES), recursive=True)
    for input_file, output_file in zip(input_files, output_files):
        testcase = TestCase()
        testcase.input_file = input_file
        testcase.output_file = output_file
        testcase.language = language
        yield testcase


def compile(src: os.PathLike):
    language = lang.detect_language(src)
    backup_src = os.path.join(__CONFIG_TMP_DIRECTORY, language.EXTENSION)
    shutil.copyfile(src, backup_src)
    subprocess.run(language.COMPILE, check=True)

def judge_testcase(testcase: TestCase):
    verdict = ''
    user_output_file = os.path.join(__CONFIG_TMP_DIRECTORY, '.stdout')
    try:
        TimeRecorder.check()
        subprocess.run(
            testcase.language.RUN,
            stdin=open(testcase.input_file, 'r'),
            stdout=open(user_output_file, 'w'),
            timeout=__CONFIG_TIMEOUT,
            check=True)
        TimeRecorder.check()
    except subprocess.CalledProcessError:
        verdict = '런타임 에러'
    except subprocess.TimeoutExpired:
        verdict = '시간 초과'
    except MemoryError:
        verdict = '메모리 초과'
    else:
        with open(testcase.output_file, 'r') as f_ans, open(user_output_file, 'r') as f_usr:
            ans = f_ans.read().rstrip()
            usr = f_usr.read().rstrip()
        if ans == usr:
            verdict = '맞았습니다!!'
        elif not usr:
            verdict = '출력 없음'
        else:
            verdict = '틀렸습니다'
    finally:
        result = f'{verdict:10s}'

        if __CONFIG_RESULT_INCLUDES_TIME:
            result += f'\t{TimeRecorder.pop():>7d} ms'

        if __CONFIG_RESULT_INCLUDES_DATAPATH:
            result += f'\t{util.shorten_path(testcase.input_file)}'
    return result

import subprocess

from boj.config import config
from boj.judge.Testcase import TestCase
from boj.util import TimeRecorder, temp_filename, shorten_path


def judge_testcase(testcase: TestCase):
    user_output_file = temp_filename('.stdout')
    verdict = ''
    try:
        TimeRecorder.check()
        subprocess.run(
            testcase.language.run(testcase.source_file),
            stdin=open(testcase.input_file, 'r'),
            stdout=open(user_output_file, 'w'),
            timeout=float(config['judge']['defaultTimeLimit']) / 1000,
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
        if config['judge']['briefTime']:
            result += f'\t{TimeRecorder.pop():>7d} ms'
        if config['judge']['briefDatapath']:
            result += f'\t{shorten_path(testcase.input_file)}'
    return result

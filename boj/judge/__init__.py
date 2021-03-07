import argparse
import pathlib
import subprocess

from boj.config import config
from boj.core import DatasetQueue, Language
from boj.util import shorten_path, TimeRecorder


def action(args:argparse.Namespace):
    sourcefile: pathlib.Path = args.src

    if True:
    #############################################################################
    # 채점 준비 : 소스코드 백업 및 데이터 셋 생성
    #############################################################################

        print('[INFO]', '채점 준비중...                                        ')

        language = Language(source_file=sourcefile)
        datasetQueue = DatasetQueue(source_file=sourcefile)

    #############################################################################
    # 컴파일
    #############################################################################

        print('[INFO]', '컴파일 중...                                          ')

    try:
        language.compile(source_file=sourcefile)

    except subprocess.CalledProcessError:
        print('[INFO]', '컴파일 에러                                           ')
        print('================================================================')

    except BaseException as error:
        print('[INFO]', '컴파일 에러                                           ')
        print('================================================================')
        raise error

    else:
        print('[INFO]', '채점 준비 완료                                        ')
        print('----------------------------------------------------------------')
        print('[INFO]', f'선택된 파일: "{shorten_path(sourcefile)}"            ')
        print('[INFO]',f'선택된 언어: {language.name}                          ')
        print('[INFO]',f'{len(datasetQueue.queue)}개의 데이터 셋 로드 됨            ')
        print('----------------------------------------------------------------')

    #############################################################################
    # 채점 시작
    #############################################################################


    for input_file, output_file in datasetQueue.queue:
        print('[INFO]', '채점 중...                                  ', end='\r')

        verdict = ''
        stdoutFilename = config.get('user', 'path.temp.stdout.filename')
        try:
            TimeRecorder.check()
            language.run(input_file=input_file, output_file=stdoutFilename)
            TimeRecorder.check()
        except subprocess.CalledProcessError:
            verdict = '런타임 에러'
        except subprocess.TimeoutExpired:
            verdict = '시간 초과'
        except MemoryError:
            verdict = '메모리 초과'
        else:
            with open(output_file, 'r') as f_ans, open(stdoutFilename, 'r') as f_usr:
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
            if config.getboolean('user', 'judge.brief.time'):
                result += f'\t{TimeRecorder.pop():>7d} ms'
            if config.getboolean('user', 'judge.brief.inputfile'):
                result += f'\t{shorten_path(input_file)}'

        print('[INFO]', result                                                  )

    #############################################################################
    # 채점 완료
    #############################################################################

    if True:
        print('================================================================')

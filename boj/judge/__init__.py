import argparse
import pathlib
import subprocess

from boj.judge.load_testcases import load_testcases
from boj.judge.judge_testcases import judge_testcase
from boj.util.path import shorten_path, temp_makecopy
from boj.lang import detect_language

def __main__(src: pathlib.Path):
    if True:
        print('================================================================')
        print('                 :: BOJ. Offline Judge ::                       ')
        print('                  * 짭준 오프라인 저지 *                        ')
        print('            당신의 채점 결과를 예측해 드립니다.                 ')
        print('================================================================')
        print('[INFO]', f'선택된 파일: "{shorten_path(src)}"')
        print('----------------------------------------------------------------')

    #############################################################################
    # 채점 준비 : 소스코드 백업 및 데이터 셋 생성
    #############################################################################

        print('[INFO]', '채점 준비중...                                        ')

        source = temp_makecopy(src)
        language = detect_language(src)
        testcase_generator = load_testcases(source)

    #############################################################################
    # 컴파일
    #############################################################################

        print('[INFO]', '컴파일 중...                                          ')

    try:
        subprocess.run(language.COMPILE, check=True)
    except BaseException as error:
        print('[INFO]', '컴파일 에러                                           ')
        print('================================================================')
        raise error
    else:
        print('[INFO]', '채점 준비 완료                                        ')
        print('----------------------------------------------------------------')

    #############################################################################
    # 채점 시작
    #############################################################################

    for testcase in testcase_generator:
        print('[INFO]', '채점 중...                                  ', end='\r')
        print('[INFO]', judge_testcase(testcase))

    #############################################################################
    # 채점 완료
    #############################################################################

    if True:
        print('================================================================')

action = argparse.Action()
action.__call__ = __main__

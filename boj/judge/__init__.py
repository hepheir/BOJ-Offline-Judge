import argparse
import pathlib
import subprocess

from boj.config import config
from boj.judge.load_testcases import load_testcases
from boj.judge.judge_testcases import judge_testcase
from boj.util import shorten_path, temp_makecopy, format_src
from boj.lang import detect_language

def action(args:argparse.Namespace):
    original_sourcefile: pathlib.Path = args.src

    if True:
        print('================================================================')
        print('                 :: BOJ. Offline Judge ::                       ')
        print('                  * 짭준 오프라인 저지 *                        ')
        print('            당신의 채점 결과를 예측해 드립니다.                 ')
        print('================================================================')
        print('[INFO]', f'선택된 파일: "{shorten_path(original_sourcefile)}"')
        print('----------------------------------------------------------------')

    #############################################################################
    # 채점 준비 : 소스코드 백업 및 데이터 셋 생성
    #############################################################################

        print('[INFO]', '채점 준비중...                                        ')

        temp_sourcefile = temp_makecopy(original_sourcefile)
        language = detect_language(original_sourcefile)
        input_filename_pattern = format_src(config['path']['inputFilenamePattern'], original_sourcefile)
        output_filename_pattern = format_src(config['path']['outputfilenamePattern'], original_sourcefile)
        testcase_generator = load_testcases(temp_sourcefile, language, input_filename_pattern, output_filename_pattern)

    #############################################################################
    # 컴파일
    #############################################################################

        print('[INFO]', '컴파일 중...                                          ')

    try:
        subprocess.run(language.compile(temp_sourcefile), check=True)
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

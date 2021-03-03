import argparse

from boj import judge
from boj import util

parser = argparse.ArgumentParser(
    'Baekjoon Offline Judge <짭준 오프라인 저지> :: 당신의 채점 결과를 예측해 드립니다.',
    usage='<source file>')

parser.add_argument('src', help='작성한 소스코드의 경로')

args = parser.parse_args()

if True:
    print('================================================================')
    print('                 :: BOJ. Offline Judge ::                       ')
    print('                  * 짭준 오프라인 저지 *                        ')
    print('            당신의 채점 결과를 예측해 드립니다.                 ')
    print('================================================================')
    print('[INFO]',f'선택된 파일: "{util.shorten_path(args.src)}"'          )
    print('----------------------------------------------------------------')    
    print('[INFO]', '채점 준비중...                                        ')
    testcases_iterator = judge.load_testcases(args.src)

    print('[INFO]', '컴파일 중...                                          ')
try:
    judge.compile(args.src)
except BaseException as error:
    print('[INFO]', '컴파일 에러                                           ')
    print('================================================================')
    raise error
else:
    print('[INFO]', '채점 준비 완료                                        ')
    print('----------------------------------------------------------------')

for testcase in testcases_iterator:
    print('[INFO]', '채점 중...                                  ', end='\r')
    print('[INFO]', judge.judge_testcase(testcase)                          )

if True:
    print('================================================================')

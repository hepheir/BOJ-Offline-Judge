import argparse

from . import judge

parser = argparse.ArgumentParser(
    'Baekjoon Offline Judge <짭준 오프라인 저지> :: 당신의 채점 결과를 예측해 드립니다.',
    usage='<source file>')

parser.add_argument('src', help='작성한 소스코드의 경로')

args = parser.parse_args()

if True:
    print('================================================================')
    print('[INFO]', '                                                      ')
    print('[INFO]', ':: Baekjoon Offline Judge ::                          ')
    print('[INFO]', '* 짭준 오프라인 저지.                                 ')
    print('[INFO]', '  당신의 채점 결과를 예측해 드립니다.                 ')
    print('[INFO]', '                                                      ')
    print('================================================================')
    print('[INFO]', '선택된 파일:                                          ')
    print('[INFO]',f' -> "{args.src}"'                                      )
    print('[INFO]', '                                                      ')
    
    print('[INFO]', '채점 준비중...                              ', end='\r')
    testcases_iterator = judge.load_testcases(args.src)

    print('[INFO]', '컴파일 중...                                ', end='\r')
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
    print('[INFO]', '                                                      ')

if True:
    print('================================================================')

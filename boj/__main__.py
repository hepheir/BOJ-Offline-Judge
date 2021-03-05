import argparse
import pathlib
import textwrap

from boj.judge import action

parser = argparse.ArgumentParser(
    prog=textwrap.dedent('''
        Baekjoon Offline Judge :: 당신의 채점 결과를 예측해 드립니다.
    '''),
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''
        Baekjoon Online Judge를 풀면서 데이터 셋을 돌려보는 것이 번거롭지 않았나요.
        전 제가 귀찮아서 이 프로그램을 제작하였습니다.

        제작자: Hepheir (hepheir@gmail.com)
        깃허브: https://github.com/Hepheir/BOJ-Offline-Judge
    '''),
    usage='<command>')
subparsers = parser.add_subparsers()

judge = subparsers.add_parser(name='judge', help='채점과 관련된 작업')
judge.add_argument('src', type=pathlib.Path, help='채점할 소스코드')
judge.set_defaults(func=action)

args = parser.parse_args()
args.func(args)

import argparse
import pathlib
import textwrap


parser = argparse.ArgumentParser(
    prog=textwrap.dedent('''
        Baekjoon Offline Judge :: 당신의 채점 결과를 예측해 드립니다.
        ================================================================
    '''),
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''
        Baekjoon Online Judge를 풀면서 데이터 셋을 돌려보는 것이 번거롭지 않았나요.
        전 제가 귀찮아서 이 프로그램을 제작하였습니다.

        제작자: Hepheir (hepheir@gmail.com)
        깃허브: https://github.com/Hepheir/BOJ-Offline-Judge
    '''),
    usage='[ python -m boj <command> ] or [ python -m boj.judge <source_file> ]')

parser.add_argument('command', help='수행할 작업', choices=['judge', 'setup'])

args, sub_args = parser.parse_known_args()


if args.command == 'judge':
    from boj.judge import action

    parser = argparse.ArgumentParser(usage='python -m boj judge <source_file>')
    parser.add_argument('src', type=pathlib.Path, help='채점할 소스코드')

    args = parser.parse_args(sub_args)
    action(args)

elif args.command == 'setup':
    from boj.core import Problem

    problem = Problem(int(input('문제 번호: ')))
    problem.make_sample_data_files()

import argparse
import pathlib

from boj.judge import action


parser = argparse.ArgumentParser(usage='python -m boj judge <source_file>')
parser.add_argument('src', type=pathlib.Path, help='채점할 소스코드')

args = parser.parse_args()
action(args.src)

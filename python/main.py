import argparse

from . import util
from . import core

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('stdin')
parser.add_argument('stdout')
parser.add_argument('--lang',
                    required=False)

args = parser.parse_args()

language = util.guess_from_ext(args.file)
task_runner = core.task_generator(args.file, language, allow_handicap=True)

# TODO: task_runner() ...
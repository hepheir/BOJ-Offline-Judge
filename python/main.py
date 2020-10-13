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


import glob
import pathlib
import typing

from boj.config import config
from boj.judge.Testcase import TestCase
from boj.lang import BaseLanguage
from boj.util.format import format_src


def load_testcases(source_file: pathlib.Path, language: BaseLanguage) -> typing.Generator[TestCase]:
    input_files = glob.glob(format_src(config.get('Paths', 'inputfilenamePatterns')), recursive=True)
    output_files = glob.glob(format_src(config.get('Paths', 'outputfilenamePatterns')), recursive=True)
    for input_file, output_file in zip(input_files, output_files):
        yield TestCase(source_file, input_file, output_file, language)

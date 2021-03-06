import glob
import pathlib
import typing

from boj.judge.Testcase import TestCase
from boj.lang import BaseLanguage


def load_testcases(source_file: pathlib.Path, language: BaseLanguage, input_filename_pattern:str, output_filename_pattern:str) -> typing.Generator[TestCase, None, None]:
    input_files = glob.glob(input_filename_pattern, recursive=True)
    output_files = glob.glob(output_filename_pattern, recursive=True)
    for input_file, output_file in zip(input_files, output_files):
        yield TestCase(source_file, input_file, output_file, language)

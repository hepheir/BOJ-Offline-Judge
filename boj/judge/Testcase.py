import pathlib

from boj.lang import BaseLanguage


class TestCase:
    def __init__(self, source_file: pathlib.Path, input_file: pathlib.Path, output_file: pathlib.Path, language: BaseLanguage):
        self.source_file = source_file
        self.input_file = input_file
        self.output_file = output_file
        self.language = language

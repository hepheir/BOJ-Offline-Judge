import pathlib
import glob

from boj.lang import BaseLanguage, detect_language
from boj.config import config
from boj.util.path import temp_makecopy
from boj.util.format import format_src


class TestCase:
    def __init__(self, source_file: pathlib.Path, input_file: pathlib.Path, output_file: pathlib.Path, language: BaseLanguage):
        self.source_file = source_file
        self.input_file = input_file
        self.output_file = output_file
        self.language = language


def load_testcases(src: pathlib.Path):
    language = detect_language(src)
    source_file = temp_makecopy(src)
    input_files = glob.glob(format_src(config.get('Paths', 'inputfilenamePatterns')), recursive=True)
    output_files = glob.glob(format_src(config.get('Paths', 'outputfilenamePatterns')), recursive=True)
    for input_file, output_file in zip(input_files, output_files):
        yield TestCase(source_file, input_file, output_file, language)

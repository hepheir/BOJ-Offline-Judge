import collections
import glob
import os
import pathlib

from boj.config import config


class Problem:
    def __init__(self, source_file:pathlib.Path):
        self.queue = collections.deque()
        self.load_data(source_file)


    def load_data(self, source_file:pathlib.Path):
        config_inputFileExt = config.get('user', 'data.extension.inputfile')
        config_outputFileExt = config.get('user', 'data.extension.outputfile')
        config_dataDirname = config.get('user', 'data.dirname', vars={
            'src': source_file,
            'srcDirname': os.path.dirname(source_file),
        })
        # 파일명 패턴 생성
        inputFilePattern = os.path.join(config_dataDirname, '**', '*'+config_inputFileExt)
        outputFilePattern = os.path.join(config_dataDirname, '**', '*'+config_outputFileExt)
        # 생성된 패턴을 이용하여 파일 목록 불러오기
        input_files = glob.glob(inputFilePattern, recursive=True)
        output_files = glob.glob(outputFilePattern, recursive=True)
        # 큐에 파일 목록을 삽입
        self.queue.extend(zip(input_files, output_files))

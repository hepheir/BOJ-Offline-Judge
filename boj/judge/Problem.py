import collections
import glob
import os
import pathlib
import typing

from boj.config import config


class Problem:
    def __init__(self):
        self.queue = collections.deque()
        self.load_data()


    def load_data(self, source:pathlib.Path):
        config_inputFileExt = config.get('path', 'inputFilieExt', fallback='.in')
        config_outputFileExt = config.get('path', 'outputFileExt', fallback='.out')
        config_dataDirname = config.get('path', 'outputFileExt', fallback='%(srcDirname)', vars={
            'src': source,
            'srcDirname': os.path.dirname(source),
        })
        input_files = glob.glob(os.path.join(config_dataDirname, '**', '*'+config_inputFileExt), recursive=True)
        output_files = glob.glob(os.path.join(config_dataDirname, '**', '*'+config_outputFileExt), recursive=True)
        self.queue.extend(zip(input_files, output_files))

        
    def get_dataset_from_queue(self) -> typing.Tuple[pathlib.Path, pathlib.Path]:
        return self.queue.popleft()

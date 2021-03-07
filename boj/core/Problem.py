import os
import typing

from boj.config import config
from boj.util.Html import Html


class Problem:
    def __init__(self, number:int):
        self.html:Html = Html(f'https://acmicpc.net/problem/{number}')
        self.number:int = number
        self.title = self.html.innerHTML('<span id="problem_title">')
        print('[INFO]',f'선택한 문제: {self.number}번 - {self.title}')
        print('----------------------------------------------------------------')


    def sample_data_generator(self) -> typing.Generator[typing.Tuple[str, str], None, None]:
        for i in range(1, 20):
            sample_in = self.html.innerHTML( f'<pre class="sampledata" id="sample-input-{i}">')
            sample_out = self.html.innerHTML( f'<pre class="sampledata" id="sample-output-{i}">')
            if not sample_in:
                break
            sample_in = sample_in.replace('\r\n', '\n')
            sample_out = sample_out.replace('\r\n', '\n')
            yield sample_in, sample_out


    def make_sample_data_files(self):
        dirname = config.get('user', 'path.data.boj.sample.dirname', vars={
            'problem.number': self.number,
            'problem.title': self.title,
        })
        inputfileExt = config.get('user', 'path.inputfile.ext')
        outputfileExt = config.get('user', 'path.outputfile.ext')
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        dataset_count = 0
        for input_data, output_data in self.sample_data_generator():
            dataset_count += 1
            print('[INFO]',f'데이터 셋 생성 중... ({dataset_count})')
            # Input data
            input_file_path = os.path.join(dirname, str(dataset_count)+inputfileExt)
            with open(input_file_path, 'w') as input_file:
                input_file.write(input_data)
            # Output data
            output_file_path = os.path.join(dirname, str(dataset_count)+outputfileExt)
            with open(output_file_path, 'w') as output_file:
                output_file.write(output_data)
        print('----------------------------------------------------------------')
        print('[INFO]',f'데이터 셋 생성 완료: "{dirname}"')
        print('[INFO]',f'총 {dataset_count}개의 데이터 셋 생성됨.')
        print('----------------------------------------------------------------')

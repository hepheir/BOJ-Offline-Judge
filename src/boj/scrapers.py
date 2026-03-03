import requests

from bs4 import BeautifulSoup
from typing import Dict, Set

from boj.models import ProblemDTO, TestCaseDTO, SectionDTO


def get_html(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


class ProblemHtmlParser:
    @classmethod
    def parse(cls, html: str) -> ProblemDTO:
        return ProblemDTO(
            id=cls.parse_id(html),
            title=cls.parse_title(html),
            sections=cls.parse_sections(html),
            testcases=cls.parse_testcases(html),
        )

    @classmethod
    def parse_id(cls, html: str) -> int:
        soup = BeautifulSoup(html, 'html.parser')
        return int(soup.select_one('title').get_text(strip=True).split('번')[0])

    @classmethod
    def parse_title(cls, html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        return soup.select_one('span#problem_title').get_text(strip=True)

    @classmethod
    def parse_sections(cls, html: str) -> list[SectionDTO]:
        soup = BeautifulSoup(html, 'html.parser')
        return [
            SectionDTO(
                name=section.select_one('.headline').get_text(strip=True),
                text=section.select_one('.problem-text').get_text(strip=True),
            )
            for section in soup.select('div#problem-body > div > section')
        ]

    @classmethod
    def parse_testcases(cls, html: str) -> list[TestCaseDTO]:
        testcase_names: Set[str] = set()
        testcase_inputs: Dict[str, str] = {}
        testcase_outputs: Dict[str, str] = {}
        soup = BeautifulSoup(html, 'html.parser')
        for section in soup.select('div#problem-body > div > div > div > section'):
            headline = (
                section
                .select_one('.headline')
                .get_text()
                .replace('복사', '')
                .strip()
            )
            content = section.select_one('.sampledata').get_text(strip=True)

            testcase_name = ' '.join(
                headline.replace('입력', '').replace('출력', '').split()
            )
            testcase_names.add(testcase_name)

            if '입력' in headline:
                testcase_inputs[testcase_name] = content.strip()
            elif '출력' in headline:
                testcase_outputs[testcase_name] = content.strip()
            else:
                raise ValueError('Unknown testcase headline: %s' % headline)

        retval = []
        for name in testcase_names:
            if name not in testcase_inputs:
                raise ValueError('Missing input for testcase: %s' % name)
            if name not in testcase_outputs:
                raise ValueError('Missing output for testcase: %s' % name)
            retval.append(TestCaseDTO(
                name=name,
                input=testcase_inputs[name],
                output=testcase_outputs[name],
            ))
        return retval

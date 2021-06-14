import unittest

from boj.python.core.problem import Problem
from boj.python.core.problem import Rule


SAMPLE_PROBLEM = '.tmp/1000/'


class Test_Problem(unittest.TestCase):
    def setUp(self) -> None:
        self.problem = Problem()
        return super().setUp()

    def testLoad_fromWeb(self):
        self.problem.number = 1000
        self.problem.load()
        self.assertEqual(self.problem.number, 1000)
        self.assertEqual(self.problem.title, 'A+B')
        self.assertTrue(isinstance(self.problem.document.desc, str))
        self.assertTrue(isinstance(self.problem.document.input, str))
        self.assertTrue(isinstance(self.problem.document.output, str))
        self.assertTrue(isinstance(self.problem.document.hint, str))
        self.assertTrue(isinstance(self.problem.rule.judge_method, int))
        self.assertTrue(isinstance(self.problem.rule.memory_limit, float))
        self.assertTrue(isinstance(self.problem.rule.time_limit, float))

    def testLoad_withoutNumber(self):
        # 문제 번호 없이는 웹으로 부터 문제를 불러오는게 불가능합니다.
        with self.assertRaises(Exception):
            self.problem.load()

    def testLoad_fromLocal(self):
        self.problem.load(SAMPLE_PROBLEM)
        self.assertEqual(self.problem.number, 1000)
        self.assertEqual(self.problem.title, 'A+B')
        self.assertEqual(self.problem.document.desc,
                         '<p>두 정수 A와 B를 입력받은 다음,&nbsp;A+B를 출력하는 프로그램을 작성하시오.</p>')
        self.assertEqual(self.problem.document.hint,
                         '<p><a href="https://www.acmicpc.net/help/language">여기</a>를 누르면 1000번 예제 소스를 볼 수 있습니다.</p>')
        self.assertEqual(self.problem.document.input,
                         '<p>첫째 줄에 A와 B가 주어진다. (0 &lt; A, B &lt; 10)</p>')
        self.assertEqual(self.problem.document.output,
                         '<p>첫째 줄에 A+B를 출력한다.</p>')
        self.assertEqual(self.problem.rule.judge_method, Rule.DEFAULT)
        self.assertEqual(self.problem.rule.time_limit, 2.0)
        self.assertEqual(self.problem.rule.memory_limit, 128.0)

import unittest
from boj.python.core.web import Crawler


class Test_Crawler(unittest.TestCase):
    maxDiff = None

    def testGet_TestFile(self):
        TEST_URL = 'https://github.com/Hepheir/BOJ-Offline-Judge/files/6643645/TESTING.txt'
        TEST_HTML = 'Test for boj.python.core.web.Crawler.get()'
        html = Crawler.get(TEST_URL)
        self.assertTrue(isinstance(html, str),
                        f'`Crawler.get()` should return `str` type, not {type(html)}')
        self.assertEqual(html, TEST_HTML)

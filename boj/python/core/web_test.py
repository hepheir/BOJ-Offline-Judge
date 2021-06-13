import unittest
from boj.python.core.web import Crawler


class test_get(unittest.TestCase):
    maxDiff = None

    def testGetMethod(self):
        url = 'https://github.com/Hepheir/BOJ-Offline-Judge/files/6643645/TESTING.txt'
        html = Crawler.get(url)
        self.assertTrue(isinstance(html, str))
        self.assertEqual(html, 'Test for boj.python.core.web.Crawler.get()')
        self.assertNotEqual(html, ' ')

import unittest

import boj.tags


class TestGetMethod(unittest.TestCase):
    def test_get_existing_tag(self):
        x = boj.tags.get(1)
        self.assertIsInstance(x, boj.tags.Tag)
        # type checks
        for property, cls in [('id', int), ('name_ko', str), ('name_en', str), ('count', int)]:
            with self.subTest(property=property):
                self.assertIsInstance(x.__dict__[property], cls)
        self.assertEqual(x.id, 1)
        self.assertNotEqual(x.name_ko, '')
        self.assertNotEqual(x.name_en, '')

    def test_get_non_existing_tag(self):
        with self.assertRaises(Exception):
            boj.tags.get(99999)


if __name__ == '__main__':
    unittest.main()

import unittest
from yana.base import BasePost


class MyTestCase(unittest.TestCase):
    def test(self):
        self.base = BasePost('about','.md')
        self.base.add('index')
        self.assertEqual(self.base.done,1)

        self.base.add('about_me')

        self.base.remove('index2')
        self.assertEqual(self.base.done,1)

        self.base.remove('index')
        self.assertEqual(self.base.done,1)


if __name__ == '__main__':
    unittest.main()

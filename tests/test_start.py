import unittest
from yana import start


class TestStart(unittest.TestCase):
    def test_create(self):
        self.test_create_obj = start.Start();
        self.test_create_obj.create("mySite","My Site","Dariush","http://github.com/edrock/mysite")

        self.assertEqual(self.test_create_obj.done,1)

if __name__ == '__main__':
    unittest.main()

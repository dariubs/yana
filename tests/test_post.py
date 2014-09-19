import unittest
from yana import post


class TestPost(unittest.TestCase):
    def test(self):
        self.test_add = post.Post()
        self.test_add.add("postName")
        self.assertEqual(self.test_add.done,1);

        self.test_delete = post.Post();
        self.test_delete.delete("postName");
        self.assertEqual(self.test_delete.done,1)

if __name__ == '__main__':
    unittest.main()

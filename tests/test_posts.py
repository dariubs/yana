import unittest
from yana import posts


class TestPost(unittest.TestCase):
    def test(self):
        self.test_add = posts.Post()
        self.test_add.add("postName")
        self.assertEqual(self.test_add.done,1);

        self.test_delete = posts.Post();
        self.test_delete.delete("postName");
        self.assertEqual(self.test_delete.done,1)

if __name__ == '__main__':
    unittest.main()

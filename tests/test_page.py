import unittest
from yana import page


class MyPage(unittest.TestCase):
    def test(self):
        self.test_add = page.Page()
        self.test_add.add("pageName")
        self.assertEqual(self.test_add.done,1);

        self.test_delete = page.Page();
        self.test_delete.delete("pageName");
        self.assertEqual(self.test_delete.done,1)

if __name__ == '__main__':
    unittest.main()

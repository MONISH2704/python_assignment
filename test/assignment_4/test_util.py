import unittest
from python_assignment.src.assignment_4.util import merge

class testmerge(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(merge("aabccdabc",3),"ab\cd\abc")
if __name__=="__main__":
    unittest.main()
import unittest
from python_assignment.src.assignment_7.util import find

class testfind(unittest.TestCase):
    def test_find(self):
        self.assertEqual(find(8,5,2005), "Friday")
        self.assertEqual(find(8,5,2015), "Wednesday")
if __name__=="__main__":
    unittest.main()
import unittest
from python_assignment.src.assignment_15.util import calculate

class testcalculate(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate(3,2,[1,5,3],[3,1],[5,7]),1)
if __name__=="__main__":
    unittest.main()
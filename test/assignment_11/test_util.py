import unittest
from python_assignment.src.assignment_11.util import calculate

class testcalculate(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(
            calculate([
                "4 2",
                "2 5",
                "3 7",
                "1 3",
                "4 0"
            ]),
            3
        )
if __name__=="__main__":
    unittest.main()
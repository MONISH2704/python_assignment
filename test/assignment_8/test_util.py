import unittest
from python_assignment.src.assignment_4.util import average

class TestAverage(unittest.TestCase):
    def test_average(self):
        data = [
            "90 A Monish 1",
            "80 B Rahul 2",
            "70 C Anil 3"
        ]
        self.assertEqual(
            average(3, ["MARKS", "CLASS", "NAME", "ID"], data),
            80.0
        )

if __name__ == "__main__":
    unittest.main()

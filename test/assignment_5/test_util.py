import unittest
from python_assignment.src.assignment_5.util import number

class TestNumber(unittest.TestCase):
    def test_number(self):
        result = number(2)
        expected = (
            "  0  0  0  0\n"
            "  1  1  1  1\n"
            "  2  2 10 10\n"
        )
        self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()

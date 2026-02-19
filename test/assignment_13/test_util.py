import unittest
from python_assignment.src.assignment_4.util import math

class TestMath(unittest.TestCase):
    def test_math(self):
        data = [
            [1, 2],
            [3, 4]
        ]
        result = math(data)
        expected = (
            "[1.5 3.5]\n"
            "[1. 1.]\n"
            "1.118033988749895"
        )
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

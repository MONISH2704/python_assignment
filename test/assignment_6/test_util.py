import unittest
from python_assignment.src.assignment_6.util import h

class TestH(unittest.TestCase):
    def test_h(self):
        result = h(2, "H")
        expected = (
            " H H \n"
            "HHHHHHHHHH\n"
            "HHHHHHHHHH\n"
            "HHHHHHHHHH\n"
            "HHHHHHHHHH\n"
            " H H \n"
        )
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

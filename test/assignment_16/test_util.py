import unittest
from python_assignment.src.assignment_4.util import word

class TestWord(unittest.TestCase):
    def test_word(self):
        data = ["apple", "banana", "apple", "orange", "banana"]
        self.assertEqual(
            word(5, data),
            "3\n2 2 1"
        )

if __name__ == "__main__":
    unittest.main()

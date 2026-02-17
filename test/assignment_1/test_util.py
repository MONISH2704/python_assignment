import unittest
from python_assignment.src.assignment_1.util import runner

class testrunnerup(unittest.TestCase):
    def test_runner(self):
        self.assertEqual(runner([1,2,3,4,5]),4)
if __name__=="__main__":
    unittest.main()

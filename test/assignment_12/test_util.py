import unittest
from python_assignment.src.assignment_12.util import det

class testdet(unittest.TestCase):
    def test_det(self):
        self.assertEqual(det([[1.1,1.1],[1.1,1.1]]),0.00)
if __name__=="__main__":
    unittest.main()
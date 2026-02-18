import unittest
from python_assignment.src.assignment_17.util import iter

class testiter(unittest.TestCase):
    def test_iter(self):
        self.assertEqual(iter(4,['a','a','c','d'],2),0.833)
if __name__=="__main__":
    unittest.main()
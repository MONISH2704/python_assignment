import unittest
from python_assignment.src.assignment_2.util import average

class testaverage(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average({"a":[20,20,20],"b":[30,30,30]},"b"),30.00)
if __name__=="__main__":
    unittest.main()
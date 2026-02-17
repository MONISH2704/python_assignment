import unittest
from python_assignment.src.assignment_10.util import math

class testmath(unittest.TestCase):
    def test_math(self):
        self.assertEqual(math([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]),  (
        [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0],
        [2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],
        [1.0,2.0,3.0,4.0,5.0,6.0,8.0,9.0,10.0]
    ))
if __name__=="__main__":    
    unittest.main()
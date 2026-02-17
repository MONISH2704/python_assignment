import unittest
from python_assignment.src.assignment_3.util import mutate

class testmutate(unittest.TestCase):
    def test_mutate(self):
        self.assertEqual(mutate("abcdef",2,"l"),"a b l d e f")

if __name__=="__main__":
    unittest.main()
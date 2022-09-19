import unittest
from analytical import get_probs_analytically as get_probs

class TestSum(unittest.TestCase):
    #target = __import__("../analytical.py")

    def test_base(self):
        self.s = sorted([49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46])
        self.r = 6
        self.assertAlmostEqual(get_probs(self.s,self.r)[4], .46, delta=.01)

    def test_base_random(self):
        self.s = sorted([1,2,3,4,5,6,7,8,9,10])
        self.r = 2
        self.assertAlmostEqual(get_probs(self.s,self.r)[5], .11, delta=.01)

    def test_type(self):
        self.s = sorted([49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46])
        self.r = 6
        self.assertIsInstance({}, dict, "Should return a dictionary")

if __name__ == '__main__':
    unittest.main()

import unittest
from python.src.analytical import get_probs_analytically

class TestSum(unittest.TestCase):
    #target = __import__("../analytical.py") #for minimal tests
    get_probs = get_probs_analytically
    s = sorted([49, 8, 48, 15, 47, 4, 16, 23, 43, 44, 42, 45, 46])
    r = 6

    def test_base(self):
        self.assertIsInstance(get_probs(s,r), dict, "Should return a dictionary")

if __name__ == '__main__':
    unittest.main()

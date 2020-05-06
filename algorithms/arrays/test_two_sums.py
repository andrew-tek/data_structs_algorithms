from two_sums import twoNumberSum
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(twoNumberSum([1, 2, 3], 3), [1, 2])

    def test_sum1(self):
        self.assertEqual(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10), [-1, 11])

    def test_blank_no_answer(self):
        self.assertEqual(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15),[])
    
    def test_long_array(self):
        self.assertEqual(twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164), [])

if __name__ == '__main__':
    unittest.main()
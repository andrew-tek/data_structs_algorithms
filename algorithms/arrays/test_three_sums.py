from three_sums import three_number_sum
import unittest

class TestThreeSum(unittest.TestCase):
    def test_one(self):
        self.assertEqual(three_number_sum([1, 2, 3], 6), [[1, 2, 3]])

    def test_two(self):
        self.assertEqual(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])

    def test_three(self):
        self.assertEqual(three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 0), [])
    
    def test_four(self):
        self.assertEqual(three_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32), [[8, 9, 15]])


if __name__ == '__main__':
    unittest.main()
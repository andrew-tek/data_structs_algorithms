from two_sums import two_number_sum
import unittest

class TestTwoSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(two_number_sum([1, 2, 3], 3), [1, 2])

    def test_sum1(self):
        self.assertEqual(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10), [-1, 11])

    def test_blank_no_answer(self):
        self.assertEqual(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 15),[])
    
    def test_long_array(self):
        self.assertEqual(two_number_sum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164), [])

if __name__ == '__main__':
    unittest.main()
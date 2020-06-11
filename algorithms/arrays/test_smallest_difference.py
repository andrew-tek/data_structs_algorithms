from smallest_difference import smallest_difference
import unittest

class SmallestDifference(unittest.TestCase):
    def test_one(self):
        self.assertEqual(smallest_difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26])
    
    def test_two(self):
        self.assertEqual(smallest_difference([5], [5]), [5, 5])

if __name__ == '__main__':
    unittest.main()
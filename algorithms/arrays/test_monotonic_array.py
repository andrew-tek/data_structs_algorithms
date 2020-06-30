from monotonic_array import is_monotonic
import unittest

class MonotnicTest(unittest.TestCase):
    def test_true_one(self):
        self.assertEqual(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]), True)

    def test_false_one(self):
        self.assertEqual(is_monotonic([1, 2, 3, 1, 4, 5]), False)

    def test_all_same(self):
        self.assertEqual(is_monotonic([1, 1, 1, 1, 1]), True)

if __name__ == '__main__':
    unittest.main()
from spiral_traverse import spiral_traverse
import unittest

class SpiralTraverse(unittest.TestCase):
    def test_one(self):
        self.assertEqual(spiral_traverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    def test_two(self):
        self.assertEqual(spiral_traverse([[1, 2, 3, 4], [12, 13, 14, 5]]), [1, 2, 3, 4, 5, 14, 13, 12])
if __name__ == '__main__':
    unittest.main()
from move_element_to_end import move_element_to_end
import unittest

class MoveElementToEnd(unittest.TestCase):
    def test_one(self):
        self.assertEqual(move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2), [4, 1, 3, 2, 2, 2, 2, 2])

    def test_two(self):
        self.assertEqual(move_element_to_end([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
        
    def test_three(self):
        self.assertEqual(move_element_to_end([1, 1, 1, 1, 1], 1), [1, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
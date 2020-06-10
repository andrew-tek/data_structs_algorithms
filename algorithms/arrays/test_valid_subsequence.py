from valid_subsequence import isValidSubsequence
import unittest

class TestValidSubsequence(unittest.TestCase):

    def test_subsequence(self):
        self.assertEqual(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]), True)
    
    def test_subsequence_false(self):
        self.assertEqual(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -2]), False)

if __name__ == '__main__':
    unittest.main()
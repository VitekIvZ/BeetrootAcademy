#task1lesson20.py


"""
Pick your solution to one of the exercises in this module. 
Design tests for this solution and write tests using unittest library. 
"""


import unittest
import sys


sys.path.append('./lesson13')

from task3lesson13 import choose_func, square_nums, remove_negatives


class TestChooseFunc(unittest.TestCase):
    def test_all_positive(self):
        nums = [1, 2, 3, 4, 5]
        result = choose_func(nums, square_nums, remove_negatives)
        self.assertEqual(result, [1, 4, 9, 16, 25])

    def test_contains_negatives(self):
        nums = [1, -2, 3, -4, 5]
        result = choose_func(nums, square_nums, remove_negatives)
        self.assertEqual(result, [1, 3, 5])

    def test_all_negatives(self):
        nums = [-1, -2, -3, -4, -5]
        result = choose_func(nums, square_nums, remove_negatives)
        self.assertEqual(result, [])

    def test_mixed_positives_and_negatives(self):
        nums = [-1, 2, -3, 4, -5]
        result = choose_func(nums, square_nums, remove_negatives)
        self.assertEqual(result, [2, 4])

    def test_empty_list(self):
        nums = []
        result = choose_func(nums, square_nums, remove_negatives)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
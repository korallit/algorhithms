# coding: utf-8

import unittest
from algorithms.sort.bubble_sort import andris
from algorithms.sort.bubble_sort import grzs


data1 = [5, 1, 3, 2, 4]


# class TestBubbleSortAndris(unittest.TestCase):
#     def test_first_step(self):
#         """
#         Test that it swaps the first two element first
#         """
#         result = andris.swap_first_two(data1)
#         self.assertEqual(result, [1, 5, 3, 2, 4])

#     def test_first_round(self):
#         """
#         Test that it can find the greatest item
#         """
#         result = andris.greatest_to_end(data1)
#         self.assertEqual(result, [1, 3, 2, 4, 5])

#     def test_sort(self):
#         """
#         Test that it can sort a list of integers
#         """
#         result = andris.sort(data1)
#         self.assertEqual(result, [1, 2, 3, 4, 5])


# class TestBubbleSortGrzs(unittest.TestCase):
#     def test_first_step(self):
#         """
#         Test that it swaps the first two element first
#         """
#         result = grzs.swap_first_two(data1)
#         self.assertEqual(result, [1, 5, 3, 2, 4])

#     def test_first_round(self):
#         """
#         Test that it can find the greatest item
#         """
#         result = grzs.greatest_to_end(data1)
#         self.assertEqual(result, [1, 3, 2, 4, 5])

#     def test_sort(self):
#         """
#         Test that it can sort a list of integers
#         """
#         result = grzs.sort(data1)
#         self.assertEqual(result, [1, 2, 3, 4, 5])

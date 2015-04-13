from unittest import TestCase
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

__author__ = 'AWood'


class TestSorting(TestCase):
    def test_bs_null(self):
        test_input = None
        test_output = bubble_sort(test_input)
        TestCase.assertIsNone(self, test_output)

    def test_ms_null(self):
        test_input = None
        test_output = merge_sort(test_input)
        TestCase.assertIsNone(self, test_output)

    def test_qs_null(self):
        test_input = None
        test_output = quick_sort(test_input)
        TestCase.assertIsNone(self, test_output)

    def test__bs_empty_array(self):
        test_input = list()
        test_output = bubble_sort(test_input)
        TestCase.assertEquals(self, list(), test_output)

    def test__ms_empty_array(self):
        test_input = list()
        test_output = merge_sort(test_input)
        TestCase.assertEquals(self, list(), test_output)

    def test__qs_empty_array(self):
        test_input = list()
        test_output = quick_sort(test_input)
        TestCase.assertEquals(self, list(), test_output)

    def test_bs_sorting_sorted_array(self):
        test_input = [0, 1, 2, 3, 4, 5]
        test_output = bubble_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_ms_sorting_sorted_array(self):
        test_input = [0, 1, 2, 3, 4, 5]
        test_output = merge_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_qs_sorting_sorted_array(self):
        test_input = [0, 1, 2, 3, 4, 5]
        test_output = quick_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_bs_sorting_unsorted_array(self):
        test_input = [5, 3, 1, 4, 2, 0]
        test_output = bubble_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_ms_sorting_unsorted_array(self):
        test_input = [5, 3, 1, 4, 2, 0]
        test_output = merge_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_qs_sorting_unsorted_array(self):
        test_input = [5, 3, 1, 4, 2, 0]
        test_output = quick_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_bs_sorting_uniform_array(self):
        test_input = [1, 1, 1, 1, 1]
        test_output = bubble_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_ms_sorting_uniform_array(self):
        test_input = [1, 1, 1, 1, 1]
        test_output = merge_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_qs_sorting_uniform_array(self):
        test_input = [1, 1, 1, 1, 1]
        test_output = quick_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)
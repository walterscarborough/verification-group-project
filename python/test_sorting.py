from unittest import TestCase
from bubble_sort import bubble_sort
from merge_sort import merge_sort

__author__ = 'AWood'


class TestSorting(TestCase):
    def test_bsNull(self):
        test_input = None
        test_output = bubble_sort(test_input)
        TestCase.assertIsNone(self, test_output)

    def test_msNull(self):
        test_input = None
        test_output = merge_sort(test_input)
        TestCase.assertIsNone(self, test_output)

    def test__bsEmptyArray(self):
        test_input = list()
        test_output = bubble_sort(test_input)
        TestCase.assertIsNone(self, test_output)

    def test__msEmptyArray(self):
        test_input = list()
        test_output = merge_sort(test_input)
        TestCase.assertIsNone(self, test_output)

    def test_bsSortingWithSortedArray(self):
        test_input = [0, 1, 2, 3, 4, 5]
        test_output = bubble_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_msSortingWithSortedArray(self):
        test_input = [0, 1, 2, 3, 4, 5]
        test_output = merge_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_bsSortingWithUnsortedArray(self):
        test_input = [5, 3, 1, 4, 2, 0]
        test_output = bubble_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_msSortingWithUnsortedArray(self):
        test_input = [5, 3, 1, 4, 2, 0]
        test_output = merge_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_bsSortingWithUniformArray(self):
        test_input = [1, 1, 1, 1, 1]
        test_output = bubble_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)

    def test_msSortingWithUniformArray(self):
        test_input = [1, 1, 1, 1, 1]
        test_output = merge_sort(test_input)
        TestCase.assertEquals(self, sorted(test_input), test_output)
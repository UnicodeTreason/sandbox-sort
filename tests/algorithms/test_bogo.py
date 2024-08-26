import unittest

from sandboxsort.algorithms.sort_bogo import sort


class TestSum(unittest.TestCase):

    def test_sort_bogo(self):
        """
        Compare test input to provided true answer
        """
        testData = [5, 2, 1]
        result = sort(testData)
        self.assertEqual(result, [1, 2, 5])

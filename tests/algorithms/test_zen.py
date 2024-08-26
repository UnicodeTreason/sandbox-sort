import unittest

from sandboxsort.algorithms.sort_zen import sort


class TestSum(unittest.TestCase):

    def test_sort_zen(self):
        """
        Compare test input to provided true answer
        """
        testData = [5, 2, 1]
        result = sort(testData)
        self.assertEqual(result, [5, 2, 1])

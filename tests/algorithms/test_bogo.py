import unittest

from sandboxsort.algorithms.sort_bogo import calculate


class TestSum(unittest.TestCase):

    def test_sort_bogo(self):
        """
        Compare test input to provided true answer
        """
        testData = [5, 2, 1]
        result = calculate(testData)
        self.assertEqual(result, [1, 2, 5])

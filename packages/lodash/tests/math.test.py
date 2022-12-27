"""
Math Test
"""

import unittest
import libs as _


class TestMathMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(_.add(6, 4), 10)

    def test_ceil(self):
        self.assertEqual(_.ceil(4.006), 5)

    def test_divide(self):
        self.assertEqual(_.divide(6, 4), 1.5)

    def test_floor(self):
        self.assertEqual(_.floor(4.006), 4)

    def test_max(self):
        self.assertEqual(_.max([4, 2, 8, 6]), 8)

    def test_maxBy(self):
        self.assertEqual(_.max_by([{'n': 1}, {'n': 2}], 'n'), 2)

    def test_mean(self):
        self.assertEqual(_.mean([4, 2, 8, 6]), 5)

    def test_meanBy(self):
        self.assertEqual(
            _.mean_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], 'n'), 5)

    def test_min(self):
        self.assertEqual(_.min([4, 2, 8, 6]), 2)

    def test_minBy(self):
        self.assertEqual(
            _.min_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], 'n'), 2)

    def test_multiply(self):
        self.assertEqual(_.multiply(6, 4), 24)

    def test_roundNumber(self):
        self.assertEqual(_.round_number(4.006, 2), 4.01)

    def test_subtract(self):
        self.assertEqual(_.subtract(6, 4), 2)

    def test_sum(self):
        self.assertEqual(_.sum([4, 2, 8, 6]), 20)

    def test_sumBy(self):
        self.assertEqual(
            _.sum_by([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], 'n'), 20)


if __name__ == '__main__':
    unittest.main()

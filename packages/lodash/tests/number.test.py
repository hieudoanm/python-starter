"""
object
"""

import unittest
import libs as _


class TestNumberMethods(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(_.clamp(-10, -5, 5), -5)
        self.assertEqual(_.clamp(10, -5, 5), 5)

    def test_in_range(self):
        self.assertTrue(_.in_range(3, 2, 4))
        self.assertTrue(_.in_range(4, 8))
        self.assertFalse(_.in_range(4, 2))
        self.assertFalse(_.in_range(2, 2))
        self.assertTrue(_.in_range(1.2, 2))
        self.assertFalse(_.in_range(5.4, 4))
        self.assertFalse(_.in_range(-3, -2, -6))

    def test_random(self):
        random1 = _.random(5)
        self.assertTrue(0 <= random1 and random1 <= 5)
        random2 = _.random(5, 10)
        self.assertTrue(5 <= random2 and random2 <= 10)


if __name__ == '__main__':
    unittest.main()

"""
Date Test
"""

import unittest
import libs as _


class TestDateMethods(unittest.TestCase):
    """
    Test Date
    """

    def test_now(self):
        """
        Test Now
        """
        now = _.now()
        print(now)
        self.assertIsInstance(_.now(), int)

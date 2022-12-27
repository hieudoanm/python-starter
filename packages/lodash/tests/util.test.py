"""
Util Test
"""

import unittest
import libs as _


class TestUtilMethods(unittest.TestCase):
    def test_constant(self):
        """
        test_constant
        """
        self.assertEqual(_.times(2, _.constant({'a': 1})), [
                         {'a': 1}, {'a': 1}])

    def test_default_to(self):
        """
        test_default_to
        """
        self.assertEqual(_.default_to(1, 10), 1)
        self.assertEqual(_.default_to(None, 10), 10)

    def test_identity(self):
        """
        test_identity
        """
        obj = {'a': 1}
        self.assertEqual(_.identity(obj), obj)
        self.assertEqual(_.identity(123), 123)
        self.assertEqual(_.identity(obj, 123), obj)

    def test_noop(self):
        """
        test_noop
        """
        self.assertEqual(_.noop(), None)

    def test_range_array(self):
        """
        test_range_array
        """
        self.assertEqual(_.range_array(4), [0, 1, 2, 3])
        self.assertEqual(_.range_array(1, 5), [1, 2, 3, 4])
        self.assertEqual(_.range_array(0, 20, 5), [0, 5, 10, 15])

    def test_range_right(self):
        """
        test_range_right
        """
        self.assertEqual(_.range_right(4), [3, 2, 1, 0])
        self.assertEqual(_.range_right(1, 5), [4, 3, 2, 1])
        self.assertEqual(_.range_right(0, 20, 5), [15, 10, 5, 0])

    def test_stub_array(self):
        """
        test_stub_array
        """
        self.assertEqual(_.stub_array(), [])

    def test_stub_false(self):
        """
        test_stub_false
        """
        self.assertFalse(_.stub_false())

    def test_stub_object(self):
        """
        test_stub_object
        """
        self.assertEqual(_.stub_object(), {})

    def test_stub_string(self):
        """
        test_stub_string
        """
        self.assertEqual(_.stub_string(), '')

    def test_stub_true(self):
        """
        test_stub_true
        """
        self.assertTrue(_.stub_true())

    def test_times(self):
        """
        test_times
        """
        self.assertEqual(_.times(3), [0, 1, 2])
        self.assertEqual(_.times(4, _.constant(0)), [0, 0, 0, 0])

    def test_to_path(self):
        """
        test_to_path
        """
        self.assertEqual(_.to_path('a.b.c'), ['a', 'b', 'c'])
        self.assertEqual(_.to_path('a[0]b.c'), ['a', '0', 'b', 'c'])

    def test_unique_id(self):
        """
        test_unique_id
        """
        unique_id = _.unique_id()
        print(unique_id)


if __name__ == '__main__':
    unittest.main()

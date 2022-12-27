"""
lang
"""

import unittest
import libs as _


class TestLangMethods(unittest.TestCase):
    def test_cast_array(self):
        self.assertEqual(_.cast_array(1), [1])
        self.assertEqual(_.cast_array({'a': 1}), [{'a': 1}])
        self.assertEqual(_.cast_array('abc'), ['abc'])
        self.assertEqual(_.cast_array(None), [None])

    def test_conforms_to(self):
        object = {'a': 1, 'b': 2}
        self.assertTrue(_.conforms_to(object, {'b': lambda n: n > 1}))

    def test_clone(self):
        objects = [{'a': 1}, {'b': 2}]
        shallow = _.clone(objects)
        self.assertEqual(objects[0], shallow[0])

    def test_clone_deep(self):
        objects = [{'a': 1}, {'b': 2}]
        deep = _.clone_deep(objects)
        self.assertEqual(objects[0], deep[0])

    def test_clone_deep_with(self):
        objects = [{'a': 1}, {'b': 2}]
        deepValue = _.clone_deep_with(objects, lambda o: o[0])
        self.assertEqual(deepValue, {'a': 1})

    def test_clone_with(self):
        objects = [{'a': 1}, {'b': 2}]
        deepValue = _.clone_with(objects, lambda o: o[0])
        self.assertEqual(deepValue, {'a': 1})

    def test_eq(self):
        self.assertTrue(_.eq({'a': 1}, {'a': 1}))
        self.assertTrue(_.eq('a', 'a'))
        self.assertFalse(_.eq({'a': 1}, 'a'))
        self.assertFalse(_.eq('a', 1))

    def test_gt(self):
        self.assertTrue(_.gt(3, 1))
        self.assertFalse(_.gt(3, 3))
        self.assertFalse(_.gt(1, 3))

    def test_gte(self):
        self.assertTrue(_.gte(3, 1))
        self.assertTrue(_.gte(3, 3))
        self.assertFalse(_.gte(1, 3))

    def test_is_array(self):
        self.assertTrue(_.is_array([1, 2, 3]))
        self.assertFalse(_.is_array(123))

    def test_is_array_like(self):
        self.assertTrue(_.is_array_like([1, 2, 3]))
        self.assertTrue(_.is_array_like('abc'))
        self.assertFalse(_.is_array_like(_.noop))

    def test_is_array_like_object(self):
        self.assertTrue(_.is_array_like_object([1, 2, 3]))
        self.assertFalse(_.is_array_like_object('abc'))
        self.assertFalse(_.is_array_like_object(_.noop))

    def test_is_boolean(self):
        self.assertTrue(_.is_boolean(True))
        self.assertTrue(_.is_boolean(False))
        self.assertFalse(_.is_boolean(None))

    def test_is_empty(self):
        self.assertTrue(_.is_empty(None))
        self.assertTrue(_.is_empty(True))
        self.assertTrue(_.is_empty(1))
        self.assertFalse(_.is_empty([1, 2, 3]))
        self.assertTrue(_.is_empty([]))
        self.assertFalse(_.is_empty({'a': 1}))
        self.assertTrue(_.is_empty({}))

    def test_is_equal(self):
        self.assertTrue(_.is_equal({'a': 1}, {'a': 1}))

    def test_is_equal_with(self):
        object = {'a': 1}
        other = {'a': 3}
        self.assertTrue(_.is_equal_with(
            object, other, lambda o: o['a'] % 2 == 1))

    def test_is_finite(self):
        self.assertTrue(_.is_finite(3))
        self.assertFalse(_.is_finite('3'))
        self.assertFalse(_.is_finite(float('-inf')))

    def test_isFunction(self):
        def a():
            return
        self.assertTrue(_.isFunction(a))
        self.assertTrue(_.isFunction(lambda a: a))

    def test_is_integer(self):
        self.assertTrue(_.is_integer(3))
        self.assertFalse(_.is_integer('3'))

    def test_is_length(self):
        self.assertTrue(_.is_length(3))
        self.assertFalse(_.is_length('3'))

    def test_is_match(self):
        obj = {'a': 1, 'b': 2}
        self.assertTrue(_.is_match(obj, {'b': 2}))
        self.assertFalse(_.is_match(obj, {'b': 1}))

    def test_is_match_with(self):
        obj = {'a': 1, 'b': 2}
        self.assertTrue(_.is_match_with(
            obj, {'b': 4}, lambda value: value % 2 == 0))
        self.assertFalse(_.is_match_with(
            obj, {'b': 1}, lambda value: value % 2 == 0))

    def test_is_nil(self):
        self.assertTrue(_.is_nil(None))

    def test_is_null(self):
        self.assertTrue(_.is_null(None))

    def test_is_number(self):
        self.assertTrue(_.is_number(3))
        self.assertFalse(_.is_number('3'))
        self.assertTrue(_.is_number(float('-inf')))

    def test_is_object(self):
        self.assertTrue(_.is_object({}))
        self.assertFalse(_.is_object(None))

    def test_is_objectLike(self):
        self.assertTrue(_.is_object_like({}))
        self.assertTrue(_.is_object_like([]))
        self.assertFalse(_.is_object_like(None))

    def test_is_safe_integer(self):
        self.assertTrue(_.is_safe_integer(3))
        self.assertFalse(_.is_safe_integer('3'))
        self.assertFalse(_.is_safe_integer(float('inf')))

    def test_is_set(self):
        self.assertTrue(_.is_set(set([1, 2, 3])))

    def test_is_string(self):
        self.assertTrue(_.is_string('abc'))
        self.assertFalse(_.is_string(123))

    def test_is_undefined(self):
        self.assertTrue(_.is_undefined(None))

    def test_lt(self):
        self.assertTrue(_.lt(1, 3))
        self.assertFalse(_.lt(3, 3))
        self.assertFalse(_.lt(3, 1))

    def test_lte(self):
        self.assertTrue(_.lte(1, 3))
        self.assertTrue(_.lte(3, 3))
        self.assertFalse(_.lte(3, 1))

    def test_to_array(self):
        self.assertEqual(_.to_array({'a': 1, 'b': 2}), [1, 2])
        self.assertEqual(_.to_array('abc'), ['a', 'b', 'c'])
        self.assertEqual(_.to_array(1), [])
        self.assertEqual(_.to_array(None), [])

    def test_toInteger(self):
        self.assertEqual(_.to_integer(3.2), 3)
        self.assertEqual(_.to_integer('3.2'), 3)

    def test_toLength(self):
        self.assertEqual(_.to_length(3.2), 3)
        self.assertEqual(_.to_length('3.2'), 3)

    def test_toNumber(self):
        self.assertEqual(_.to_number(3.2), 3.2)
        self.assertEqual(_.to_number('3.2'), 3.2)

    def test_toSafeInteger(self):
        self.assertEqual(_.to_safe_integer(3.2), 3)
        self.assertEqual(_.to_safe_integer(float('inf')), 9223372036854775807)
        self.assertEqual(_.to_safe_integer(
            float('-inf')), -9223372036854775808)

    def test_toString(self):
        self.assertIsInstance(_.to_string(-9), str)


if __name__ == '__main__':
    unittest.main()

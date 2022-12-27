"""
object
"""

import unittest
import libs as _


class TestObjectMethods(unittest.TestCase):
    def test_assign(self):
        self.assertEqual(_.assign({'a': 0}, {'a': 1}, {
                         'b': 1}), {'a': 1, 'b': 1})

    def test_at(self):
        obj = {'a': {'b': {'c': 3}, 'd': 4}}
        self.assertEqual(_.at(obj, ['a.b.c', 'a.d']), [3, 4])

    def test_defaults(self):
        self.assertEqual(_.defaults(
            {'a': 1}, {'b': 2}, {'a': 3}), {'a': 1, 'b': 2})

    def test_find_key(self):
        users = {
            'barney':    {'age': 36, 'active': True},
            'fred':        {'age': 40, 'active': False},
            'pebbles': {'age': 1,    'active': True}
        }
        self.assertEqual(_.find_key(users, lambda u: u['age'] < 40), 'barney')
        self.assertEqual(
            _.find_key(users, lambda u: u['age'] == 1 and u['active']), 'pebbles')
        self.assertEqual(_.find_key(users, lambda u: not u['active']), 'fred')
        self.assertEqual(_.find_key(users, lambda u: u['active']), 'barney')

    def test_for_in(self):
        object = {
            'a': 1,
            'b': 2,
            'c': 3
        }
        _.for_in(object, lambda value, key: print(key, value))

    def test_for_in_right(self):
        object = {
            'a': 1,
            'b': 2,
            'c': 3
        }
        _.for_in_right(object, lambda value, key: print(key, value))

    def test_for_own(self):
        object = {
            'a': 1,
            'b': 2,
            'c': 3
        }
        _.for_own(object, lambda value, key: print(key, value))

    def test_for_own_right(self):
        object = {
            'a': 1,
            'b': 2,
            'c': 3
        }
        _.for_own_right(object, lambda value, key: print(key, value))

    def test_find_last_key(self):
        users = {
            'barney':    {'age': 36, 'active': True},
            'fred':        {'age': 40, 'active': False},
            'pebbles': {'age': 1,    'active': True}
        }
        self.assertEqual(_.find_last_key(
            users, lambda u: u['age'] < 40), 'pebbles')
        self.assertEqual(_.find_last_key(
            users, lambda u: u['age'] == 36 and u['active']), 'barney')
        self.assertEqual(_.find_last_key(
            users, lambda u: not u['active']), 'fred')
        self.assertEqual(_.find_last_key(
            users, lambda u: u['active']), 'pebbles')

    def test_functions(self):
        object = {
            'a': _.constant('a'),
            'b': _.constant('b')
        }
        self.assertEqual(_.functions(object), ['a', 'b'])

    def test_functions_in(self):
        object = {
            'a': _.constant('a'),
            'b': _.constant('b'),
            'c': _.constant('c')
        }
        self.assertEqual(_.functions_in(object), ['a', 'b', 'c'])

    def test_get(self):
        obj = {'a': {'b': 1}}
        self.assertEqual(_.get(obj, 'a.b'), 1)
        self.assertEqual(_.get(obj, 'a.b.c'), None)

    def test_has(self):
        object = {'a': {'b': 2}}
        self.assertTrue(_.has(object, 'a'))
        self.assertTrue(_.has(object, 'a.b'))
        self.assertFalse(_.has(object, 'c'))

    def test_invert(self):
        self.assertEqual(_.invert({'a': 1, 'b': 2, 'c': 1}), {
                         '1': 'c', '2': 'b'})

    def test_invertBy(self):
        self.assertEqual(_.invert_by({'a': 1, 'b': 2, 'c': 1}), {
                         '1': ['a', 'c'], '2': ['b']})

    def test_keys(self):
        self.assertEqual(_.keys({'a': 1, 'b': 2}), ['a', 'b'])

    def test_keysIn(self):
        self.assertEqual(_.keys({'a': 1, 'b': 2, 'c': 3}), ['a', 'b', 'c'])

    def test_mapKeys(self):
        self.assertEqual(_.map_keys({'a': 1, 'b': 2}, lambda value, key: str(
            key) + str(value)), {'a1': 1, 'b2': 2})

    def test_mapValues(self):
        users = {
            'fred':        {'user': 'fred',        'age': 40},
            'pebbles': {'user': 'pebbles', 'age': 1}
        }
        _.map_values(users, lambda o: o['age'])
        self.assertEqual(users, {'fred': 40, 'pebbles': 1})

    def test_omit(self):
        object = {'a': 1, 'b': '2', 'c': 3}
        self.assertEqual(_.omit(object, ['a', 'c']), {'b': '2'})

    def test_omitBy(self):
        object = {'a': 1, 'b': '2', 'c': 3}
        self.assertEqual(_.omit_by(object, _.is_number), {'b': '2'})

    def test_pick(self):
        obj = {'a': 1, 'b': '2', 'c': 3}
        self.assertEqual(_.pick(obj, ['a', 'c']), {'a': 1, 'c': 3})

    def test_pickBy(self):
        object = {'a': 1, 'b': '2', 'c': 3}
        self.assertEqual(_.pick_by(object, _.is_number), {'a': 1, 'c': 3})

    def test_result(self):
        obj = {'a': {'b': {'c1': 3, 'c2': _.constant(4)}}}
        self.assertEqual(_.result(obj, 'a.b.c1'), 3)
        self.assertEqual(_.result(obj, 'a.b.c2'), 4)

    def test_setObject(self):
        obj = {'a': {'b': {'c': 0}}}
        self.assertEqual(_.set_object(obj, 'a.b.c', 1), {'a': {'b': {'c': 1}}})

    def test_toPairs(self):
        obj = {'a': 1, 'b': 2}
        self.assertEqual(_.to_pairs(obj), [['a', 1], ['b', 2]])

    def test_toPairsIn(self):
        obj = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(_.to_pairs_in(obj), [['a', 1], ['b', 2], ['c', 3]])

    def test_update(self):
        obj = {'a': {'b': {'c': 3}}}
        _.update(obj, 'a.b.c', lambda n: n * n)
        self.assertEqual(obj, {'a': {'b': {'c': 9}}})

    def test_values(self):
        obj = {'a': 1, 'b': 2}
        self.assertEqual(_.values(obj), [1, 2])

    def test_valuesIn(self):
        obj = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(_.values_in(obj), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()

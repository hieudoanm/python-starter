"""
Collection Test
"""

import unittest
import libs as _


class TestCollectionMethods(unittest.TestCase):
    def test_count_by(self):
        self.assertEqual(_.count_by([6.1, 4.2, 6.3], _.floor), {4: 1, 6: 2})

    def test_every(self):
        self.assertTrue(_.every([4, 6], lambda n: n > 2))
        self.assertFalse(_.every([4, 6], lambda n: n > 4))

    def test_filter(self):
        self.assertEqual(_.filter([4, 6], lambda n: n % 3 == 0), [6])

    def test_find(self):
        users = [
            {'user': 'barney',    'age': 36, 'active': True},
            {'user': 'fred',        'age': 40, 'active': False},
            {'user': 'pebbles', 'age': 1,    'active': True}
        ]
        self.assertEqual(_.find(users, lambda u: u['age'] < 40), {
                         'user': 'barney',    'age': 36, 'active': True})
        self.assertEqual(_.find(users, lambda u: u['active']), {
                         'user': 'barney',    'age': 36, 'active': True})
        self.assertEqual(_.find(users, lambda u: u['age'] > 40), None)

    def test_find_last(self):
        self.assertEqual(_.find_last([1, 2, 3, 4], lambda n: n % 2 == 1), 3)

    def test_flat_map(self):
        self.assertEqual(_.flat_map([1, 2], lambda n: [n, n]), [1, 1, 2, 2])

    def test_flat_map_deep(self):
        self.assertEqual(_.flat_map_deep(
            [1, 2], lambda n: [[[n, n]]]), [1, 1, 2, 2])

    def test_flat_mapDepth(self):
        self.assertEqual(_.flat_map_depth([1, 2], lambda n: [
                         [[n, n]]], 2), [[1, 1], [2, 2]])

    def test_for_each(self):
        _.for_each([1, 2], lambda n: print('n', n))

    def test_for_each_right(self):
        _.for_each_right([1, 2], lambda n: print('n', n))

    def test_group_by(self):
        self.assertEqual(_.group_by([6.1, 4.2, 6.3], _.floor), {
                         '4': [4.2], '6': [6.1, 6.3]})

    def test_includes(self):
        self.assertTrue(_.includes([1, 2, 3], 1))
        self.assertFalse(_.includes([1, 2, 3], 1, 2))

    def test_invoke_map(self):
        self.assertEqual(_.invoke_map([[5, 1, 7], [3, 2, 1]], sorted), [
                         [1, 5, 7], [1, 2, 3]])
        self.assertEqual(_.invoke_map([123, 456], _.split, ''), [
                         ['1', '2', '3'], ['4', '5', '6']])

    def test_key_by(self):
        array = [
            {'dir': 'left', 'code': 97},
            {'dir': 'right', 'code': 100}
        ]
        obj = _.key_by(array, lambda i: i['dir'])
        self.assertEqual(obj, {'left': {'dir': 'left', 'code': 97}, 'right': {
                         'dir': 'right', 'code': 100}})

    def test_map(self):
        self.assertEqual(_.map([4, 8], lambda n: n * n), [16, 64])

    def test_partition(self):
        users = [
            {'user': 'barney',    'age': 36, 'active': False},
            {'user': 'fred',        'age': 40, 'active': True},
            {'user': 'pebbles', 'age': 1,    'active': False}
        ]
        self.assertEqual(_.partition(users, lambda o: o['active']), [
            [{'user': 'fred',        'age': 40, 'active': True}],
            [{'user': 'barney',    'age': 36, 'active': False}, {
                'user': 'pebbles', 'age': 1,    'active': False}]
        ])

    def test_reduce(self):
        self.assertEqual(_.reduce([1, 2], lambda sum, n: sum + n, 0), 3)

        def iteratee(result, value, key):
            if str(value) in result:
                result[str(value)].append(key)
            else:
                result[str(value)] = [key]
            return result
        self.assertEqual(_.reduce({'a': 1, 'b': 2, 'c': 1}, iteratee, {}), {
                         '1': ['a', 'c'], '2': ['b']})

    def test_reduce_right(self):
        array = [[0, 1], [2, 3], [4, 5]]
        self.assertEqual(_.reduce_right(array, lambda flattened, other: _.concat(
            flattened, other), []), [4, 5, 2, 3, 0, 1])

    def test_reject(self):
        users = [
            {'user': 'barney', 'age': 36, 'active': False},
            {'user': 'fred',     'age': 40, 'active': True}
        ]
        self.assertEqual(_.reject(users, lambda o: not o['active']), [
                         {'user': 'fred',     'age': 40, 'active': True}])

    def test_sample(self):
        array = [1, 2, 3, 4]
        sample = _.sample(array)
        self.assertTrue(sample in array)

    def test_sample_size(self):
        samples = _.sample_size([1, 2, 3], 2)
        print('samples', samples)
        self.assertEqual(len(samples), 2)

    def test_shuffle(self):
        array = [1, 2, 3, 4]
        _.shuffle(array)
        self.assertEqual(len(array), len(array))

    def test_size(self):
        self.assertEqual(_.size('pebbles'), 7)
        self.assertEqual(_.size([1, 2, 3]), 3)
        self.assertEqual(_.size({'a': 1, 'b': 2}), 2)

    def test_some(self):
        self.assertTrue(_.some([4, 6], lambda n: n > 2))
        self.assertFalse(_.some([4, 6], lambda n: n > 8))

    def test_sort_by(self):
        users = [
            {'user': 'fred',     'age': 48},
            {'user': 'barney', 'age': 36},
            {'user': 'fred',     'age': 40},
            {'user': 'barney', 'age': 34}
        ]
        self.assertEqual(_.sort_by(users, 'user'), [
            {'user': 'barney', 'age': 36},
            {'user': 'barney', 'age': 34},
            {'user': 'fred',     'age': 48},
            {'user': 'fred',     'age': 40}
        ])

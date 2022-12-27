"""
Array Test
"""

import unittest
import libs as _


class TestArrayMethods(unittest.TestCase):
    """
    Test Array
    """

    def test_chunk(self):
        """
        Test Chunk
        """
        self.assertEqual(_.chunk(['a', 'b', 'c', 'd'], 2), [
                         ['a', 'b'], ['c', 'd']])
        self.assertEqual(_.chunk(['a', 'b', 'c', 'd'], 3), [
                         ['a', 'b', 'c'], ['d']])

    def test_compact(self):
        """
        Test Concat
        """
        self.assertEqual(_.compact([0, 1, False, 2, '', 3]), [1, 2, 3])

    def test_concat(self):
        """
        Test Compact
        """
        self.assertEqual(_.concat([1], 2, [3], [[4]]), [1, 2, 3, [4]])

    def test_difference(self):
        self.assertEqual(_.difference([2, 1], [2, 3]), [1])

    def test_differenceBy(self):
        self.assertEqual(_.difference_by(
            [2.1, 1.2], [2.3, 3.4], _.floor), [1.2])

    def test_drop(self):
        self.assertEqual(_.drop([1, 2, 3]), [2, 3])
        self.assertEqual(_.drop([1, 2, 3], 2), [3])
        self.assertEqual(_.drop([1, 2, 3], 5), [])
        self.assertEqual(_.drop([1, 2, 3], 0), [1, 2, 3])

    def test_drop_right(self):
        self.assertEqual(_.drop_right([1, 2, 3]), [1, 2])
        self.assertEqual(_.drop_right([1, 2, 3], 2), [1])
        self.assertEqual(_.drop_right([1, 2, 3], 5), [])
        self.assertEqual(_.drop_right([1, 2, 3], 0), [1, 2, 3])

    def test_drop_right_while(self):
        array = [
            {'user': 'barney',    'active': True},
            {'user': 'fred',        'active': False},
            {'user': 'pebbles', 'active': False}
        ]
        _.drop_right_while(array, lambda o: not o['active'])
        self.assertEqual(array, [{'user': 'barney', 'active': True}])

    def test_drop_while(self):
        array = [
            {'user': 'barney',    'active': False},
            {'user': 'fred',        'active': False},
            {'user': 'pebbles', 'active': True}
        ]
        _.drop_while(array, lambda o: not o['active'])
        self.assertEqual(array, [{'user': 'pebbles', 'active': True}])

    def test_fill(self):
        self.assertEqual(_.fill([1, 2, 3], 'a'), ['a', 'a', 'a'])
        self.assertEqual(_.fill([4, 6, 8, 10], '*', 1, 3), [4, '*', '*', 10])

    def test_find_index(self):
        users = [
            {'user': 'barney',    'active': False},
            {'user': 'fred',        'active': False},
            {'user': 'pebbles', 'active': True}
        ]
        self.assertEqual(_.find_index(
            users, lambda o: o['user'] == 'barney'), 0)
        self.assertEqual(_.find_index(
            users, lambda o: o['user'] == 'fred' and not o['active']), 1)
        self.assertEqual(_.find_index(users, lambda o: not o['active']), 0)
        self.assertEqual(_.find_index(users, lambda o: o['active']), 2)

    def test_find_last_index(self):
        users = [
            {'user': 'barney',    'active': True},
            {'user': 'fred',        'active': False},
            {'user': 'pebbles', 'active': False}
        ]
        self.assertEqual(_.find_last_index(
            users, lambda o: o['user'] == 'pebbles'), 2)
        self.assertEqual(_.find_last_index(
            users, lambda o: o['user'] == 'barney' and o['active']), 0)
        self.assertEqual(_.find_last_index(
            users, lambda o: not o['active']), 2)
        self.assertEqual(_.find_last_index(users, lambda o: o['active']), 0)

    def test_flatten(self):
        array = [1, [2, [3, [4]], 5]]
        self.assertEqual(_.flatten(array), [1, 2, [3, [4]], 5])

    def test_flattenDeep(self):
        array = [1, [2, [3, [4]], 5]]
        self.assertEqual(_.flattenDeep(array), [1, 2, 3, 4, 5])

    def test_flatten_depth(self):
        array = [1, [2, [3, [4]], 5]]
        self.assertEqual(_.flatten_depth(array), [1, 2, [3, [4]], 5])
        self.assertEqual(_.flatten_depth(array, 2), [1, 2, 3, [4], 5])

    def test_fromPairs(self):
        self.assertEqual(_.from_pairs([['a', 1], ['b', 2]]), {'a': 1, 'b': 2})

    def test_head(self):
        self.assertEqual(_.head([1, 2, 3]), 1)

    def test_index_of(self):
        self.assertEqual(_.index_of([1, 2, 1, 2], 2), 1)
        self.assertEqual(_.index_of([1, 2, 1, 2], 2, 2), 3)

    def test_initial(self):
        self.assertEqual(_.initial([1, 2, 3]), [1, 2])

    def test_intersection(self):
        self.assertEqual(_.intersection([1, 2], [1, 3], [1, 4]), [1])

    def test_join(self):
        self.assertEqual(_.join(['a', 'b', 'c'], '~'), 'a~b~c')

    def test_last(self):
        self.assertEqual(_.last([1, 2, 3]), 3)

    def test_last_index_of(self):
        self.assertEqual(_.last_index_of([1, 2, 1, 2], 2), 3)
        self.assertEqual(_.last_index_of([1, 2, 1, 2], 2, 2), 1)

    def test_nth(self):
        self.assertEqual(_.nth(['a', 'b', 'c', 'd'], 1), 'b')

    def test_pull(self):
        array = ['a', 'b', 'c', 'a', 'b', 'c']
        _.pull(array, 'a', 'c')
        self.assertEqual(array, ['b', 'b'])

    def test_pull_all(self):
        array = ['a', 'b', 'c', 'a', 'b', 'c']
        _.pull_all(array, ['a', 'c'])
        self.assertEqual(array, ['b', 'b'])

    def test_pull_at(self):
        array = ['a', 'b', 'c', 'd']
        pulled = _.pull_at(array, [1, 3])
        self.assertEqual(array, ['a', 'c'])
        self.assertEqual(pulled, ['b', 'd'])

    def test_remove(self):
        array = [1, 2, 3, 4]
        evens = _.remove(array, lambda n: n % 2 == 0)
        self.assertEqual(evens, [2, 4])
        self.assertEqual(array, [1, 3])

    def test_reverse(self):
        self.assertEqual(_.reverse([1, 2, 3]), [3, 2, 1])

    def test_slice(self):
        self.assertEqual(_.slice([1, 2, 3, 4], 1), [2, 3, 4])
        self.assertEqual(_.slice([1, 2, 3, 4], 1, 3), [2, 3])

    def test_sorted_index(self):
        self.assertEqual(_.sorted_index([30, 50], 40), 1)

    def test_sortedLast_index(self):
        self.assertEqual(_.sorted_last_index([4, 5, 5, 5, 6], 5), 4)

    def test_sortedUniq(self):
        self.assertEqual(_.sorted_uniq([1, 1, 2]), [1, 2])

    def test_tail(self):
        self.assertEqual(_.tail([1, 2, 3]), [2, 3])

    def test_take(self):
        self.assertEqual(_.take([1, 2, 3]), [1])
        self.assertEqual(_.take([1, 2, 3], 2), [1, 2])
        self.assertEqual(_.take([1, 2, 3], 5), [1, 2, 3])
        self.assertEqual(_.take([1, 2, 3], 0), [])

    def test_take_right(self):
        """
        Take Right
        """
        self.assertEqual(_.take_right([1, 2, 3]), [3])
        self.assertEqual(_.take_right([1, 2, 3], 2), [2, 3])
        self.assertEqual(_.take_right([1, 2, 3], 5), [1, 2, 3])
        self.assertEqual(_.take_right([1, 2, 3], 0), [])

    def test_take_right_while(self):
        """
        Take Right White
        """
        users = [
            {'user': 'barney',    'active': False},
            {'user': 'fred',        'active': False},
            {'user': 'pebbles', 'active': True}
        ]
        _.take_right_while(users, lambda o: not o['active'])
        self.assertEqual(users, [
            {'user': 'barney',    'active': False},
            {'user': 'fred',        'active': False},
        ])

    def test_take_while(self):
        """
        Test Take While
        """
        users = [
            {'user': 'barney',    'active': False},
            {'user': 'fred',        'active': False},
            {'user': 'pebbles', 'active': True}
        ]
        _.take_while(users, lambda o: not o['active'])
        self.assertEqual(users, [
            {'user': 'barney',    'active': False},
            {'user': 'fred',        'active': False},
        ])

    def test_union(self):
        self.assertEqual(_.union([2], [1, 2]), [2, 1])

    def test_uniq(self):
        self.assertEqual(_.uniq([2, 1, 2]), [1, 2])

    def test_unzip(self):
        self.assertEqual(_.unzip([['a', 1, True], ['b', 2, False]]), [
                         ['a', 'b'], [1, 2], [True, False]])

    def test_unzip_with(self):
        self.assertEqual(_.unzip_with(
            [[1, 10, 100], [2, 20, 200]], _.add), [3, 30, 300])

    def test_without(self):
        self.assertEqual(_.without([2, 1, 2, 3], 1, 2), [3])

    def test_xor(self):
        self.assertEqual(_.xor([2, 1], [2, 3]), [1, 3])

    def test_zip(self):
        grouped = _.zip(["a", "b", None], [1, 2], [True, False], [])
        expected = [
            ["a", 1, True, None],
            ["b", 2, False, None],
            [None, None, None, None]
        ]
        self.assertEqual(grouped, expected)

    def test_zip_object(self):
        """
        Test Zip Object
        """
        self.assertEqual(_.zip_object(['a', 'b'], [1, 2]), {'a': 1, 'b': 2})

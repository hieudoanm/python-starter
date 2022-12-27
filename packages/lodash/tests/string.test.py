"""
string
"""

import unittest
import libs as _


class TestStringMethods(unittest.TestCase):
    def test_camelCase(self):
        self.assertEqual(_.camel_case('Foo bar'), 'fooBar')

    def test_capitalize(self):
        self.assertEqual(_.capitalize('FOO'), 'Foo')

    def test_ends_with(self):
        self.assertTrue(_.ends_with('abc', 'c'))
        self.assertFalse(_.ends_with('abc', 'b'))
        self.assertTrue(_.ends_with('abc', 'b', 2))

    def test_kebabCase(self):
        self.assertEqual(_.kebab_case('Foo Bar'), 'foo-bar')

    def test_lowerCase(self):
        self.assertEqual(_.lower_case('--Foo--Bar--'), 'foo bar')
        self.assertEqual(_.lower_case('__Foo__Bar__'), 'foo bar')

    def test_lowerFirst(self):
        self.assertEqual(_.lower_first('Fred'), 'fred')
        self.assertEqual(_.lower_first('F_rED'), 'f_rED')

    def test_pad(self):
        self.assertEqual(_.pad('abc', 8), '    abc     ')
        self.assertEqual(_.pad('abc', 8, '_-'), '_-abc_-_')
        self.assertEqual(_.pad('abc', 3), 'abc')

    def test_padEnd(self):
        self.assertEqual(_.pad_end('abc', 6), 'abc     ')
        self.assertEqual(_.pad_end('abc', 6, '_-'), 'abc_-_')
        self.assertEqual(_.pad_end('abc', 3), 'abc')

    def test_padStart(self):
        self.assertEqual(_.pad_start('abc', 6), '     abc')
        self.assertEqual(_.pad_start('abc', 6, '_-'), '_-_abc')
        self.assertEqual(_.pad_start('abc', 3), 'abc')

    def test_parseInt(self):
        self.assertEqual(_.parse_int('08'), 8)

    def test_repeat(self):
        self.assertEqual(_.repeat('*', 3), '***')

    def test_replace(self):
        self.assertEqual(
            _.replace('placeholder', 'placeholder', 'test'), 'test')

    def test_snakeCase(self):
        self.assertEqual(_.snake_case('Foo Bar'), 'foo_bar')

    def test_split(self):
        self.assertEqual(_.split('a-b-c', '-'), ['a', 'b', 'c'])
        self.assertEqual(_.split('a-b-c', '-', 2), ['a', 'b'])

    def test_startCase(self):
        self.assertEqual(_.start_case('--foo--bar--'), 'Foo Bar')
        self.assertEqual(_.start_case('__foo__bar__'), 'Foo Bar')

    def test_starts_with(self):
        self.assertTrue(_.starts_with('test', 't'))
        self.assertFalse(_.starts_with('test', 'e'))
        self.assertTrue(_.starts_with('test', 'e', 1))

    def test_toLower(self):
        self.assertEqual(_.to_lower('TEST'), 'test')

    def test_toUpper(self):
        self.assertEqual(_.to_upper('test'), 'TEST')

    def test_trim(self):
        self.assertEqual(_.trim('     abc     '), 'abc')

    def test_trimEnd(self):
        self.assertEqual(_.trim_end('     abc     '), '     abc')

    def test_trimStart(self):
        self.assertEqual(_.trim_start('     abc     '), 'abc     ')

    def test_truncate(self):
        self.assertEqual(_.truncate(
            'hi-diddly-ho there, neighborino'), 'hi-diddly-ho there, neighbo ...')

    def test_upperCase(self):
        self.assertEqual(_.upper_case('--Foo--Bar--'), 'FOO BAR')
        self.assertEqual(_.upper_case('__Foo__Bar__'), 'FOO BAR')

    def test_upper_first(self):
        self.assertEqual(_.upper_first('tEST'), 'Test')

    def test_words(self):
        self.assertEqual(_.words('fred, barney, & pebbles'),
                         ['fred', 'barney', 'pebbles'])


if __name__ == '__main__':
    unittest.main()

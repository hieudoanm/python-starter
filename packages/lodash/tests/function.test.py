import unittest
import libs as _


class TestFunctionMethods(unittest.TestCase):
    def test_debouce(self):
        def func():
            print('wait for 1 seconds')
        _.debounce(func, 1)

    def test_delay(self):
        def func(text):
            print(text)
        _.delay(func, 1, "wait for 1 seconds")

"""
util
"""

import uuid

def constant(value):
    """
    constant
    """
    return value

def default_to(value, default_value):
    """
    defaultTo
    """
    if value is None:
        return default_value
    return value

def identity(*args):
    """
    identity
    """
    value = args[0]
    return value

def noop():
    """
    noop
    """
    return None

def range_array(_start, _end = None, step = 1):
    """
    range_array
    """
    start = 0
    end = _start
    if _end is not None:
        start = _start
        end = _end
    array = [*range(start, end, step)]
    return array

def range_right(start, end = None, step = 1):
    """
    range_right
    """
    array = range_array(start, end, step)
    array.reverse()
    return array

def stub_array():
    """
    stub_array
    """
    return []

def stub_false():
    """
    stub_false
    """
    return False

def stub_object():
    """
    stub_object
    """
    return {}

def stub_string():
    """
    stub_string
    """
    return ''

def stub_true():
    """
    stub_true
    """
    return True

def times(number, callback = None):
    """
    times
    """
    array = [*range(0, number, 1)]
    if callback is None:
        return array
    for index, _ in enumerate(array):
        array[index] = callback
    return array

def to_path(value):
    """
    to_path
    """
    value = value.replace("[", ".")
    value = value.replace("]", ".")
    return value.split(".")

def unique_id(prefix = ''):
    """
    unique_id
    """
    return prefix + str(uuid.uuid4())

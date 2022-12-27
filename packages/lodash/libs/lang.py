"""
lang
"""

import copy
import math
import sys

def cast_array(value):
    """
    cast_array
    """
    return [value]

def conforms_to(object_var, source):
    """
    conforms_to
    """
    keys = list(source.keys())
    key = keys[0]
    value = object_var[key]
    return source[key](value)

def clone(value):
    """
    clone
    """
    return copy.copy(value)

def clone_deep(value):
    """
    clone_deep
    """
    return copy.deepcopy(value)

def clone_deep_with(value, customizer):
    """
    clone_deep_with
    """
    deep = clone_deep(value)
    return customizer(deep)

def clone_with(value, customizer):
    """
    clone_with
    """
    shallow = clone(value)
    return customizer(shallow)

def eq(value, other):
    """
    eq
    """
    return value == other

def gt(value, other):
    """
    gt
    """
    return value > other

def gte(value, other):
    """
    gte
    """
    return value >= other

def is_array(value):
    """
    is_array
    """
    return isinstance(value, list)

def is_array_like(value):
    """
    is_array_like
    """
    return isinstance(value, list) or isinstance(value, str)

def is_array_like_object(value):
    """
    is_array_like_object
    """
    return isinstance(value, list)

def is_boolean(value):
    """
    is_boolean
    """
    return isinstance(value, bool)

def is_empty(value):
    """
    is_empty
    """
    if isinstance(value, list) and len(value) > 0:
        return False
    if isinstance(value, dict) and len(list(value.keys())) > 0:
        return False
    return True

def is_equal(value, other):
    """
    is_equal
    """
    return value == other

def is_equal_with(value, other, customizer):
    """
    is_equal_with
    """
    return customizer(value) and customizer(other)

def is_finite(value):
    """
    is_finite
    """
    if not is_number(value):
        return False
    return math.isfinite(value)

def is_function(value):
    """
    is_function
    """
    return str(type(value)) == "<class 'function'>"

def is_integer(value):
    """
    is_integer
    """
    return isinstance(value, int)

def is_length(value):
    """
    is_length
    """
    return is_integer(value)

def is_match(obj, source):
    """
    is_match
    """
    _keys = list(source.keys())
    flag = True
    for key in _keys:
        if obj[key] != source[key]:
            flag = False
            break
    return flag

def is_match_with(obj, source, customizer):
    """
    is_match_with
    """
    _keys = list(source.keys())
    flag = True
    for key in _keys:
        if customizer(obj[key]) != customizer(source[key]):
            flag = False
            break
    return flag

def is_nil(value):
    """
    is_nil
    """
    return value is None

def is_null(value):
    """
    is_null
    """
    return value is None

def is_number(value):
    """
    is_number
    """
    return isinstance(value, float) or isinstance(value, int)

def is_object(value):
    """
    is_object
    """
    return isinstance(value, dict)

def is_object_like(value):
    """
    is_object_like
    """
    return isinstance(value, dict) or isinstance(value, list)

def is_safe_integer(value):
    """
    is_safe_integer
    """
    if not isinstance(value, int):
        return False
    upper = sys.maxsize
    lower = - upper - 1
    return lower < value and value < upper

def is_set(value):
    """
    is_set
    """
    return isinstance(value, set)

def is_string(value):
    """
    is_string
    """
    return isinstance(value, str)

def is_undefined(value):
    """
    is_undefined
    """
    return value is None

def lt(value, other):
    """
    lt
    """
    return value < other

def lte(value, other):
    """
    lte
    """
    return value <= other

def to_array(value):
    """
    to_array
    """
    if isinstance(value, dict):
        return list(value.values())
    if isinstance(value, str):
        return [c for c in value]
    if isinstance(value, list):
        return value
    return []

def to_integer(value):
    """
    to_integer
    """
    if isinstance(value, str):
        return int(float(value))
    return int(value)

def to_length(value):
    """
    to_length
    """
    return to_integer(value)

def to_number(value):
    """
    to_number
    """
    return float(value)

def to_safe_integer(value):
    """
    to_safe_integer
    """
    upper = sys.maxsize
    lower = - upper - 1
    if value < lower:
        return lower
    elif value > upper:
        return upper
    if not isinstance(value, int):
        value = int(value)
    return value

def to_string(value):
    """
    to_string
    """
    if value is None:
        return ''
    return str(value)

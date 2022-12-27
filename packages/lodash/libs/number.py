"""
number
"""

import random as rand

def clamp(number, lower, upper):
    """
    clamp
    """
    if lower > upper:
        return
    if number < lower:
        return lower
    elif number > upper:
        return upper
    else:
        return number

def in_range(number, x_value, y_value = None):
    """
    in_range
    """
    start = 0
    stop = x_value
    if y_value is not None:
        start = x_value
        stop = y_value
    return start < number and number < stop

def random(x_value, y_value = None, step = 1):
    """
    random
    """
    start = 0
    end = x_value
    if y_value is not None:
        start = x_value
        end = y_value
    return rand.randrange(start, end, step)

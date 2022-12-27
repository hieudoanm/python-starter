"""
math
"""

import math

def add(a_value, b_value):
    """
    add
    """
    return a_value + b_value

def ceil(number):
    """
    ceil
    """
    return math.ceil(number)

def divide(a_value, b_value):
    """
    divide
    """
    return a_value / b_value

def floor(number):
    """
    floor
    """
    return math.floor(number)

def max(numbers):
    """
    max
    """
    if len(numbers) == 0:
        return
    max_value = float('-inf')
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

def max_by(objects, iteratee):
    """
    max_by
    """
    if len(objects) == 0:
        return
    numbers = []
    for obj in objects:
        number = obj[iteratee]
        numbers.append(number)
    return max(numbers)

def mean(numbers):
    """
    mean
    """
    length = len(numbers)
    if length == 0:
        return 0
    sum_value = sum(numbers)
    return sum_value / length

def mean_by(objects, iteratee):
    """
    mean_by
    """
    if len(objects) == 0:
        return
    numbers = []
    for obj in objects:
        number = obj[iteratee]
        numbers.append(number)
    return mean(numbers)

def min(numbers):
    """
    min
    """
    if len(numbers) == 0:
        return
    min_value = float('inf')
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

def min_by(objects, iteratee):
    """
    min_by
    """
    if len(objects) == 0:
        return
    numbers = []
    for obj in objects:
        number = obj[iteratee]
        numbers.append(number)
    return min(numbers)

def multiply(a_value, b_value):
    """
    multiply
    """
    return a_value * b_value

def round_number(number, precision = 0):
    """
    round_number
    """
    return round(number, precision)

def subtract(a_value, b_value):
    """
    subtract
    """
    return a_value - b_value

# Recursion
def sum(numbers):
    """
    sum
    """
    if len(numbers) == 0:
        return 0
    first = numbers.pop(0)
    return first + sum(numbers)

def sum_by(objects, iteratee):
    """
    sum_by
    """
    if len(objects) == 0:
        return
    numbers = []
    for obj in objects:
        number = obj[iteratee]
        numbers.append(number)
    return sum(numbers)

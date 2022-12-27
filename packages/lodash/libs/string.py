"""
string
"""

import math

def camel_case(string):
    """
    camel_case
    """
    array = split(string, ' ')
    first = array[0].lower()
    new_array = []
    for char in array[1:len(array)]:
        new_char = capitalize(char)
        new_array.append(new_char)
    new_array.insert(0, first)
    return "".join(new_array)

def capitalize(string):
    """
    capitalize
    """
    first = string[0].capitalize()
    rest = string[1:len(string)].lower()
    return first + rest

def ends_with(string, target, position = 1):
    """
    ends_with
    """
    return string[len(string) - position] == target

def kebab_case(string):
    """
    kebab_case
    """
    array1 = split(string, ' ')
    array2 = []
    for item in array1:
        new_item = item.lower()
        array2.append(new_item)
    return "-".join(array2)

def lower_case(string):
    """
    lower_case
    """
    new_array = []
    for char in string:
        new_item = char if char.isalpha() else ' '
        new_array.append(new_item)
    result = "".join(new_array).lower().strip()
    return " ".join(result.split())

def lower_first(string):
    """
    lower_first
    """
    first = string[0].lower()
    return first + string[1:len(string)]

def pad(string, length = 0, chars = ' '):
    """
    pad
    """
    padding = length - len(string)
    if padding <= 0:
        return string
    padding_start = math.floor(padding / 2)
    padding_end = padding - padding_start
    start = (chars * padding_start)[0:padding_start]
    end = (chars * padding_end)[0:padding_end]
    return start + string + end

def pad_end(string, length = 0, chars = ' '):
    """
    pad_end
    """
    padding = length - len(string)
    end = (chars * padding)[0:padding]
    return string + end

def pad_start(string, length = 0, chars = ' '):
    """
    pad_start
    """
    padding = length - len(string)
    start = (chars * padding)[0:padding]
    return start + string

def parse_int(string):
    """
    parse_int
    """
    return int(string)

def repeat(string, times):
    """
    repeat
    """
    return string * times

def replace(string, pattern, replacement):
    """
    replace
    """
    return string.replace(pattern, replacement)

def snake_case(string):
    """
    snake_case
    """
    array1 = split(string, ' ')
    array2 = []
    for item in array1:
        new_item = item.lower()
        array2.append(new_item)
    return "_".join(array2)

def split(value, separator = '', limit = None):
    """
    split
    """
    string = str(value)
    if separator == '':
        return [c for c in string]
    array = string.split(separator)
    return array[0:limit]

def start_case(string):
    """
    start_case
    """
    array1 = []
    for char in string:
        new_item = char if char.isalpha() else ' '
        array1.append(new_item)
    result = "".join(array1).lower().strip()
    array2 = []
    for word in result.split():
        array2.append(capitalize(word))
    return " ".join(array2)

def starts_with(string, target, position = 0):
    """
    starts_with
    """
    return string[position] == target

def to_lower(string):
    """
    to_lower
    """
    return string.lower()

def to_upper(string):
    """
    to_upper
    """
    return string.upper()

def trim(string):
    """
    trim
    """
    return string.strip()

def trim_end(string):
    """
    trim_end
    """
    return string.rstrip()

def trim_start(string):
    """
    trim_start
    """
    return string.lstrip()

def truncate(string, length = 30, omission = "..."):
    """
    truncate
    """
    omission_len = len(omission)
    short = length - omission_len
    return string[0:short] + " " + omission

def upper_case(string):
    """
    upper_case
    """
    new_array = []
    for char in string:
        new_item = char if char.isalpha() else ' '
        new_array.append(new_item)
    result = "".join(new_array).upper().strip()
    return " ".join(result.split())

def upper_first(string):
    """
    upper_first
    """
    return string.capitalize()

def words(string):
    """
    words
    """
    new_array = []
    for char in string:
        new_item = char if char.isalpha() else ' '
        new_array.append(new_item)
    result = "".join(new_array).strip()
    return result.split()

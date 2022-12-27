"""
array
"""

import copy


def chunk(array, size=1):
    """
    chunk
    """
    new_array = []
    for i in range(0, len(array), size):
        new_array.append(array[i:i + size])
    return new_array


def compact(array):
    """
    compact
    """
    new_array = []
    for item in array:
        if item:
            new_array.append(item)
    return new_array


def concat(array, *args):
    """
    concat
    """
    new_array = array
    for arg in args:
        if isinstance(arg, list):
            for item in arg:
                new_array.append(item)
        else:
            new_array.append(arg)
    return new_array


def difference(array, values):
    """
    difference
    """
    if len(array) == 0:
        return []
    _difference = []
    for i in array:
        if i not in values:
            _difference.append(i)
    return _difference


def difference_by(array, values, callback):
    """
    difference_by
    """
    new_values = []
    for value in values:
        new_values.append(callback(value))
    new_array = []
    for item in array:
        if callback(item) not in new_values:
            new_array.append(item)
    return new_array


def drop(array, number=1):
    """
    drop
    """
    return array[number:len(array)]


def drop_right(array, number=1):
    """
    drop_right
    """
    if number >= len(array):
        return []
    return array[0:len(array) - number]


def drop_right_while(array, callback):
    """
    drop_right_while
    """
    temp_array = copy.deepcopy(array)
    temp_array.reverse()
    for item in temp_array:
        flag = callback(item)
        if flag:
            array.remove(item)


def drop_while(array, callback):
    """
    drop_while
    """
    temp_array = copy.deepcopy(array)
    for item in temp_array:
        flag = callback(item)
        if flag:
            array.remove(item)


def fill(array, value, start=0, end=None):
    """
    fill
    """
    if end is None:
        end = len(array)
    for index, item in enumerate(array):
        if index < start or index > end - 1:
            array[index] = item
        else:
            array[index] = value
    return array

# Linear Search


def find_index(array, callback, from_index=0):
    """
    find_index
    """
    new_array = array[from_index:]
    index = -1
    for idx, item in enumerate(new_array):
        flag = callback(item)
        if flag:
            index = idx
            break
    return index


def find_last_index(array, callback, from_index=None):
    """
    find_last_index
    """
    new_array = array[0:from_index]
    index = -1
    for idx, item in enumerate(new_array):
        flag = callback(item)
        if flag:
            index = idx
    return index


def flatten(array):
    """
    flatten
    """
    new_array = []
    for item in array:
        if isinstance(item, list):
            new_array = concat(new_array, item)
        else:
            new_array.append(item)
    return new_array


def flatten_deep(array):
    """
    flatten_deep
    """
    if array == []:
        return array
    if isinstance(array[0], list):
        return flatten_deep(array[0]) + flatten_deep(array[1:])
    return array[:1] + flatten_deep(array[1:])


def flatten_depth(array, depth=1):
    """
    flatten_depth
    """
    new_array = array
    for _ in range(0, depth):
        new_array = flatten(new_array)
    return new_array


def from_pairs(pairs):
    """
    from_pairs
    """
    object_var = {}
    for pair in pairs:
        key, value = pair
        object_var[key] = value
    return object_var


def head(array):
    """
    head
    """
    if len(array) == 0:
        return
    return array[0]


def index_of(array, value, from_index=0):
    """
    index_of
    """
    if from_index >= len(array):
        return -1
    return array[from_index:len(array)].index(value) + from_index


def initial(array):
    """
    initial
    """
    return array[0:len(array) - 1]


def intersection(*args):
    """
    intersection
    """
    arrays = list(args)
    total = len(arrays)
    flatten_array = flatten_deep(arrays)
    item_count = {}
    for item in flatten_array:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    array = []
    for key, value in item_count.items():
        if value == total:
            array.append(key)
    return array


def join(array, separator):
    """
    join
    """
    return separator.join(array)


def last(array):
    """
    last
    """
    if len(array) == 0:
        return
    return array[len(array) - 1]


def last_index_of(array, value, from_index=None):
    """
    last_index_of
    """
    new_array = array[0:from_index]
    index = -1
    for idx, item in enumerate(new_array):
        if item == value:
            index = idx
    return index


def nth(array, number):
    """
    nth
    """
    return array[number]


def pull(array, *args):
    """
    pull
    """
    values = list(args)
    temp_array = copy.deepcopy(array)
    for item in temp_array:
        if item in values:
            array.remove(item)


def pull_all(array, values):
    """
    pull_all
    """
    temp_array = copy.deepcopy(array)
    for item in temp_array:
        if item in values:
            array.remove(item)


def pull_at(array, indexes):
    """
    pull_at
    """
    temp_array = copy.deepcopy(array)
    removed_array = []
    for index, item in enumerate(temp_array):
        if index in indexes:
            array.remove(item)
            removed_array.append(item)
    return removed_array


def remove(array, callback):
    """
    remove
    """
    new_array = []
    temp_array = copy.deepcopy(array)
    for item in temp_array:
        flag = callback(item)
        if flag:
            array.remove(item)
            new_array.append(item)
    return new_array

# _recursion


def reverse(array):
    """
    reverse
    """
    if len(array) == 0:
        return []
    sub = array[1:]
    reverse_sub = reverse(sub)
    reverse_sub.append(array[0])
    return reverse_sub


def slice(array, start=0, end=None):
    """
    slice
    """
    return array[start:end]


def sorted_index(array, value):
    """
    sorted_index
    """
    index = -1
    for idx, _ in enumerate(array):
        if idx < len(array) - 1:
            first = array[idx]
            second = array[idx + 1]
            if first <= value and value <= second:
                index = idx + 1
                break
        else:
            idx = index + 1
    return index


def sorted_last_index(array, value):
    """
    sorted_last_index
    """
    index = -1
    for idx, _ in enumerate(array):
        if idx < len(array) - 1:
            first = array[idx]
            second = array[idx + 1]
            if first <= value and value <= second:
                index = idx + 1
        else:
            idx = index + 1
    return index


def sorted_uniq(array):
    """
    sorted_uniq
    """
    new_array = []
    for item in array:
        if item not in new_array:
            new_array.append(item)
    return new_array


def tail(array):
    """
    tail
    """
    return array[1:len(array)]


def take(array, number=1):
    """
    take
    """
    return array[0:number]


def take_right(array, number=1):
    """
    take_right
    """
    length = len(array)
    start = length - number if length - number >= 0 else 0
    return array[start:length]


def take_right_while(array, callback):
    """
    take_right_while
    """
    temp_array = copy.deepcopy(array)
    temp_array.reverse()
    for item in temp_array:
        flag = callback(item)
        if not flag:
            array.remove(item)


def take_while(array, callback):
    """
    take_while
    """
    temp_array = copy.deepcopy(array)
    for item in temp_array:
        flag = callback(item)
        if not flag:
            array.remove(item)


def union(*args):
    """
    union
    """
    arrays = list(args)
    new_array = []
    for array in arrays:
        for item in array:
            if item not in new_array:
                new_array.append(item)
    return new_array


def uniq(array):
    """
    uniq
    """
    return list(set(array))


def unzip(arrays):
    """
    unzip
    """
    total_items_per_array = len(arrays)
    total_arrays = 0
    for array in arrays:
        if total_arrays < len(array):
            total_arrays = len(array)
    new_array = []
    for idx1 in range(0, total_arrays):
        new_array.append([])
        for idx2 in range(0, total_items_per_array):
            value = arrays[idx2][idx1]
            new_array[idx1].append(value)
    return new_array


def unzip_with(arrays, callback):
    """
    unzip_with
    """
    unzipped = unzip(arrays)
    new_array = []
    for array in unzipped:
        value = callback(*array)
        new_array.append(value)
    return new_array


def without(array, *args):
    """
    without
    """
    values = list(args)
    new_array = []
    for item in array:
        if item not in values:
            new_array.append(item)
    return new_array


def xor(*args):
    """
    xor
    """
    arrays = list(args)
    flatten_array = flatten_deep(arrays)
    item_count = {}
    for item in flatten_array:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    array = []
    for key, value in item_count.items():
        if value == 1:
            array.append(key)
    return array


def zip(*args):
    """
    zip
    """
    arrays = list(args)
    maximum = 0
    for array in arrays:
        if maximum < len(array):
            maximum = len(array)
    new_arrays = []

    def get_item(array, i):
        try:
            return array[i]
        except:
            return None
    for i in range(0, maximum):
        new_array = []
        for array in arrays:
            item = get_item(array, i)
            new_array.append(item)
        new_arrays.append(new_array)
    return new_arrays


def zip_object(props, values):
    """
    zip_object
    """
    obj = {}
    for index, prop in enumerate(props):
        value = None
        if index < len(values):
            value = values[index]
        obj[prop] = value
    return obj

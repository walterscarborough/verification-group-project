__author__ = 'AWood'

def quick_sort_wrapper(x, y, z):

    array_in = [x, y, z]

    array_in = quick_sort(array_in)

    return tuple(array_in)

def expected_result():
    return [
        (0, 1, 2),
        (0, 2, 8),
        (0, 2, 8),
        (0, 0, 0),
        (0, 0, 2),
        (2, 8, 9)
    ]

def quick_sort(array_in):
    # If array is None (null), return None (null)
    if array_in is None:
        return None

    # If array size is 0 or 1, it is already sorted
    if len(array_in) < 2:
        return array_in

    max_index = len(array_in) - 1
    index = partition(array_in, 0, max_index)
    lesser = quick_sort(array_in[0:index + 1])
    greater = quick_sort(array_in[index + 1:max_index + 1])
    return lesser + greater


# Sorting step
def partition(array_in, min_index, max_index):
    pivot_index = choose_pivot(array_in, min_index, max_index)
    pivot_value = array_in[pivot_index]
    swap(array_in, pivot_index, max_index)
    return_index = min_index
    for i in range(min_index, max_index):
        if array_in[i] < pivot_value:
            swap(array_in, i, return_index)
            return_index += 1
    swap(array_in, return_index, max_index)
    return return_index


# Arbitrarily use middle element as pivot
def choose_pivot(array_in, min_index, max_index):
    return int((max_index - min_index) / 2)


# Swaps elements in an array at index 'a' and 'b'
def swap(array_in, a, b):
    temp = array_in[a]
    array_in[a] = array_in[b]
    array_in[b] = temp

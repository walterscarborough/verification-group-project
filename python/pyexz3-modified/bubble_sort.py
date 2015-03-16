__author__ = 'AWood'

def bubble_sort(x, y, z):

    # Walter Note:
    # pyexz3 can work on integers, but not on an entire array
    # workaround: just construct the array now
    array_in = [x, y, z]

    # If array is None (null), return None (null)
    if array_in is None:
        return None

    # If array size is 0 or 1, it is already sorted
    if len(array_in) < 2:
        return array_in

    # Begin outer loop
    for i in range(len(array_in)):
        for j in range(0, len(array_in) - (i + 1)):
            if array_in[j] > array_in[j+1]:
                temp = array_in[j+1]
                array_in[j+1] = array_in[j]
                array_in[j] = temp

    # Walter Note:
    # pyexz3 will throw an 'unhashable list' error if we return an array.
    # workaround: return a tuple instead
    return tuple(array_in)

def expected_result():
    return [
        (0, 2, 9),
        (0, 0, 2),
        (0, 1, 2),
        (0, 2, 8),
        (0, 0, 0),
        (2, 8, 9),
    ]

#if __name__ == "__main__":
#    import sys
#    bubble_sort(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

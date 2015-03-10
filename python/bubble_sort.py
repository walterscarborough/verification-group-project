__author__ = 'AWood'


def bubble_sort(array_in):
    # If array is None (null) or size == 0
    if not array_in:
        return None
    # If array size is 1, it is already sorted
    if len(array_in) == 1:
        return input

    array_out = array_in

    # Begin outer loop
    for i in range(len(array_in)):
        for j in range(0, len(array_in) - (i + 1)):
            if array_out[j] > array_out[j+1]:
                temp = array_out[j+1]
                array_out[j+1] = array_out[j]
                array_out[j] = temp

    return array_out
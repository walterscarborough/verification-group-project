__author__ = 'AWood'


def merge_sort(array_in):
    # If array is None (null), return None (null)
    if array_in is None:
        return None

    # If array size is 0 or 1, it is already sorted
    if len(array_in) < 2:
        return array_in

    # Divide and conquer
    index = int(len(array_in) / 2)
    a = merge_sort(array_in[0:index])
    b = merge_sort(array_in[index:len(array_in)])

    # Needed variables
    a_index = 0
    b_index = 0
    out_index = 0
    array_out = [0]*(len(a)+len(b))

    # Sorting logic for ascending sort
    while a_index < len(a) and b_index < len(b):
        if a[a_index] > b[b_index]:
            array_out[out_index] = b[b_index]
            b_index += 1
        else:
            array_out[out_index] = a[a_index]
            a_index += 1
        out_index += 1

    # Add remaining elements to end of array
    if a_index < b_index:
        array_out[out_index:len(array_out)] = a[a_index:len(a)]
    else:
        array_out[out_index:len(array_out)] = b[b_index:len(b)]

    return array_out
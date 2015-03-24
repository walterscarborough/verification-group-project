__author__ = 'AWood'

def bubble_sort_wrapper(x, y, z):

    array_in = [x, y, z]

    array_in = bubble_sort(array_in)

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

def bubble_sort(array_in):
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

    return array_in

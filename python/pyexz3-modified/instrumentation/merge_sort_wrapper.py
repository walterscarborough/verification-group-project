__author__ = 'AWood'

from instrumentation import Instrumentation

root_node = Instrumentation()
root_node.node_name = "C0"

current_node = Instrumentation()
current_node = root_node

def merge_sort_wrapper(x, y, z):
    global root_node

    array_in = [x, y, z]

    array_in = merge_sort(array_in)

    root_node.print_connected_nodes()

    return tuple(array_in)

def expected_result():
    return [
        (0, 1, 8),
        (0, 0, 2),
        (0, 1, 2),
        (0, 0, 1),
        (0, 2, 3),
        (0, 0, 0)
    ]

def merge_sort(array_in):

    global current_node

    # If array is None (null), return None (null)
    if array_in is None:
        array_in_node = Instrumentation()
        array_in_node.node_name = "C1"
        current_node.next_node = array_in_node
        current_node = array_in_node

        return None

    # If array size is 0 or 1, it is already sorted
    if len(array_in) < 2:
        array_in_node = Instrumentation()
        array_in_node.node_name = "C2"
        current_node.next_node = array_in_node
        current_node = array_in_node

        return array_in

    array_2_in_node = Instrumentation()
    array_2_in_node.node_name = "C3"
    current_node.next_node = array_2_in_node
    current_node = array_2_in_node

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

            array_in_node = Instrumentation()
            array_in_node.node_name = "C4"
            current_node.next_node = array_in_node
            current_node = array_in_node

            array_out[out_index] = b[b_index]
            b_index += 1
        else:
            array_in_node = Instrumentation()
            array_in_node.node_name = "C5"
            current_node.next_node = array_in_node
            current_node = array_in_node

            array_out[out_index] = a[a_index]
            a_index += 1
        out_index += 1

    # Add remaining elements to end of array
    if a_index < b_index:
        array_out[out_index:len(array_out)] = a[a_index:len(a)]

        array_in_node = Instrumentation()
        array_in_node.node_name = "C6"
        current_node.next_node = array_in_node
        current_node = array_in_node
    else:
        array_out[out_index:len(array_out)] = b[b_index:len(b)]

        array_in_node = Instrumentation()
        array_in_node.node_name = "C7"
        current_node.next_node = array_in_node
        current_node = array_in_node

    array_in_node = Instrumentation()
    array_in_node.node_name = "C8"
    current_node.next_node = array_in_node
    current_node = array_in_node

    return array_out

__author__ = 'AWood'

from instrumentation import Instrumentation

root_node = Instrumentation()
root_node.node_name = "C0"

current_node = Instrumentation()
current_node = root_node

def quick_sort_wrapper(x, y, z):
    global root_node

    array_in = [x, y, z]

    array_in = quick_sort(array_in)

    root_node.print_connected_nodes()

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

    array_in_node = Instrumentation()
    array_in_node.node_name = "C3"
    current_node.next_node = array_in_node
    current_node = array_in_node

    max_index = len(array_in) - 1
    index = partition(array_in, 0, max_index)
    lesser = quick_sort(array_in[0:index + 1])
    greater = quick_sort(array_in[index + 1:max_index + 1])

    array_in_1_node = Instrumentation()
    array_in_1_node.node_name = "C4"
    current_node.next_node = array_in_1_node
    current_node = array_in_1_node

    return lesser + greater


# Sorting step
def partition(array_in, min_index, max_index):
    global current_node

    pivot_index = choose_pivot(array_in, min_index, max_index)
    pivot_value = array_in[pivot_index]
    swap(array_in, pivot_index, max_index)
    return_index = min_index
    for i in range(min_index, max_index):
        if array_in[i] < pivot_value:
            swap(array_in, i, return_index)
            return_index += 1

            array_in_node_1 = Instrumentation()
            array_in_node_1.node_name = "C5"
            current_node.next_node = array_in_node_1
            current_node = array_in_node_1

        else:
            array_in_node_2 = Instrumentation()
            array_in_node_2.node_name = "C6"
            current_node.next_node = array_in_node_2
            current_node = array_in_node_2


    swap(array_in, return_index, max_index)

    array_in_node_3 = Instrumentation()
    array_in_node_3.node_name = "C8"
    current_node.next_node = array_in_node_3
    current_node = array_in_node_3

    return return_index


# Arbitrarily use middle element as pivot
def choose_pivot(array_in, min_index, max_index):
    return int((max_index - min_index) / 2)


# Swaps elements in an array at index 'a' and 'b'
def swap(array_in, a, b):
    temp = array_in[a]
    array_in[a] = array_in[b]
    array_in[b] = temp

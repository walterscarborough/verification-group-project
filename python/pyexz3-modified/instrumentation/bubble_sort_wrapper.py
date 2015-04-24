__author__ = 'AWood'

from instrumentation import Instrumentation

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

    root_node = Instrumentation()
    current_node = root_node

    root_node.node_name = "C0"


    # If array is None (null), return None (null)
    if array_in is None:
        array_in_3_node = Instrumentation()
        array_in_3_node.node_name = "C1"
        current_node.next_node = array_in_3_node
        current_node = array_in_3_node

        return None

    # If array size is 0 or 1, it is already sorted
    if len(array_in) < 2:
        array_in_3_node = Instrumentation()
        array_in_3_node.node_name = "C2"
        current_node.next_node = array_in_3_node
        current_node = array_in_3_node

        return array_in

    array_in_2_node = Instrumentation()
    array_in_2_node.node_name = "C3"
    current_node.next_node = array_in_2_node
    current_node = array_in_2_node
    

    # Begin outer loop
    for i in range(len(array_in)):
        for j in range(0, len(array_in) - (i + 1)):
            if array_in[j] > array_in[j+1]:
                temp = array_in[j+1]
                array_in[j+1] = array_in[j]
                array_in[j] = temp

                array_in_1_node = Instrumentation()
                array_in_1_node.node_name = "C4"
                current_node.next_node = array_in_1_node
                current_node = array_in_1_node

            else:
                array_in_12_node = Instrumentation()
                array_in_12_node.node_name = "C5"
                current_node.next_node = array_in_12_node
                current_node = array_in_12_node

    array_in_node = Instrumentation()
    array_in_node.node_name = "C6"
    current_node.next_node = array_in_node
    current_node = array_in_node

    root_node.print_connected_nodes()

    return array_in

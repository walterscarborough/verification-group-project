__author__ = 'AWood'

def bubble_sort_instrumentation(x, y, z):

    print('top | x=', x, ' y=', y, ' z=', z)
    array_in = [x, y, z]


    array_in = bubble_sort(array_in)

    return tuple(array_in)

#def expected_result():
#    return [
#        (0, 2, 9),
#        (0, 0, 2),
#        (0, 1, 2),
#        (0, 2, 8),
#        (0, 0, 0),
#        (2, 8, 9),
#    ]

def bubble_sort(array_in):

    paths = list()

    instrumentation_root = 'root | array_in=' + str(array_in)

    # If array is None (null), return None (null)
    instrumentation_path_1_condition = str(array_in) + ' =? None'
    paths.append((instrumentation_root, instrumentation_path_1_condition))

    if array_in is None:
        instrumentation_path_1_end = str(array_in) + ' == None\n END. Sorted = None'

        paths.append((instrumentation_path_1_condition, instrumentation_path_1_end))

        return None

    instrumentation_path_1_continue = str(array_in) + ' != None '

    paths.append((instrumentation_path_1_condition, instrumentation_path_1_continue))

    instrumentation_path_2_condition = 'len(' + str(array_in) + ') >? 2'
    paths.append((instrumentation_path_1_continue, instrumentation_path_2_condition))

    # If array size is 0 or 1, it is already sorted
    if len(array_in) < 2:
        instrumentation_path_2_end = 'len(' + str(array_in) + ') <= 2\n END. Sorted = ' + str(array_in)

        paths.append((instrumentation_path_2_condition, instrumentation_path_2_end))

        return array_in

    instrumentation_path_2_continue = 'len(' + str(array_in) + ') > 2'

    paths.append((instrumentation_path_2_condition, instrumentation_path_2_continue))

    # Begin outer loop
    for i in range(len(array_in)):
        for j in range(0, len(array_in) - (i + 1)):
            instrumentation_path_3_condition = str(array_in[j]) + ' >? ' + str(array_in[j+1])

            paths.append((instrumentation_path_2_continue, instrumentation_path_3_condition))

            if array_in[j] > array_in[j+1]:
                instrumentation_path_3_continue = str(array_in[j]) + ' > ' + str(array_in[j+1])

                instrumentation_path_3_continue += '\n'  + 'swap ' + str(array_in[j]) + ' with ' + str(array_in[j+1])

                temp = array_in[j+1]
                array_in[j+1] = array_in[j]
                array_in[j] = temp

                instrumentation_path_3_continue += '\n' + ' array_in=' + str(array_in)

                paths.append((instrumentation_path_3_condition, instrumentation_path_3_continue))
            else:
                instrumentation_path_3_end = str(array_in[j]) + ' <= ' + str(array_in[j+1]) + '\nNo op'
                paths.append((instrumentation_path_3_condition, instrumentation_path_3_end))



    print('digraph G{')
    for pair in paths:
        print('"', pair[0], '" -> "', pair[1], '"')

    print('}')
    #print('finish | x=', array_in[0], ' y=', array_in[1], ' z=', array_in[2])

    return array_in

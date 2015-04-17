__author__ = 'AWood'


def swap(array, ind1, ind2):
    temp = array[:]
    temp[ind1] = array[ind2]
    temp[ind2] = array[ind1]
    return temp

original = ['A0', 'A1', 'A2']

# (Path, Action, Array)
root = ('A != None, len(A) > 2', 'A0 >? A1', original)
node_counter = 1

branches = list()
edges = list()
branches.append(list())
branches[0].append(root)

# Comparison points
for i in range(1, 3):
    branches.append(list())
    for branch in branches[i-1]:
        path, action, arry = branch
        lt_arry = arry[:]
        gt_arry = swap(arry, (i - 1) % 2, ((i - 1) % 2) + 1)
        if path != '':
            lt_path = '%s, %s' % (path, action.replace('>?', '<='))
            gt_path = '%s, %s' % (path, action.replace('?', ''))
        else:
            lt_path = action.replace('>?', '<=')
            gt_path = action.replace('?', '')
        lt_action = '%s >? %s' % (lt_arry[len(arry) - (i+1)], lt_arry[len(arry) - i])
        gt_action = '%s >? %s' % (gt_arry[len(arry) - (i+1)], gt_arry[len(arry) - i])
        branches[i].append((gt_path, gt_action, gt_arry))
        edges.append((branch, (gt_path, gt_action, gt_arry)))
        branches[i].append((lt_path, lt_action, lt_arry))
        edges.append((branch, (lt_path, lt_action, lt_arry)))

# Leaf Nodes
for branch in branches[2]:
    path, action, arry = branch
    lt_arry = arry[:]
    gt_arry = swap(arry, (i - 1) % 2, ((i - 1) % 2) + 1)
    if path != '':
        lt_path = '%s, %s' % (path, action.replace('>?', '<='))
        gt_path = '%s, %s' % (path, action.replace('?', ''))
    else:
        lt_path = action.replace('>?', '<=')
        gt_path = action.replace('?', '')
    lt_action = 'END. Sorted = %s' % lt_arry
    gt_action = 'END. Sorted = %s' % gt_arry
    edges.append((branch, (lt_path, lt_action.replace("'",''), lt_arry)))
    edges.append((branch, (gt_path, gt_action.replace("'",''), gt_arry)))

# Output File
fout = open('..\\utils\\bs_depth_3.dot', 'w')

# Preamble (easy steps)
fout.write('digraph G{\n')
fout.write('\t"Let A = Input Array\\nA0, A1, A2 = A[0], A[1], A[2]" -> "A =? None";\n')
fout.write('\t"A =? None" -> "Path[A == None]\\nEND. Sorted = None";\n')
fout.write('\t"A =? None" -> "Path[A != None]\\nlen(A) >? 2";\n')
fout.write('\t"Path[A != None]\\nlen(A) >? 2" -> "Path[A != None, len(A) <= 2]\\nEND. Sorted = A"\n')
fout.write('\t"Path[A != None]\\nlen(A) >? 2" -> "Path[A != None, len(A) > 2]\\nA0 >? A1"\n')

# Main branches with edges
for source, target in edges:
    src_string = '"Path[%s]\\n%s"' % (source[0], source[1])
    tgt_string = '"Path[%s]\\n%s"' % (target[0], target[1])
    fout.write('\t%s -> %s\n' % (src_string, tgt_string))
fout.write('}')

# Close file
fout.close()
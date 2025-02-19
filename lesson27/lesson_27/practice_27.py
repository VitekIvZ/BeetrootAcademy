

#      R
#    / | \
#   N  N  N
#  /  / \  \
# L  L   L  L

# height, depth
#      

my_tree = [
    'a', 
        ['b', 
            ['d', [], []],
            ['f', [], []]
         ],
        ['c', 
            ['g', [], []],
            ['h', [], []]
         ]
]

#  [ ['a', 'b', 'd'], ['a', 'b', 'f'], ['a', 'c', 'g'], ['a', 'c', 'h'] ]


def binaryTree(r):
    return [r, [], []]


def insert_left(tree, value):
    tr = tree.pop(1)
    if len(tr) > 1:
        tree.insert(1, [value, tr, []])
    else:
        tree.insert(1, [value, [], []])


def insert_right(tree, value):
    tr = tree.pop(2)
    if len(tr) > 1:
        tree.insert(2, [value, [], tr])
    else:
        tree.insert(2, [value, [], []])


# def delete_left(tree):
#     left = tree[1]
#     child_left, child_right = left[1], left[2]


def print_tree(tree, indent=0, symbol=' '):
    if len(tree) > 1:
        print(f"{symbol*indent}{tree[0]}")
    if len(tree) == 3:
        print_tree(tree[1], indent=indent+4)
        print_tree(tree[2], indent=indent+4)


def get_paths(tree, paths, curr_path):
    curr_path.append(tree[0])
    if not tree[1] and not tree[2]:
        paths.append(curr_path)
    else:
        if tree[1]:
            get_paths(tree[1], paths, curr_path.copy())
        if tree[2]:
            get_paths(tree[2], paths, curr_path.copy())

    # if tree[1]:
    #     get_paths(tree[1], paths, curr_path=curr_path.copy())
    # else:
    #     paths.append(curr_path)
    # if tree[2]:
    #     get_paths(tree[2], paths, curr_path=curr_path.copy())
    # else:
    #     paths.append(curr_path)
    # paths.append(curr_path)
    # else:
    #     paths.append(curr_path)

    return paths



if __name__ == '__main__':
    # print_tree(my_tree)
    tr = binaryTree('a')
    insert_left(tr, 'd')
    insert_right(tr, 'h')
    print_tree(tr)

    insert_left(tr, 'b')
    insert_right(tr, 'c')
    insert_right(tr[1], 'f')
    insert_left(tr[2], 'g')
    
    # insert_right(tree, value)

    print_tree(tr)

    paths = get_paths(tr, [], [])
    print(paths)
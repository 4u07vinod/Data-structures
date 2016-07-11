def binary_tree(root):
    return [root, [], []]

def insert_left(root, newbranch):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [],[]])
    return root

def insert_right(root, newbranch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(2, [newbranch, [], t])
    else:
        root.insert(2, [newbranch, [], []])
    return root

def get_root_value(root):
    return root[0]

def set_root_value(root, newvalue):
    root[0]=newvalue

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

if __name__ == '__main__':
    t=binary_tree(1)
    print insert_left(t, 2)
    v= insert_right(t, 3)
    for i in range(3):
        root = get_left_child(t)
        if root is None:
            break
        print root
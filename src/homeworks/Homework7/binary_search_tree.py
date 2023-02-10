class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def insert(rt, val):
    if rt is None:
        return Node(val)
    else:
        if rt.key <= val:
            rt.right = insert(rt.right, val)
        else:
            rt.left = insert(rt.left, val)
        return rt


def print_preorder(rt: Node):
    if rt:
        print_preorder(rt.left)
        print(rt.key)
        print_preorder(rt.right)


def minimum(rt: Node):
    p = rt
    while p.left:
        p = p.left
    return p


def delete(rt: Node, value):
    if rt is None:
        return rt
    elif value < rt.key:
        rt.left = delete(rt.left, value)
    elif value > rt.key:
        rt.right = delete(rt.right, value)
    else:
        if rt.left is None and rt.right is None:
            del rt
            rt = None
        elif rt.left is None:
            tmp = rt
            rt = rt.right
            del tmp
        elif rt.right is None:
            tmp = rt
            rt = rt.left
            del tmp
        else:
            tmp = minimum(rt.right)
            rt.key = tmp.key
            rt.right = delete(rt.right, tmp.key)
    return rt


def search(rt: Node, value):
    if rt is None or value == rt.key:
        return rt
    if value < rt.key:
        return search(rt.left, value)
    else:
        return search(rt.right, value)


def for_search(rt: Node, value):
    if search(rt, value):
        return True
    return False


root = Node(10)
insert(root, 2)
insert(root, 0)
insert(root, 60)
print_preorder(root)
print("------------------------------")
delete(root, 10)
print_preorder(root)
print("------------------------------")
print(for_search(root, 2))
print(for_search(root, 10))

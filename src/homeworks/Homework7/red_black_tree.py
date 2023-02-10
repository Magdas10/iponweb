
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree:
    def __init__(self):
        self.as_root = Node(0)
        self.as_root.color = 0
        self.as_root.left = None
        self.as_root.right = None
        self.root = self.as_root

    def for_search(self, rt, value):
        if rt == self.as_root or value == rt.value:
            return rt

        if value < rt.value:
            return self.for_search(rt.left, value)
        return self.for_search(rt.right, value)

    def left_rotate(self, rt1):
        rt2 = rt1.right
        rt1.right = rt2.left
        if rt2.left != self.as_root:
            rt2.left.parent = rt1

        rt2.parent = rt1.parent
        if rt1.parent is None:
            self.root = rt2
        elif rt1 == rt1.parent.left:
            rt1.parent.left = rt2
        else:
            rt1.parent.right = rt2
        rt2.left = rt1
        rt1.parent = rt2

    def right_rotate(self, rt1):
        rt2 = rt1.left
        rt1.left = rt2.right
        if rt2.right != self.as_root:
            rt2.right.parent = rt1

        rt2.parent = rt1.parent
        if rt1.parent is None:
            self.root = rt2
        elif rt1 == rt1.parent.right:
            rt1.parent.right = rt2
        else:
            rt1.parent.left = rt2
        rt2.right = rt1
        rt1.parent = rt2

    def fix_after_insert(self, rt1):
        while rt1.parent.color == 1:
            if rt1.parent == rt1.parent.parent.right:
                rt2 = rt1.parent.parent.left
                if rt2.color == 1:
                    rt2.color = 0
                    rt1.parent.color = 0
                    rt1.parent.parent.color = 1
                    rt1 = rt1.parent.parent
                else:
                    if rt1 == rt1.parent.left:
                        rt1 = rt1.parent
                        self.right_rotate(rt1)
                    rt1.parent.color = 0
                    rt1.parent.parent.color = 1
                    self.left_rotate(rt1.parent.parent)
            else:
                rt2 = rt1.parent.parent.right

                if rt2.color == 1:
                    rt2.color = 0
                    rt1.parent.color = 0
                    rt1.parent.parent.color = 1
                    rt1 = rt1.parent.parent
                else:
                    if rt1 == rt1.parent.right:
                        rt1 = rt1.parent
                        self.left_rotate(rt1)
                    rt1.parent.color = 0
                    rt1.parent.parent.color = 1
                    self.right_rotate(rt1.parent.parent)
            if rt1 == self.root:
                break
        self.root.color = 0

    def insert(self, value):
        rt = Node(value)
        rt.parent = None
        rt.value = value
        rt.left = self.as_root
        rt.right = self.as_root
        rt.color = 1

        y = None
        x = self.root

        while x != self.as_root:
            y = x
            if rt.value < x.value:
                x = x.left
            else:
                x = x.right

        rt.parent = y
        if y is None:
            self.root = rt
        elif rt.value < y.value:
            y.left = rt
        else:
            y.right = rt

        if rt.parent is None:
            rt.color = 0
            return

        if rt.parent.parent is None:
            return

        self.fix_after_insert(rt)

    def fix_after_delete(self, rt):
        while rt != self.root and rt.color == 0:
            if rt == rt.parent.left:
                rt1 = rt.parent.right
                if rt1.color == 1:
                    rt1.color = 0
                    rt.parent.color = 1
                    self.left_rotate(rt.parent)
                    rt1 = rt.parent.right

                if rt1.left.color == 0 and rt1.right.color == 0:
                    rt1.color = 1
                    rt = rt.parent
                else:
                    if rt1.right.color == 0:
                        rt1.left.color = 0
                        rt1.color = 1
                        self.right_rotate(rt1)
                        rt1 = rt.parent.right

                    rt1.color = rt.parent.color
                    rt.parent.color = 0
                    rt1.right.color = 0
                    self.left_rotate(rt.parent)
                    rt = self.root
            else:
                rt1 = rt.parent.left
                if rt1.color == 1:
                    rt1.color = 0
                    rt.parent.color = 1
                    self.right_rotate(rt.parent)
                    rt1 = rt.parent.left

                if rt1.right.color == 0 and rt1.right.color == 0:
                    rt1.color = 1
                    rt = rt.parent
                else:
                    if rt1.left.color == 0:
                        rt1.right.color = 0
                        rt1.color = 1
                        self.left_rotate(rt1)
                        rt1 = rt.parent.left

                    rt1.color = rt.parent.color
                    rt.parent.color = 0
                    rt1.left.color = 0
                    self.right_rotate(rt.parent)
                    rt = self.root
        rt.color = 0

    def __transplant_tree(self, rt1, rt2):
        if rt1.parent is None:
            self.root = rt2
        elif rt1 == rt1.parent.left:
            rt1.parent.left = rt2
        else:
            rt1.parent.right = rt2
        rt2.parent = rt1.parent

    def minimum(self, rt):
        while rt.left != self.as_root:
            rt = rt.left
        return rt

    def for_delete(self, rt, value):
        as_root1 = self.as_root
        while rt != self.as_root:
            if rt.value == value:
                as_root1 = rt

            if rt.value <= value:
                rt = rt.right
            else:
                rt = rt.left

        if as_root1 == self.as_root:
            return "no such value"

        y = as_root1
        y_original_color = y.color
        if as_root1.left == self.as_root:
            x = as_root1.right
            self.__transplant_tree(as_root1, as_root1.right)
        elif as_root1.right == self.as_root:
            x = as_root1.left
            self.__transplant_tree(as_root1, as_root1.left)
        else:
            y = self.minimum(as_root1.right)
            y_original_color = y.color
            x = y.right
            if y.parent == as_root1:
                x.parent = y
            else:
                self.__transplant_tree(y, y.right)
                y.right = as_root1.right
                y.right.parent = y

            self.__transplant_tree(as_root1, y)
            y.left = as_root1.left
            y.left.parent = y
            y.color = as_root1.color
        if y_original_color == 0:
            self.fix_after_delete(x)

    def delete(self, item):
        self.for_delete(self.root, item)

    def search(self, value):
        return self.for_search(self.root, value)

    def __for_tree(self, node, indent, last):
        if node != self.as_root:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.value) + "(" + s_color + ")")
            self.__for_tree(node.left, indent, False)
            self.__for_tree(node.right, indent, True)

    def print(self):
        self.__for_tree(self.root, "", True)


bst = RedBlackTree()

bst.insert(5)
bst.insert(13)
bst.insert(8)
bst.print()
print("-------------------------")

bst.insert(60)
bst.insert(7)
bst.insert(77)

bst.print()
print("-------------------------")
bst.delete(8)
bst.print()
print("-------------------------")
bst.delete(5)
bst.print()

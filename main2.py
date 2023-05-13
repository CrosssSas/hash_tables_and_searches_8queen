from random import *


def generator(element_count, min_num, max_num):
    data = []
    for i in range(element_count):
        data.append(randint(min_num, max_num))

    return data


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if node.data > value:
            if node.left:
                return self.find(node.left, node, value)

        if node.data < value:
            if node.right:
                return self.find(node.right, node, value)

        return node, parent, False

    def adder(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, flag_find = self.find(self.root, None, obj.data)

        if not flag_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node, out_flag):
        if node is None:
            return

        if out_flag:
            self.show_tree(node.left, True)
            print(node.data)
            self.show_tree(node.right, True)
        elif not out_flag:
            self.show_tree(node.right, False)
            print(node.data)
            self.show_tree(node.left, False)


# v = [10, 5, 7, 16, 13, 2, 20]

v = generator(50, 1, 100)

t = Tree()
for x in v:
    t.adder(Node(x))

t.show_tree(t.root, True)

n, p, f = t.find(t.root, None, 7)

print(f)
print(n.data)
print(p.data)

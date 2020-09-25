import sys
sys.stdin = open('../input.txt', 'r')
sys.setrecursionlimit(10 ** 4)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            curr_node = self.root
            while True:
                if curr_node.value > value:
                    if not curr_node.left:
                        curr_node.left = Node(value)
                        break
                    else:
                        curr_node = curr_node.left
                if curr_node.value < value:
                    if not curr_node.right:
                        curr_node.right = Node(value)
                        break
                    else:
                        curr_node = curr_node.right


def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    answer.append(node.value)


answer = []
tree = Tree()
while True:
    try:
        value = int(input())
        tree.insert(value)
    except:
        break

postorder(tree.root)

print(' '.join(map(str, answer)))
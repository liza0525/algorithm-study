import sys
sys.stdin = open('../input.txt', 'r')


def preorder(node):
    print(node.value, end='')
    if node.lc != '.':
        preorder(t[node.lc])
    if node.rc != '.':
        preorder(t[node.rc])


def inorder(node):
    if node.lc != '.':
        inorder(t[node.lc])
    print(node.value, end='')
    if node.rc != '.':
        inorder(t[node.rc])


def postorder(node):
    if node.lc != '.':
        postorder(t[node.lc])
    if node.rc != '.':
        postorder(t[node.rc])
    print(node.value, end='')


class Node:
    def __init__(self, value, lc, rc):
        self.value = value
        self.lc = lc
        self.rc = rc


N = int(input())
t = {}
for _ in range(N):
    data = input().split()
    t[data[0]] = Node(value=data[0], lc=data[1], rc=data[2])

preorder(t['A'])
print()
inorder(t['A'])
print()
postorder(t['A'])
print()
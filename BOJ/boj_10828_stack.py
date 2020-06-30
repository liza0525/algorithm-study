import sys
sys.stdin = open('../input.txt', 'r')

class Stack():
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst += [x]

    def pop(self):
        if self.lst:
            print(self.lst.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.lst))

    def empty(self):
        if self.lst:
            print(0)
        else:
            print(1)

    def top(self):
        if self.lst:
            print(self.lst[-1])
        else:
            print(-1)

N = int(input())
stack = Stack()
for _ in range(N):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        stack.push(line[1])
    elif line[0] == 'pop':
        stack.pop()
    elif line[0] == 'size':
        stack.size()
    elif line[0] == 'empty':
        stack.empty()
    elif line[0] == 'top':
        stack.top()
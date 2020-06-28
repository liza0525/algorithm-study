import sys
sys.stdin = open('../input.txt', 'r')

class Deque():
    def __init__(self):
        self.lst = list()

    def push_front(self, x):
        self.lst.insert(0, x)

    def push_back(self, x):
        self.lst.append(x)

    def pop_front(self):
        if self.lst:
            print(self.lst.pop(0))
        else:
            print(-1)

    def pop_back(self):
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

    def front(self):
        if self.lst:
            print(self.lst[0])
        else:
            print(-1)

    def back(self):
        if self.lst:
            print(self.lst[-1])
        else:
            print(-1)


dq = Deque()
N = int(input())
for _ in range(N):
    line = sys.stdin.readline().split()
    if line[0] == 'push_front':
        dq.push_front(line[1])
    elif line[0] == 'push_back':
        dq.push_back(line[1])
    elif line[0] == 'pop_front':
        dq.pop_front()
    elif line[0] == 'pop_back':
        dq.pop_back()
    elif line[0] == 'size':
        dq.size()
    elif line[0] == 'empty':
        dq.empty()
    elif line[0] == 'front':
        dq.front()
    elif line[0] == 'back':
        dq.back()
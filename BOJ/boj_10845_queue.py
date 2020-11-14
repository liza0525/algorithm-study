import sys
sys.stdin = open('../input.txt', 'r')

from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    commands = sys.stdin.readline().rstrip()
    if commands[:4] == 'push':
        command, number = commands.split()
        queue.append(number)
    else:
        if commands == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif commands == 'size':
            print(len(queue))
        elif commands == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif commands == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif commands == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
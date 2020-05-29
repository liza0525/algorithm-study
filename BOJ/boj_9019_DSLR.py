import sys
sys.stdin = open('../input.txt', 'r')

import collections

def D(num):
    return (num * 2) % 10000, 'D'


def S(num):
    return (num - 1, 'S') if num != 0 else (9999, 'S')


def L(num):
    str_num = str(num)
    return int(str_num[1:] + str_num[0]), 'L'


def R(num):
    str_num = str(num)
    return int(str_num[-1] + str_num[:-1]), 'R'


def bfs(num):
    queue = collections.deque()
    queue.append(num)
    visited = [[0, ''] for _ in range(10000)]
    visited[num][0] = -1
    while queue:
        snum = queue.popleft()
        for nnum, char in [D(snum), S(snum), L(snum), R(snum)]:
            if not visited[nnum][0]:
                queue.append(nnum)
                visited[nnum][0] = snum
                visited[nnum][1] = char
    return visited

for _ in range(int(input())):
    A, B = map(int, input().split())
    visited = [[0, ''] for _ in range(10000)]

    visited = bfs(A)

    res, num = '', B
    while num != A:
        res += visited[num][1]
        num = visited[num][0]
    print(res[::-1])
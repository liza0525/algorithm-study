import sys
sys.stdin = open('../input.txt', 'r')

import collections

def D(num):
    return (num * 2) // 10000, 'D'


def S(num):
    return num - 1 if num != 0 else 9999, 'S'


def L(num):
    str_num = str(num)
    return int(str_num[1:] + str_num[0]), 'L'


def R(num):
    str_num = str(num)
    return int(str_num[-1] + str_num[:-1]), 'R'


def bfs(num):
    queue = collections.deque()
    queue.append(num)
    res = ''

    while queue:
        snum = queue.popleft()
        for nnum, char in [D(snum), S(snum), L(snum), R(snum)]:
            


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
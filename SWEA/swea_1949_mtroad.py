import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def isField(i, j):
    return 0 <= i < n and 0 <= j < n


def bfs(i, j):
    global max_road
    visited = [(i, j)]
    queue = [(i, j)]
    road = 1

    while queue:
        temp = queue[:]
        queue = []
        
        while temp:
            si, sj = temp.pop(0)
            for di, dj in d:
                if isField(si+di, sj+dj) and g[si+di][sj+dj] < g[si][sj] and (si+di, sj+dj) not in queue:
                    queue.append((si+di, sj+dj))
                    visited.append((si+di, sj+dj))
        if not queue:
            break
        road += 1

    if road > max_road:
        max_road = road


def set_start(g, peek):
    for i in range(n):
        for j in range(n):
            if g[i][j] == peek:
                bfs(i, j)


for test in range(int(input())):
    n, k = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    max_road = 0
    peek = 0

    for i in range(n):
        for j in range(n):
            if g[i][j] > peek:
                peek = g[i][j]


    for kk in range(k+1):
        for i in range(n):
            for j in range(n):
                g[i][j] -= kk
                set_start(g, peek)
                g[i][j] += kk

    print('#{} {}'.format(test+1, max_road))
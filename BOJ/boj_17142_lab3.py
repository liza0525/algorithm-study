from pprint import pprint
import sys
sys.stdin = open('../input.txt', 'r')


import itertools
import collections


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(case):
    global min_dist
    dist = [[-1] * N for _ in range(N)]
    queue = collections.deque()
    for i, j in case:
        dist[i][j] = 0
        queue.append((i, j))
    res_dist = 0
    while queue:
        si, sj = queue.popleft()
        for di, dj in ds:
            ni, nj = si+di, sj+dj
            if not(0 <= ni < N and 0 <= nj < N): continue
            if dist[ni][nj] == -1 and g[ni][nj] != 1:
                dist[ni][nj] = dist[si][sj] + 1
                queue.append((ni, nj))
                if g[ni][nj] == 2:
                    case.append((si, sj))
                else:
                    res_dist = dist[ni][nj]


    for num in range(N*N):
        row, col = num // N, num % N
        if g[row][col] != 1 and dist[row][col] == -1:
            break
    else:
        if res_dist < min_dist:
            min_dist = res_dist

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
virus, min_dist = [], 1e9

for i in range(N):
    for j in range(N):
        if g[i][j] == 2:
            virus.append((i, j))

for case in map(list, itertools.combinations(virus, M)):
    bfs(case)

print(min_dist if min_dist != 1e9 else -1)
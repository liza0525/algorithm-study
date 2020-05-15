import sys
sys.stdin = open('../input.txt', 'r')
from itertools import combinations
from collections import deque


ds = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs():
    flower = 0
    g1 = [[0] * M for _ in range(N)]
    for i in range(N*M):
        row, col = i // M, i % M
        g1[row][col] = g[row][col]
    visited = [[0] * M for _ in range(N)]
    q = deque()
    for idx in r_group:
        i, j = beedable[idx]
        g1[i][j] = 'R'
        visited[i][j] = 1
        q.append((i, j))
    for idx in g_group:
        i, j = beedable[idx]
        g1[i][j] = 'G'
        visited[i][j] = 1
        q.append((i, j))


    while q:
        si, sj = q.popleft()
        for di, dj in ds:
            ni, nj = si+di, sj+dj
            if not (0 <= ni < N and 0 <= nj < M): continue
            if g1[ni][nj] == 'F': continue
            if g1[ni][nj] == 0: continue
            if g1[ni][nj] == g1[si][sj]: continue
            if not visited[ni][nj] or visited[si][sj] + 1 == visited[ni][nj]:
                if g1[si][sj] == 'G':
                    if g1[ni][nj] == 'R':
                        g1[ni][nj] = 'F'
                        flower += 1
                    else:
                        g1[ni][nj] = 'G'
                        q.append((ni, nj))
                        visited[ni][nj] = visited[si][sj] + 1
                elif g1[si][sj] == 'R':
                    if g1[ni][nj] == 'G':
                        g1[ni][nj] = 'F'
                        flower += 1
                    else:
                        g1[ni][nj] = 'R'
                        q.append((ni, nj))
                        visited[ni][nj] = visited[si][sj] + 1
    return flower


N, M, G, R = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
beedable = list()
max_flower = 0

for i in range(N * M):
    row, col = i // M, i % M
    if g[row][col] == 2:
        beedable.append((row, col))

for c1 in combinations(range(len(beedable)), R+G):
    for c2 in combinations(range(R+G), R):
        r_group, g_group = [], []
        for i in range(R+G):
            if i in c2: r_group.append(c1[i])
            else: g_group.append(c1[i])
        max_flower = max(max_flower, bfs())

print(max_flower)
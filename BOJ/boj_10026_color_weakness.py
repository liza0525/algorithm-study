import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')


ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def rgb(i, j):
    global visited
    visited[i][j] = 1
    stack = [(i, j)]

    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N and g[si][sj] == g[ni][nj] and not visited[ni][nj]:
                stack.append((ni, nj))
                visited[ni][nj] = 1
    return 1


def b(i, j):
    global visited
    visited[i][j] = 1
    stack = [(i, j)]

    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N:
                if (g[si][sj] == 'R' and g[ni][nj] == 'G') or (g[si][sj] == 'G' and g[ni][nj] == 'R') or (g[si][sj] == g[ni][nj]):
                    if not visited[ni][nj]:
                        stack.append((ni, nj))
                        visited[ni][nj] = 1
    return 1


N = int(input())
g = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt_rgb, cnt_b = 0, 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt_rgb += rgb(i, j)

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt_b += b(i, j)

print(cnt_rgb, cnt_b)
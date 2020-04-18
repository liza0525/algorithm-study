import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(i, j):
    stack = [(i, j)]

    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ni, nj = si+di, sj+dj
            if 0 <= ni < M and 0 <= nj < N:
                if g[ni][nj] and not visited[ni][nj]:
                    stack.append((ni, nj))
                    visited[ni][nj] = 1
    return 1


T = int(input())

for test in range(T):
    M, N, K = map(int, input().split())
    g = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    res = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        g[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if g[i][j] and not visited[i][j]:
                res += dfs(i, j)

    print(res)
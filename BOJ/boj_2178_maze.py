import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')

ds = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def bfs(i, j):
    global visited
    visited[i][j] = 1
    queue = [(i, j)]

    while queue:
        si, sj = queue.pop()
        for di, dj in ds:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if g[ni][nj] and (not visited[ni][nj] or sc[ni][nj] > sc[si][sj] + 1):
                    sc[ni][nj] = sc[si][sj] + 1
                    visited[ni][nj] = 1
                    queue.append((ni, nj))


N, M = map(int, input().split())
g = [list(map(int, input())) for _ in range(N)]
sc = [[N*M+1]*M for _ in range(N)]
sc[0][0] = 1
visited = [[0]*M for _ in range(N)]

bfs(0, 0)

print(sc[N-1][M-1])
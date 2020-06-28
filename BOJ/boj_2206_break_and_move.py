import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint
from collections import deque

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    dist[i][j][0] = 1
    while queue:
        si, sj = queue.popleft()
        for di, dj in ds:
            ni, nj = si + di, sj + dj
            if not(0 <= ni < N and 0 <= nj < M): continue
            if not g[ni][nj]:
                if not dist[ni][nj][0]:
                    dist[ni][nj][1] = dist[si][sj][1]
                    dist[ni][nj][0] = dist[si][sj][0] + 1
                    queue.append((ni, nj))
                else:
                    if dist[si][sj][0] + 1 < dist[ni][nj][0]:
                        dist[ni][nj][1] = dist[si][sj][1]
                        dist[ni][nj][0] = dist[si][sj][0] + 1
                        queue.append((ni, nj))
                    elif dist[si][sj][0] + 1 == dist[ni][nj][0] and dist[ni][nj][1] != dist[si][sj][1]:
                        dist[ni][nj][1] = 0
                        dist[ni][nj][0] = dist[si][sj][0] + 1
                        queue.append((ni, nj))
            else:
                if not dist[si][sj][1]:
                    dist[ni][nj][0] = dist[si][sj][0] + 1
                    dist[ni][nj][1] = 1
                    queue.append((ni, nj))

N, M = map(int, input().split())
g = [list(map(int, input())) for _ in range(N)]
cand = []
min_dist = 1e9
dist = [[[0, 0] for _ in range(M)] for _ in range(N)] # index 0 : 거리 index 1: 1을 통과했는지

bfs(0, 0)
# for line in dist:
#     print(line)
print(dist[N-1][M-1][0] if dist[N-1][M-1][0] != 0 else -1)
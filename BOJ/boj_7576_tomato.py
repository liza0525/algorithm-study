import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(tomatos):
    queue = tomatos[:]
    days = -1

    while queue:
        temp = queue[:]
        queue = []
        for si, sj in temp:
            for di, dj in ds:
                ni, nj = si+di, sj+dj
                if 0 <= ni < M and 0 <= nj < N and g[ni][nj] == 0:
                    queue.append((ni, nj))
                    g[ni][nj] = 1
        days += 1

    return days

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(M)]
tomatos = []

for num in range(N*M):
    i, j = num // N, num % N
    if g[i][j] == 1:
        tomatos.append((i, j))
days = bfs(tomatos)

# pprint(g)
# print(visited)

if 0 in sum(g, []):
    days = -1

print(days)
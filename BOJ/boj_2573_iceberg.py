import sys
sys.stdin = open('../input.txt', 'r')

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(i, j):
    stack = [(i, j)]
    visited[i][j] = 1

    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ni, nj = si+di, sj+dj
            if not (0 <= ni < N and 0 <= nj < M): continue
            if g[ni][nj] and not visited[ni][nj]:
                stack.append((ni, nj))
                visited[ni][nj] = 1
    return 1


def melt_iceberg():
    infos = []
    for i in range(N):
        for j in range(M):
            sea_count = 0
            if g[i][j] == 0:
                continue
            for di, dj in ds:
                ni, nj = i+di, j+dj
                if g[ni][nj] == 0:
                    sea_count += 1
            infos.append((i, j, sea_count))

    for info in infos:
        i, j, sea_count = info
        g[i][j] = 0 if g[i][j] <= sea_count else g[i][j] - sea_count


N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
year = 0

while True:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    melt_iceberg()
    iceberg = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] != 0 and not visited[i][j]:
                iceberg += dfs(i, j)

    year += 1
    if iceberg > 1:
        break
    elif iceberg == 0:
        year = 0
        break

print(year)
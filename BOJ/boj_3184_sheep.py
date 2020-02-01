ds = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def isField(i, j):
    return 0 <= i < N and 0 <= j < M

def dfs(i, j):
    global sheep_t, wolf_t, visited
    sheep, wolf = 0, 0
    visited[i][j] = 1
    stack = [(i, j)]
    while stack:
        si, sj = stack.pop()
        if g[si][sj] == 'v':
            wolf += 1
        elif g[si][sj] == 'o':
            sheep += 1
        for di, dj in ds:
            ni, nj = si + di, sj + dj
            if isField(ni, nj) and g[ni][nj] != '#' and not visited[ni][nj]:
                visited[ni][nj] = 1
                stack.append((ni, nj))
    if sheep > wolf:
        sheep_t += sheep
    else:
        wolf_t += wolf


N, M = map(int, input().split())
g = []
for _ in range(N):
    g.append(list(input()))

visited = [[0] * M for _ in range(N)]
sheep_t, wolf_t = 0, 0

for i in range(N):
    for j in range(M):
        if g[i][j] != '#' and not visited[i][j]:
            dfs(i, j)

print(sheep_t, wolf_t)
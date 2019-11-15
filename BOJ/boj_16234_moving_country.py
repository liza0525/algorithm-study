d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def isField(i, j):
    return 0 <= i < N and 0 <= j < N


def moving(countries, total):
    global notMove, temp

    avg = total // len(countries)
    for i, j in countries:
        temp[i][j] = avg
    notMove = True


def bfs(i, j):
    global visited
    visited = [(i, j)]
    queue = [(i, j)]
    total = g[i][j]
    while queue:
        si, sj = queue.pop(0)
        for di, dj in d:
            ni = si+di
            nj = sj+dj
            if isField(ni, nj) and L <= abs(g[ni][nj] - g[si][sj]) <= R and (ni, nj) not in visited:
                total += g[ni][nj]
                queue.append((ni, nj))
                visited.append((ni, nj))
    if len(visited) != 1:
        moving(visited, total)


N, L, R = map(int, input().split())
g, temp = [], [[0] * N for _ in range(N)]
for _ in range(N):
    g.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        temp[i][j] = g[i][j]

cnt = 0

while True:
    visited = []
    notMove = False
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited:
                bfs(i, j)
    for i in range(N):
        for j in range(N):
            g[i][j] = temp[i][j]
    if not notMove:
        break
    cnt += 1

print(cnt)
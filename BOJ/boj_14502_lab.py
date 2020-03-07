ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def virus(g):
    global min_spread
    stack = []
    spread = 0
    temp = [[0]*M for _ in range(N)]
    for n in range(N*M):
        i, j = n // M, n % M
        temp[i][j] = g[i][j]

    for n in range(N*M):
        i, j = n // M, n % M
        if temp[i][j] == 2:
            stack.append((i, j))

    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M and not temp[ni][nj]:
                stack.append((ni, nj))
                temp[ni][nj] = 2
                spread += 1
                if spread >= min_spread:
                    return
    min_spread = spread

def wall(d, next):
    if d == 3:
        virus(g)
    else:
        for n in range(next, len(space)):
            i, j = space[n]
            if not g[i][j]:
                g[i][j] = 1
                wall(d+1, next+1)
                g[i][j] = 0

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
space = []
empty = sum(g, []).count(0)
min_spread = N * M + 1
for n in range(N*M):
    i, j = n // M, n % M
    if g[i][j] == 0:
        space.append((i, j))

wall(0, 0)

print(empty - min_spread - 3)
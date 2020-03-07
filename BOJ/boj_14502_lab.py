ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def virus(g):
    stack = []
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
    return sum(temp, []).count(0)

def wall(d, next):
    global max_res
    if d == 3:
        res = virus(g)
        if res > max_res:
            max_res = res

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
max_res = 0
for n in range(N*M):
    i, j = n // M, n % M
    if g[i][j] == 0:
        space.append((i, j))

wall(0, 0)

print(max_res)

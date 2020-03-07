ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_field(i, j):
    return 0 <= i < N and 0 <= j < M


def virus(i, j):
    stack =[(i, j)]

    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ni, nj = si + di, sj + dj
            if is_field(ni, nj) and not g[ni][nj]:
                stack.append((ni, nj))
                g[ni][nj] = 2

def wall(cand, d):
    global g, max_res, visited
    if d == 3:
        temp = [[0]*M for _ in range(N)]
        for n in range(N*M):
            i, j = n // M, n % M
            temp[i][j] = g[i][j]

        for i, j in cand:
            g[i][j] = 1

        for n in range(N*M):
            i, j = n // M, n % M
            if g[i][j] == 2:
                virus(i, j)

        res = sum(g, []).count(0)
        if res > max_res:
            max_res = res

        for n in range(N*M):
            i, j = n // M, n % M
            g[i][j] = temp[i][j]
    else:
        for n in range(N*M):
            i, j = n // M, n % M
            if g[i][j] == 0 and (i, j) not in cand:
                cand.append((i, j))
                wall(cand, d+1)
                cand.pop()


N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
max_res = 0
visited = []

wall([], 0)

print(max_res)
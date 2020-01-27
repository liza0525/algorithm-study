ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def isField(i, j):
    return 0 <= i < N and 0 <= j < N

def dfs(i, j):
    stack = [(i, j)]
    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ni = si + di
            nj = sj + dj
            if isField(ni, nj):
                if not visited[ni][nj]:
                    shortcut[ni][nj] = shortcut[si][sj] + g[ni][nj]
                    stack.append((ni, nj))
                    visited[ni][nj] = 1
                else:
                    if shortcut[ni][nj] > shortcut[si][sj] + g[ni][nj]:
                        shortcut[ni][nj] = shortcut[si][sj] + g[ni][nj]
                        stack.append((ni, nj))


for i in range(int(input())):
    N = int(input())
    shortcut = [[90001] * N for _ in range(N)]
    shortcut[0][0] = 0
    visited = [[0] * N for _ in range(N)]
    g = [[int(i) for i in list(input())] for _ in range(N)]
    time_sum = 0
    dfs(0, 0)
    print('#{} {}'.format(i+1, shortcut[N-1][N-1]))

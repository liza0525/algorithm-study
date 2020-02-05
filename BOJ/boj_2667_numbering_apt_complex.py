ds = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def isField(i, j):
    return 0 <= i < N and 0 <= j < N

def dfs(i, j):
    visited[i][j] = 1
    stack = [(i, j)]
    houses = 0
    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ni, nj = si + di, sj + dj
            if isField(ni, nj) and g[ni][nj] and not visited[ni][nj]:
                stack.append((ni, nj))
                visited[ni][nj] = 1
        houses += 1
    return houses


N = int(input())
g = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
complex_num = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and g[i][j]:
            complex_num.append(dfs(i, j))

complex_num.sort()
print(len(complex_num))
for i in range(len(complex_num)):
    print(complex_num[i])
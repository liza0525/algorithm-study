ds = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def isField(i, j):
    return 0 <= i < n and 0 <= j < n

def dfs(si, sj, h):
    global visited
    visited[si][sj] = 1
    stack = [(si, sj)]
    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ni, nj = si + di, sj + dj
            if isField(ni, nj) and g[ni][nj] > h and not visited[ni][nj]:
                visited[ni][nj] = 1
                stack.append((ni, nj))
    return 1

n = int(input())
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

max_h = max(sum(g, []))
max_island = 0

for h in range(0, max_h):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] > h and not visited[i][j]:
                cnt += dfs(i, j, h)
    if cnt > max_island:
        max_island = cnt

print(max_island)
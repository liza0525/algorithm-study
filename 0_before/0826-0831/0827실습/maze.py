dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def isSafe(y,x):
    return 0 <= y < n and 0 <= x < n and (g[y][x] == 0 or g[y][x] == 3)

def dfs(sy, sx):
    global result

    if g[sy][sx] == 3:
        result = 1
        return

    visited.append((sy, sx))
    for dir in range(4):
        nexty = sy + dy[dir]
        nextx = sx + dx[dir]
        if isSafe(nexty, nextx) and (nexty, nextx) not in visited:
            dfs(nexty, nextx)

for test in range(int(input())):
    n = int(input())
    g = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if g[i][j] == 2:
                sx, sy = j,i

    visited = []
    result = 0
    dfs(sy, sx)
    print('#{} {}'.format(test+1, result))

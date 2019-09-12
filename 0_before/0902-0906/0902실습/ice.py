import sys
from pprint import pprint
sys.stdin = open('ice.txt', 'r')

def isField(x, y):
    return 0 <= x < n and 0 <= y < m

def cntZero(x, y):
    amt = 0
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        if isField(x+dx, y+dy) and g[x+dx][y+dy] == 0:
            amt += 1
    return amt

def dfs(x, y):
    global island
    stack = []
    stack.append((x,y))

    while stack:
        x, y = stack.pop()
        if not visit[x][y]:
            visit[x][y] = 1
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if g[x+dx][y+dy] and not visit[x+dx][y+dy] :
                    stack.append((x+dx, y+dy))
    island += 1

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
year = 0

while True:
    visit = [[0] * m for _ in range(n)]
    info = []
    island = 0

    for i in range(n):
        for j in range(m):
            if g[i][j] != 0:
                info.append((i, j, cntZero(i, j)))

    for i, j, amt in info:
        g[i][j] = g[i][j] - amt if g[i][j] > amt else 0

    year += 1

    for i in range(n):
        for j in range(m):
            if g[i][j] and not visit[i][j]:
                dfs(i, j)

    if island >= 2:
        break
    elif island == 0:
        year = 0
        break

print(year)
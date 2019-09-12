import sys
from pprint import pprint
sys.stdin = open('safe_area.txt', 'r')

delta = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def isField(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    stack = []
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        if not visit[x][y]:
            visit[x][y] = 1
            for dx, dy in delta:
                if isField(x+dx, y+dy) and g[x+dx][y+dy] and not visit[x+dx][y+dy]:
                    stack.append((x+dx, y+dy))
    return 1

n = int(input())
tmp = [list(map(int, input().split())) for _ in range(n)]
max_h = max(tmp[0])
for i in range(1, len(tmp)):
    if max(tmp[i]) > max_h:
        max_h = max(tmp[i])
info = [0] * (max_h+1)
h = 0

while h <= max_h:
    g = tmp
    visit = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] <= h:
                g[i][j] = 0

    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] and not visit[i][j]:
                cnt += dfs(i, j)
    info[h] = cnt
    h += 1
print(max(info))
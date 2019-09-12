import sys
from pprint import pprint
sys.stdin = open('treasure_i.txt', 'r')

delta = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def isField(x, y):
    return 0 <= x < col and 0 <= y < row

def bfs(x, y):
    visit = [[0] * row for _ in range(col)]
    queue = []
    queue.append((x, y))
    cnt = -1
    while queue:
        tmp = queue
        for _ in range(len(tmp)):
            x, y = queue.pop(0)
            if not visit[x][y]:
                visit[x][y] = 1
                for dx, dy in delta:
                    if isField(x+dx, y+dy) and g[x+dx][y+dy] == 'L' and not visit[x+dx][y+dy]:
                        queue.append((x+dx, y+dy))
        cnt += 1
    return cnt

col, row = map(int, input().split())
g = [[ch for ch in input()] for _ in range(col)]
info = []

for i in range(col):
    for j in range(row):
        if g[i][j] == 'L':
            info.append(bfs(i, j))

print(max(info))



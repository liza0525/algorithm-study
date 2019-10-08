import sys
from pprint import pprint
sys.stdin = open('sample_input.txt', 'r')

delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

def isField(x, y):
    return 0 <= x < h and 0 <= y < w

def dfs(x, y):
    visited[x][y] = 1

    for dx, dy in delta:
        if isField(x+dx, y+dy) and g[x+dx][y+dy] and not visited[x+dx][y+dy]:
            dfs(x+dx, y+dy)

w, h = 1, 1
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    g = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if g[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
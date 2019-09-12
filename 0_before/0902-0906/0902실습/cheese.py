import sys
from pprint import pprint
sys.stdin = open('cheese.txt', 'r')

def isField(x, y):
    return 0 <= x < row and 0 <= y < col

def air(x, y):
    queue = []
    queue.append((x,y))
    cheese[x][y] = 2

    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if isField(x+dx, y+dy) and cheese[x+dx][y+dy] == 0:
                queue.append((x+dx, y+dy))
                cheese[x+dx][y+dy] = 2

def allmelted(cheese):
    for i in range(row):
        for j in range(col):
            if cheese[i][j] != 2:
                return True
    return False

row, col = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(row)]
hour = 0 # 걸리는 시간

air(0, 0)
while allmelted(cheese):
    edge_i = []
    for i in range(row):
        for j in range(col):
            if cheese[i][j] == 1:
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    if isField(i+dx, j+dy) and cheese[i+dx][j+dy] == 2:
                        edge_i.append((i, j))
                        break

    for i, j in edge_i:
        cheese[i][j] = 2
        air(i, j)
    hour += 1

print(hour)
print(len(edge_i))
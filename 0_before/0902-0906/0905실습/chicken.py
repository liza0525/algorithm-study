import sys
from pprint import pprint
sys.stdin = open('chicken.txt', 'r')

def isField(x, y):
    return 0 <= x < n and 0 <= y < n

def choose(arr, depth, next):
    if depth == m:
        remain.append(arr)
    else:
        for i in range(next, len(chicken)):
            tmp = arr[:]
            tmp.append(chicken[i])
            choose(tmp, depth+1, i+1)

# def bfs(x, y, arr):
#     d = 0
#     visit = [[0] * n for _ in range(n)]
#     queue = []
#     queue.append((x, y))
#     visit[x][y] = 1
#     checker = 0
#     while queue:
#         if checker:
#             break
#         d += 1
#         length = len(queue)
#         for _ in range(length):
#             if checker:
#                 break
#             x, y = queue.pop(0)
#             for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 if isField(x+dx, y+dy) and not visit[x+dx][y+dy]:
#                     queue.append((x+dx, y+dy))
#                     visit[x+dx][y+dy] = 1
#                     if (x+dx, y+dy) in arr:
#                         checker = 1
#                         break
#     return d

def min_distance(x, y, arr):
    tmp = []
    for fx, fy in arr:
        tmp.append(abs(x-fx)+abs(y-fy))
    return min(tmp)


n, m = map(int, input().split())
g = [list(map(int,input().split())) for _ in range(n)]
chicken = []
remain = []
dis_list = []
for i in range(n):
    for j in range(n):
        if g[i][j] == 2:
            chicken.append((i, j))

choose([], 0, 0)
a = 0
while a < len(remain):
    dis = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                dis += min_distance(i, j, remain[a])
    dis_list.append(dis)
    a += 1

print(min(dis_list))

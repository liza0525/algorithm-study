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
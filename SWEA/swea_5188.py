import sys
sys.stdin = open("../inputdata/20190925_addMin.txt", "r")

d = [(1, 0), (0, 1)]

def isField(x, y):
    return 0 <= x < n and 0 <= y < n

def dfsr(x, y):
    global num_sum, res
    visited[x][y] = 1
    num_sum += g[x][y]
    if res < num_sum:
        return
    if x == n-1 and y == n-1:
        res = num_sum
        return
    for dx, dy in d:
        if isField(x+dx, y+dy) and not visited[x+dx][y+dy]:
            dfsr(x+dx, y+dy)
            num_sum -= g[x+dx][y+dy]
            visited[x+dx][y+dy] = 0


for test in range(int(input())):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    num_sum, res = 0, 987654321

    dfsr(0, 0)

    print('#{} {}'.format(test+1, res))

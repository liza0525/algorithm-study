import sys
from pprint import pprint
sys.stdin = open('find_matrix.txt', 'r')


def dfsR(i, j):
    global a, b
    visit[i][j] = 1

    for dx, dy in [(0, 1), (1, 0)]:
        if g[i+dx][j+dy] and not visit[i+dx][j+dy]:
            dfsR(i+dx, j+dy)


def rec(x, y):
    global a, b
    while g[x][y] != 0:
        x += 1
        a += 1
    x -= 1
    while g[x][y] != 0:
        y += 1
        b += 1


for test in range(int(input())):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    cnt = 0; info = []

    for i in range(n):
        for j in range(n):
            if g[i][j] and not visit[i][j]:
                a,b = 0, 0
                dfsR(i, j)
                rec(i, j)
                info.append([a, b]) # a 세로 b 가로
                cnt += 1

    for i in range(len(info)-1):
        for j in range(i+1, len(info)):
            if info[i][0] * info[i][1] > info[j][0] * info[j][1]:
                info[i], info[j] = info[j], info[i]
            elif info[i][0] * info[i][1] == info[j][0] * info[j][1]:
                if info[i][0] > info[j][0]:
                    info[i], info[j] = info[j], info[i]
    tmp = ''
    for i in range(len(info)):
        for j in range(len(info[i])):
            tmp += str(info[i][j])+' '
    print('#{} {} {}'.format(test+1, cnt, tmp))
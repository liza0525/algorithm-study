import sys
from pprint import pprint
sys.stdin = open('new_calc.txt', 'r')

g = [[0] * 300 for _ in range(300)]
n = 1

for i in range(300):
    for j in range(i, -1, -1):
        g[i-j][j] = n
        n += 1

for test in range(int(input())):
    p, q = map(int, input().split())

    for i in range(300):
        for j in range(300):
            if g[i][j] == p:
                px, py = i, j
            if g[i][j] == q:
                qx, qy = i, j

    print('#{} {}'.format(test+1, g[px+qx+1][py+qy+1]))
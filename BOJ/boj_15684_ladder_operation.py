from pprint import pprint
import sys
sys.stdin = open('../input.txt', 'r')


import itertools


def isAnswer(r_g1):
    # print(r_g1)
    # print(not sum(r_g1[0]) % 2)
    # print('='*50)
    for line in r_g1:
        if sum(line) % 2:
            return False
    return True


def make_ladder(case):
    # print(case)
    g1 = [[0] * N for _ in range(H)]
    for idx in range(N*H):
        row, col = idx // N, idx % N
        g1[row][col] = g[row][col]

    for i, j in case:
        if g1[i][j+1] != 1:
            g1[i][j], g1[i][j+1] = 1, 1
        else:
            return False
    # pprint(g1)
    return isAnswer(list(map(list, zip(*g1))))



N, M, H = map(int, input().split())
g = [[0] * N for _ in range(H)]
cand = []
res = 0
for _ in range(M):
    a, b = map(int, input().split())
    g[a-1][b-1], g[a-1][b] = 1, 1

for idx in range(N*H):
    row, col = idx // N, idx % N
    if col+1 < N and not g[row][col] and not g[row][col+1]:
        cand.append((row, col))

for k in range(0, 4):
    flag = 0
    for case in map(list, itertools.combinations(cand, k)):
        if make_ladder(case):
            res = k
            flag = 1
            break
    if flag:
        break
else:
    res = -1

print(res)
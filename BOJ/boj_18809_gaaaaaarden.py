from pprint import pprint
import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('../input.txt', 'r')


ds = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def bfs():
    global max_flower
    flower = 0
    garden1 = deepcopy(garden)
    for i, j in g_group:
        garden1[i][j] = 'G'
    for i, j in r_group:
        garden1[i][j] = 'R'
    queue = g_group + r_group

    while queue:
        temp = queue
        queue = []
        while temp:
            si, sj = temp.pop()
            for di, dj in ds:
                ni, nj = si + di, sj + dj
                if 0 <= ni < N and 0 <= nj < M and garden1[ni][nj] != 0:
                    if garden1[ni][nj] == 'F':
                        continue
                    if garden1[si][sj] == 'R':
                        if garden1[ni][nj] == 'G':
                            garden1[ni][nj] = 'F'
                            flower += 1
                        else:
                            garden1[ni][nj] = 'R'
                    elif garden1[si][sj] == 'G':
                        if garden1[ni][nj] == 'R':
                            garden1[ni][nj] = 'F'
                            flower += 1
                        else:
                            garden1[ni][nj] = 'G'
    if flower > max_flower:
        max_flower = flower


def select_r(r_group, d, next):
    if d == R:
        bfs()
    else:
        for i in range(next, N*M):
            row, col = i // M, i % M
            if garden[row][col] == 2:
                if (row, col) not in visited_g:
                    r_group.append((row, col))
                    select_r(r_group, d+1, i+1)
                    r_group.pop()


def select_g(g_group, d, next):
    if d == G:
        select_r(r_group, 0, 0)
    else:
        for i in range(next, N*M):
            row, col = i // M, i % M
            if garden[row][col] == 2:
                visited_g.append((row, col))
                g_group.append((row, col))
                select_g(g_group, d+1, i+1)
                visited_g.pop()
                g_group.pop()


beedable = [] # 뿌릴 수 있는 곳 좌표
g_group, r_group = [], []
visited_g = []
N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
max_flower = 0

select_g(g_group, 0, 0)
print(max_flower)
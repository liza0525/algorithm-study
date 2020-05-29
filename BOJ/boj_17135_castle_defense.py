import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint


import itertools
import collections


ds = [(0, -1), (1, 0), (0, 1)]


def move():
    pass


def set_archers(archers_j):
    g1 = [[0] * M for _ in range(N+1)]
    for i in range(N*M):
        row, col = i // M, i % M
        g1[N - row][col] = g[row][col]

    count, wall = 0, 0

    # for j in archers_j:
    #     g1[0][j] = 2 # 궁수

    while count + wall != e_num:
        visited = [[0] * M for _ in range(N+1)]
        for j in archers_j:
            queue = collections.deque()
            queue.append((0, j))
            dist, cand = 0, []
            while queue:
                cand = []
                si, sj = queue.popleft()
                dist += 1
                if dist > D: continue
                for di, dj in ds:
                    ni, nj = si + di, sj + dj
                    if ni == 0: continue
                    if not (0 <= ni < N and 0 <= nj < M): continue
                    if g1[ni][nj] == 1:
                        pass



N, M, D = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
g.append([0] * M)
e_num = sum(sum(g, []))
max_count = 0

for archers_j in list(itertools.combinations([i for i in range(M)], 3)):  # 궁수의 j 인덱스 셋
    set_archers(archers_j)

print(max_count)

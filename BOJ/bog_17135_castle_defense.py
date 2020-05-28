import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

import itertools

def set_archers(archers):
    global max_count
    g1 = [[0] * M for _ in range(N+1)]
    e_pos, ek_idx = [], [] # 적의 최초 위치, 잡은 적의 인덱스
    for num in range(N*M):
        row, col = num // M, num % M
        g1[row][col] = g[row][col]
        if g[row][col] == 1:
            e_pos.append([row, col])

    count = 0 # 이번 판에서 잡은 적

    while e_pos:
        print(e_pos)
        for i in range(len(e_pos)):
            for j in range(len(archers)):
                if abs(e_pos[i][0] - N) + abs(e_pos[i][1] - archers[j]) <= D:
                    count += 1
                    ek_idx.append(i)
                    break
                else:
                    e_pos[i][0] -= 1
                    if e_pos[i][0] == N:
                        ek_idx.append(i)

        if ek_idx:
            for i in ek_idx:
                e_pos.pop(i)

    if count > max_count:
        max_count = count


N, M, D = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
g.append([0] * M)
max_count = 0

for archers in list(itertools.combinations([i for i in range(M)], 3)): # 궁수의 j 인덱스 셋
    set_archers(archers)

print(max_count)
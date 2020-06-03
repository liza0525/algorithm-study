import sys
sys.stdin = open('../input.txt', 'r')

import itertools


def set_archers(archers):
    # print('archers', archers)
    global max_cnt
    enermies = []
    for idx in range(N * M):
        row, col = idx // M, idx % M
        if g[row][col]:
            enermies.append([row, col])

    cnt = 0

    while enermies:
        remove_e = []
        for j in archers:
            cand = []
            for i in range(len(enermies)):
                dist = abs(enermies[i][0] - N) + abs(enermies[i][1] - j)
                if dist <= D:
                    cand.append([dist, enermies[i][1], i])
            if cand:
                d1, ecol, i1 = sorted(cand).pop(0)
                if i1 not in remove_e:
                    remove_e.append(i1)
                    cnt += 1

        for i in range(len(enermies) - 1, -1, -1):
            if i not in remove_e:
                enermies[i][0] += 1
                if enermies[i][0] == N:
                    remove_e.append(i)

        for i in reversed(sorted(remove_e)):
            enermies.pop(i)

    if cnt > max_cnt:
        max_cnt = cnt


N, M, D = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
g.append([0] * M)
max_cnt = 0

for archers in map(list, itertools.combinations([i for i in range(M)], 3)):  # 궁수의 j 인덱스 셋
    set_archers(archers)

print(max_cnt)
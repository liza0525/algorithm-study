import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())
info, res = [], [0] * T
for _ in range(T):
    x, y = map(int, input().split())
    info.append((x, y))

for i in range(T):
    rank = 1
    x1, y1 = info[i]
    for j in range(T):
        if i == j: continue
        x2, y2 = info[j]
        if x1 < x2 and y1 < y2: rank += 1
    res[i] = rank

print(' '.join(map(str, res)))
import sys
sys.stdin = open('../input.txt', 'r')


N = int(input())
stairs = []
for _ in range(N):
    score = int(input())
    stairs.append(score)

max_score = [0 for _ in range(N)]

if N >= 1:
    max_score[0] = stairs[0]
if N >= 2:
    max_score[1] = stairs[1] + stairs[0]
if N >= 3:
    max_score[2] = max(stairs[0], stairs[1]) + stairs[2]
if N >= 4:
    for idx in range(3, N):
        max_score[idx] = max(max_score[idx - 3] + stairs[idx - 1], max_score[idx - 2]) + stairs[idx]

print(max_score[-1])
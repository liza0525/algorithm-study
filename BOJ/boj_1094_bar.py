import sys
sys.stdin = open('../input.txt', 'r')

X = int(input())
bars = [2 ** i for i in range(7)]
N = 7

for i in range(1 << N):
    select_bar_sum = 0
    select_bar_cnt = 0
    for j in range(N):
        if i & 1 << j:
            select_bar_sum += bars[j]
            select_bar_cnt += 1
    if select_bar_sum == X:
        break

print(select_bar_cnt)
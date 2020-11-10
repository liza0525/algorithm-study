import sys
sys.stdin = open('../input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
sub_sums = [0 for _ in range(N+1)]

for idx in range(1, N+1):
    sub_sums[idx] = sub_sums[idx-1] + numbers[idx-1]

ans_cnt = 0
start, end = 0, 0

while True:
    if end > N or start > N:
        break
    sub_sum = sub_sums[end] - sub_sums[start]
    if sub_sum == M:
        ans_cnt += 1
        end += 1
    elif sub_sum < M:
        end += 1
    elif sub_sum > M:
        start += 1

print(ans_cnt)
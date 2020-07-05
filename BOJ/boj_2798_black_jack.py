import sys
sys.stdin = open('../input.txt', 'r')

N, M = map(int, input().split())
nums = list(map(int, input().split()))
max_sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            res = nums[i] + nums[j] + nums[k]
            if res <= M and res > max_sum:
                max_sum = res
print(max_sum)
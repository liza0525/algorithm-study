import sys
sys.stdin = open('../input.txt', 'r')

## dp 이용(196ms)

N = int(input())

dp = [0] * (N+1)

for i in range(2, N+1):
    if i % 3 == 0:
        dp[i] = min(dp[i-1]+1, dp[i//3]+1)
    elif i % 2 == 0:
        dp[i] = min(dp[i-1]+1, dp[i//2]+1)
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])

## 재귀 이용(468ms)
# def calculate(num, d):
#     global min_cnt
#     if num == 1:
#         min_cnt = min(min_cnt, d)
#     else:
#         if d < min_cnt:
#             if num % 3 == 0:
#                 calculate(num // 3, d+1)
#             if num % 2 == 0:
#                 calculate(num // 2, d+1)
#             calculate(num-1, d+1)
#
#
# N = int(input())
# min_cnt = 1e9
#
# calculate(N, 0)
#
# print(min_cnt)
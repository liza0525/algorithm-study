import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')

N = int(input())

dp = [[0] * 10 for _ in range(N)]
dp[0] = [1] * 10

for i in range(1, N): # 행
    for j in range(10): # 열
        for k in range(j, 10):
            dp[i][k] += dp[i-1][j]

print(sum(dp[N-1]) % 10007)
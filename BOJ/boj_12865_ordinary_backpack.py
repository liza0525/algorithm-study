import sys
sys.stdin = open('../input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())

info = [
    tuple(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]


info = [[0, 0]] + info

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = info[i][0], info[i][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[N][K])
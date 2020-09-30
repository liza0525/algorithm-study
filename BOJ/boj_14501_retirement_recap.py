import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
day_diffs, revenues = [0] * N, [0] * N
for i in range(N):
    day_diffs[i], revenues[i] = map(int, input().split())

dp = revenues[:]

for today in range(N):
    for next_day in range(1, N):
        if next_day - today >= day_diffs[today]:
            dp[next_day] = max(dp[today] + revenues[next_day], dp[next_day])

max_revenue = 0

for today in range(N):
    if today + day_diffs[today] < N+1:
        max_revenue = max(max_revenue, dp[today])

print(max_revenue)
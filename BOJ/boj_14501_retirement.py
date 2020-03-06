import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
times, pays = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    times.append(t)
    pays.append(p)
dp = pays[:]

for i in range(2, N+1):
    for j in range(1, i):
        if i - j >= times[j]:
            dp[i] = max(pays[i] + dp[j], dp[i])
max_p = 0
for i in range(1, N+1):
    if i + times[i] <= N+1:
        if max_p < dp[i]:
            max_p = dp[i]

print(max_p)
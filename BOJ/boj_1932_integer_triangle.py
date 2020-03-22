N = int(input())

g = [list(map(int, input().split())) for _ in range(N)]
mp = [[0] * N for _ in range(N-1)] + [g[N-1]]

for i in range(N-2, -1, -1):
    for j in range(i+1):
        mp[i][j] = g[i][j] + max(mp[i+1][j], mp[i+1][j+1])

print(mp[0][0])
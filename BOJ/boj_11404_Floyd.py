import sys
sys.stdin = open('../input.txt', 'r')


N = int(input())
M = int(input())
g = [[1e9] * (N+1) for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    g[s][e] = min(g[s][e], c)


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            g[i][j] = 0 if i == j else min(g[i][j], g[i][k]+g[k][j])

for row in g[1:]:
    for col in row[1:]:
        print(0, end=' ') if col == 1e9 else print(col, end=' ')
    print()
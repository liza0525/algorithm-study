import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
M = int(input())
g = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a][b], g[b][a] = 1, 1

print(g)
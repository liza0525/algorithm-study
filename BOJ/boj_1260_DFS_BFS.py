import sys
sys.stdin = open('../input.txt', 'r')

def DFS():
    pass


def BFS():
    pass


N, M, V = map(int, input().split())
g = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    g[s][e], g[e][s] = 1, 1
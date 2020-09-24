import sys
sys.stdin = open('../input.txt', 'r')
sys.setrecursionlimit(10**6)

def dfs(node):
    for next in range(N):
        if visited[next] == 0 and g[node][next] == 1:
            visited[next] = 1
            dfs(next)

N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]

for node in range(N):
    visited = [0] * N
    dfs(node)
    print(' '.join(map(str, visited)))
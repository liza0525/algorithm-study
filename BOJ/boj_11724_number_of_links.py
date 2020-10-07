import sys
sys.stdin = open('../input.txt', 'r')
sys.setrecursionlimit(10000)


def dfs(now_node):
    visited[now_node] = True
    for next_node in range(1, N+1):
        if graph[now_node][next_node] == 1 and not visited[next_node]:
            dfs(next_node)


N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v], graph[v][u] = 1, 1

topology_num = 0


for start_node in range(1, N+1):
    if not visited[start_node]:
        dfs(start_node)
        topology_num += 1

print(topology_num)
import sys
sys.stdin = open('../input.txt', 'r')


## floyd-warshall
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for line in graph:
    print(' '.join(map(str, line)))




# ## dfs
# def dfs(node):
#     for next in range(N):
#         if visited[next] == 0 and g[node][next] == 1:
#             visited[next] = 1
#             dfs(next)
#
# N = int(input())
# g = [list(map(int, input().split())) for _ in range(N)]
#
# for node in range(N):
#     visited = [0] * N
#     dfs(node)
#     print(' '.join(map(str, visited)))
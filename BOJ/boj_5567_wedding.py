N = int(input())
M = int(input())
g = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    g[a][b], g[b][a] = 1, 1

for i in range(2, N+1):
    if g[1][i]:
        visited[i] = 1
        for j in range(2, N+1):
            if g[i][j] and not visited[j]:
                visited[j] = 1

print(sum(visited))

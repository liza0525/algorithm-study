import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
E = int(input())
visited = [0] * (N+1)
g = [[0] * (N+1) for _ in range(N+1)]

for _ in range(E):
    v1, v2 = map(int, input().split())
    g[v1][v2], g[v2][v1] = 1, 1

stack = []
stack.append(1)

while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = 1
        for i in range(N+1):
            if g[v][i] and not visited[i]:
                stack.append(i)

print(sum(visited)-1)
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
g = [[0] * 8 for _ in range(8)]


def dfs(v):
    visited = [0] * 8
    stack = []
    stack.append(v)

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for i in range(1, 8):
                if g[v][i] and not visited[i]:
                    stack.append(i)
    print()


def bfs(v):
    visited = [0] * 8
    queue=[]
    queue.append(v)
    visited[v] = 1

    while queue:
        tmp = queue
        for _ in range(len(tmp)):
            pn = queue.pop(0)
            print(pn, end=' ')
            for i in range(1,8):
                if g[pn][i] and not visited[i]:
                    queue.append(i)
                    visited[i] = 1
    print()

for i in range(0, len(edges), 2):
    g[edges[i]][edges[i+1]] = 1
    g[edges[i+1]][edges[i]] = 1

dfs(1)
bfs(1)
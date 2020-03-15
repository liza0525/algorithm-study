ds = [(1, 0), (0, 1), (0, -1), (-1, 0)]

def bfs(i, j):
    visited[i][j] = 1
    q = [(i, j)]

    while q:
        si, sj = q.pop(0)
        for di, dj in ds:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if g[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = visited[si][sj] + 1
                    q.append((ni, nj))
            elif ni == N and nj == M:
                break

N, M = map(int, input().split())
g = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

bfs(0, 0)

print(visited[N-1][M-1])
def is_field(i, j):
    return 0 <= i < N and 0 <= j < M


shapes = [
    [[(0, 1), (0, 1), (0, 1)], [(1, 0), (1, 0), (1, 0)]],  # 긴 막대 모양
    [[(0, 1), (1, 0), (0, -1)]],  # 정사각 모양
    [[(1, 0), (0, 1), (1, 0)], [(1, 0), (0, -1), (1, 0)], [(0, 1), (1, 0), (0, 1)], [(0, -1), (1, 0), (0, -1)]],  # 계단모양
    [[(0, 1), (0, 1), (-1, -1)], [(1, 0), (0, 1), (1, -1)], [(1, 0), (0, -1), (1, 1)], [(0, 1), (1, 0), (-1, 1)]],
    # ㅗ 모양
    [[(1, 0), (1, 0), (0, 1)], [(1, 0), (1, 0), (0, -1)], [(0, 1), (1, 0), (1, 0)], [(0, -1), (1, 0), (1, 0)],
     [(0, 1), (0, 1), (-1, 0)], [(0, 1), (0, 1), (1, 0)], [(-1, 0), (0, 1), (0, 1)], [(1, 0), (0, 1), (0, 1)]]  # ㄴ모양
]


def dfs(i, j):
    global max_res
    si, sj = i, j
    for tetros in shapes:
        for tetro in tetros:
            res = g[si][sj]
            for di, dj in tetro:
                si += di
                sj += dj
                if not is_field(si, sj): break
                res += g[si][sj]
                if res > max_res:
                    max_res = res
            si, sj = i, j


N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
max_res = 0
visited = []

for i in range(N):
    for j in range(M):
        dfs(i, j)

print(max_res)
from pprint import pprint
import sys
sys.stdin = open('../input.txt', 'r')


import collections


ds = [(0, 2), (1, 1), (1, -1),
      (0, -2), (-1, -1), (-1, 1)]


def bfs(i, j):
    global path_num, visited
    q = collections.deque()
    q.append((i, j))
    path_num = [g[i][j]]

    while q:
        si, sj = q.popleft()
        for di, dj in ds:
            ni, nj = si+di, sj+dj
            if not(0 <= ni < N and 0 <= nj < 2*N-1): continue
            if visited[ni][nj]: continue
            if visited[si][sj] + 1 <= visited[ni][nj]: continue
            pre_num, next_num = g[si][sj], g[ni][nj]
            if tiles[pre_num][1] != tiles[next_num][0]: continue
            q.append((ni, nj))
            path_num.append(g[ni][nj])
            visited[ni][nj] = visited[si][sj] + 1
    pprint(visited)


# def dfs(i, j):
#     global path_num, visited
#     if i == N-1 and j == 2*(N-1):
#         print(len(path_num))
#         for num in sorted(path_num): print(num+1, end=' ')
#         sys.exit(0)
#     else:
#         for di, dj in ds:
#             ni, nj = i+di, j+dj
#             if not(0 <= ni < N and 0 <= nj < 2*N-1): continue
#             if visited[ni][nj]: continue
#             pre_num, next_num = g[i][j], g[ni][nj]
#             if tiles[pre_num][1] != tiles[next_num][0]: continue
#             path_num.append(g[ni][nj])
#             visited[ni][nj] = visited[i][j] + 1
#             dfs(ni, nj)
#             path_num.pop()
#             visited[ni][nj] = 0




N = int(input())
tiles = [list(map(int, input().split())) for _ in range(N * N - N // 2)]
path_num = [0]
visited = [[0]*(2*N-1) for _ in range(N)]
visited[0][0] = 1


# g = [[0] * (2*N) for _ in range(N)]
# for i in range(len(g)):
#     if not(i % 2): # 홀수 줄(코딩에서는 0번부터라 반대로)
#         for j in range(0, 2*N, 2):
#             g[i][j], g[i][j+1] = tiles[(i*N - i//2) + j//2]
#     else: # 짝수 줄
#         for j in range(1, 2*(N-1), 2):
#             g[i][j], g[i][j+1] = tiles[(i*N - i//2) + j//2]


# 타일의 번호로 dfs 한다

g = [[0]*(2*N-1) for _ in range(N)]

for i in range(N):
    if not(i % 2): # 그림 상 홀수 줄
        for j in range(0, 2*N, 2):
            g[i][j] = (i*N - i//2) + j//2
    else: # 그림 상 짝수 줄
        for j in range(1, 2*(N-1), 2):
            g[i][j] = (i*N - i//2) + j//2

bfs(0, 0)
print(path_num)
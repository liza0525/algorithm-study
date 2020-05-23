import sys
sys.stdin = open('../input.txt', 'r')

import collections


ds = [(0, 2), (1, 1), (-1, 1),
      (0, -2), (-1, -1), (1, -1)]


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
            pre_num, next_num = g[si][sj], g[ni][nj]
            if dj > 0 and tiles[pre_num][1] != tiles[next_num][0]: continue
            if dj < 0 and tiles[pre_num][0] != tiles[next_num][1]: continue
            q.append((ni, nj))
            pre_path.update({(ni, nj): [g[ni][nj], (si, sj)]}) # key : 현재 인덱스, value : 현재 번호, 이전 인덱스
            visited[ni][nj] = 1


N = int(input())
tiles = [list(map(int, input().split())) for _ in range(N * N - N // 2)]
pre_path = dict()
visited = [[0]*(2*N-1) for _ in range(N)]
visited[0][0] = 1

g = [[0]*(2*N-1) for _ in range(N)]

for i in range(N):
    if not(i % 2): # 그림 상 홀수 줄
        for j in range(0, 2*N, 2):
            g[i][j] = (i*N - i//2) + j//2
    else: # 그림 상 짝수 줄
        for j in range(1, 2*(N-1), 2):
            g[i][j] = (i*N - i//2) + j//2

bfs(0, 0)

path_num, (si, sj) = max(pre_path.values())
res = [path_num]
while True:
    path_num, (si, sj) = pre_path[(si, sj)]
    res.append(path_num)
    if si == 0 and sj == 0:
        res.append(0)
        break

print(len(res))
for i in reversed(res):
    print(i+1, end=' ')
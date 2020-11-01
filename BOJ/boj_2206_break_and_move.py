import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < M


def move(r, c):
    queue = deque()
    queue.append([r, c, 0])
    dist[r][c][0] = 1

    while queue:
        now_r, now_c, is_break = queue.popleft()
        for delta_r, delta_c in deltas:
            next_r, next_c = now_r + delta_r, now_c + delta_c
            if not is_field(next_r, next_c): continue
            if ground[next_r][next_c] and is_break: continue
            if not ground[next_r][next_c]:
                if not dist[next_r][next_c][is_break] or dist[next_r][next_c][is_break] > dist[now_r][now_c][is_break] + 1:
                    dist[next_r][next_c][is_break] = dist[now_r][now_c][is_break] + 1
                    queue.append((next_r, next_c, is_break))
            else:
                if not dist[next_r][next_c][1] or dist[next_r][next_c][1] > dist[now_r][now_c][is_break] + 1:
                    dist[next_r][next_c][1] = dist[now_r][now_c][is_break] + 1
                    queue.append((next_r, next_c, 1))


N, M = map(int, input().split())
ground = [list(map(int, input())) for _ in range(N)]
dist = [[[0, 0] for _ in range(M)] for _ in range(N)]
# 0 벽을 한 번도 안 뚫었을 때의 최소 거리
# 1 벽을 한 번 뚫었을 때의 최소 거리

move(0, 0)

if dist[N-1][M-1][0] and dist[N-1][M-1][1]:
    print(min(dist[N-1][M-1]))
elif dist[N-1][M-1][0]:
    print(dist[N-1][M-1][0])
elif dist[N-1][M-1][1]:
    print(dist[N-1][M-1][1])
else:
    print(-1)
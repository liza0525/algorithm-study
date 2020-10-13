import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

def play_game():
    for start_c in range(N - 1):
        now_r, now_c = 0, start_c
        while now_r < H:
            if visited[now_r][now_c] == 1:
                if (now_r, now_c) in ladders:
                    now_c += 1
                else:
                    now_c -= 1
            now_r += 1
        if now_c != start_c:
            return False
    return True


def set_ladder(start_r, d):
    global min_horizon_cnt
    if d > 3:
        return
    else:
        for r in range(start_r, H):
            for c in range(N - 1):
                if visited[r][c] == 0 and visited[r][c + 1] == 0:
                    visited[r][c], visited[r][c + 1] = 1, 1
                    ladders.append((r, c))

                    if play_game():
                        if min_horizon_cnt == -1:
                            min_horizon_cnt = d
                        else:
                            min_horizon_cnt = min(min_horizon_cnt, d)
                    else:
                        set_ladder(r, d + 1)
                    visited[r][c], visited[r][c + 1] = 0, 0

                    ladders.pop()


N, M, H = map(int, input().split())
visited = [[0 for _ in range(N)] for _ in range(H)]
ladders = []
for _ in range(M):
    a, b = map(int, input().split())
    visited[a - 1][b - 1], visited[a - 1][b] = 1, 1
    ladders.append((a - 1, b - 1))
min_horizon_cnt = -1

if M == 0:
    min_horizon_cnt = 0
elif M == 1:
    min_horizon_cnt = 1
else:
    if play_game():
        min_horizon_cnt = 0
    else:
        set_ladder(0, 1)

print(min_horizon_cnt)
import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint


deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def make_road(r, c):
    global max_road_length
    queue = [(r, c)]
    dist = [[0 for _ in range(N)] for _ in range(N)]
    dist[r][c] = 1

    while queue:
        now_r, now_c = queue.pop(0)
        for delta_r, delta_c in deltas:
            next_r, next_c = now_r + delta_r, now_c + delta_c
            if not is_field(next_r, next_c): continue
            if ground[next_r][next_c] >= ground[now_r][now_c]: continue
            if dist[next_r][next_c] >= dist[now_r][now_c] + 1: continue
            queue.append((next_r, next_c))
            dist[next_r][next_c] = dist[now_r][now_c] + 1


    cand_road_length = max(sum(dist, []))
    max_road_length = max(cand_road_length, max_road_length)


def set_start():
    for r in range(N):
        for c in range(N):
            if ground[r][c] == max_height:
                make_road(r, c)



T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]
    max_height = max(sum(ground, []))
    max_road_length = 0

    for r in range(N):
        for c in range(N):
            for k in range(K+1):
                ground[r][c] -= k
                set_start()
                ground[r][c] += k

    print('#{} {}'.format(test_case+1, max_road_length))
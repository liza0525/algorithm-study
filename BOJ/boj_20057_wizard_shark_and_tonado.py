import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint


deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 좌 하 우 상
spread_deltas = [[[(-1, 1), (1, 1)], [(-2, 0), (2, 0)], [(0, -2)], [(-1, 0), (1, 0)], [(-1, -1), (1, -1)], [(0, -1)]], # 좌 : 1, 2, 5, 7, 10, alpha %
                 [[(-1, -1), (-1, 1)], [(0, -2), (0, 2)], [(2, 0)], [(0, -1), (0, 1)], [(1, -1), (1, 1)], [(1, 0)]], # 하 : 1, 2, 5, 7, 10, alpha %
                 [[(-1, -1), (1, -1)], [(-2, 0), (2, 0)], [(0, 2)], [(-1, 0), (1, 0)], [(-1, 1), (1, 1)], [(0, 1)]], # 우 : 1, 2, 5, 7, 10, alpha %
                 [[(1, -1), (1, 1)], [(0, -2), (0, 2)], [(-2, 0)], [(0, -1), (0, 1)], [(-1, -1), (-1, 1)], [(-1, 0)]]] # 상 : 1, 2, 5, 7, 10, alpha %
percentage = [1, 2, 5, 7, 10]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def spread(r, c, d):
    global total_sand
    spread_delta = spread_deltas[d]
    remain_sand = 0
    for p_idx in range(6):
        if p_idx == 5:
            delta_r, delta_c = spread_delta[p_idx][0]
            next_r, next_c = r + delta_r, c + delta_c
            alpha_sand = ground[r][c] - remain_sand
            if not is_field(next_r, next_c):
                total_sand += alpha_sand
            else:
                ground[next_r][next_c] += alpha_sand
        else:
            for delta_r, delta_c in spread_delta[p_idx]:
                now_sand = ground[r][c] * percentage[p_idx] // 100
                next_r, next_c = r + delta_r, c + delta_c
                if not is_field(next_r, next_c):
                    total_sand += now_sand
                else:
                    ground[next_r][next_c] += now_sand
                remain_sand += now_sand
    ground[r][c] = 0


def move(r, c, d):
    now_length = 1
    while not (r == 0 and c == 0):
        cnt = 2 if now_length < N - 1 else 3

        for _ in range(cnt):
            delta_r, delta_c = deltas[d]
            for _ in range(now_length):
                r += delta_r
                c += delta_c
                spread(r, c, d)

            d = (d + 1) % 4
        now_length += 1


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]
total_sand = 0
r, c = N // 2 , N // 2

move(r, c, 0)

print(total_sand)
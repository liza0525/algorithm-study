import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

deltas = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def is_field(r, c):
    return 1 <= r <= N and 1 <= c <= N


def get_boundary(start_r, start_c, d1, d2):
    boundaries = []
    now_r, now_c = start_r, start_c
    direction = 0

    while direction < 4:
        delta_r, delta_c = deltas[direction]
        d_num = d1 if direction == 1 or direction == 3 else d2

        for _ in range(d_num):
            now_r, now_c = now_r + delta_r, now_c + delta_c

            boundaries.append((now_r, now_c))

        direction += 1

    return boundaries


def gerrymandering(start_r, start_c, d1, d2):
    global min_diff
    boundaries = get_boundary(start_r, start_c, d1, d2)

    first_area, second_area, third_area, forth_area = 0, 0, 0, 0

    # 1번 구역
    for r in range(start_r + d1):
        for c in range(start_c + 1):
            if (r, c) in boundaries: break
            first_area += ground[r][c]

    # 2번 구역
    for r in range(start_r + d2 + 1):
        for c in range(N, start_c, -1):
            if (r, c) in boundaries: break
            second_area += ground[r][c]

    # 3번 구역
    for r in range(start_r + d1, N+1):
        for c in range(start_c - d1 + d2):
            if (r, c) in boundaries: break
            third_area += ground[r][c]

    # 4번 구역
    for r in range(N, start_r + d2, -1):
        for c in range(N, start_c - d1 + d2 - 1, -1):
            if (r, c) in boundaries: break
            forth_area += ground[r][c]

    # 5번 구역
    fifth_area = total_people - sum([first_area, second_area, third_area, forth_area])

    max_people_cnt = max(first_area, second_area, third_area, forth_area, fifth_area)
    min_people_cnt = min(first_area, second_area, third_area, forth_area, fifth_area)

    min_diff = min(min_diff, max_people_cnt - min_people_cnt)


N = int(input())
ground = [[0 for _ in range(N+1)] for _ in range(N+1)]

for r in range(1, N+1):
    ground[r] = [0] + list(map(int, input().split()))

total_people = sum(sum(ground, []))

min_diff = 1e5

for d1 in range(1, N):
    for d2 in range(1, N):
        for start_r in range(1, N+1):
            for start_c in range(1, N+1):
                if not (1 <= start_r < start_r + d1 + d2 <= N): continue
                if not (1 <= start_c - d1 < start_c < start_c + d2 <= N): continue
                gerrymandering(start_r, start_c, d1, d2)

print(min_diff)
import sys
sys.stdin = open('../input.txt', 'r')

delta_counter_clock = [(0, 1), (-1, 0), (0, -1), (1, 0)]
delta_clock = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_field(r, c):
    return 0 <= r < R and 0 <= c < C


def spread():
    calculate = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if ground[r][c] != 0 and ground[r][c] != -1:
                move_cnt = 0
                for delta_r, delta_c in delta_clock:
                    next_r, next_c = r+delta_r, c+delta_c
                    if not is_field(next_r, next_c): continue
                    if ground[next_r][next_c] == -1: continue
                    calculate[next_r][next_c] += ground[r][c] // 5
                    move_cnt += 1
                calculate[r][c] -= ground[r][c] // 5 * move_cnt

    for r in range(R):
        for c in range(C):
            ground[r][c] += calculate[r][c]


def clean(cleaner, clockwise):
    now_r, now_c = cleaner
    temp_amount = 0
    for idx in range(4):
        delta_r, delta_c = clockwise[idx]
        while True:
            next_r, next_c = now_r + delta_r, now_c + delta_c
            if not (0 <= next_r < R and 0 <= next_c < C) or ground[next_r][next_c] == -1:
                break
            ground[next_r][next_c], temp_amount = temp_amount, ground[next_r][next_c]
            now_r, now_c = next_r, next_c


R, C, T = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(R)]

cleaners = []
for r in range(R):
    if ground[r][0] == -1:
        cleaners = [(r, 0), (r+1, 0)]
        break


for _ in range(T):
    spread()
    clean(cleaners[0], delta_counter_clock)
    clean(cleaners[1], delta_clock)

total_dust = 0

for r in range(R):
    for c in range(C):
        if ground[r][c] != 0 and ground[r][c] != -1:
            total_dust += ground[r][c]

print(total_dust)
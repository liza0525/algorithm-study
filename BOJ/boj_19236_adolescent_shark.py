from pprint import pprint
import sys
sys.stdin = open('../input.txt', 'r')

import copy

deltas = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def is_field(r, c):
    return 0 <= r < 4 and 0 <= c < 4


def move_fish(shark_r, shark_c):
    global ground
    for k in range(1, 17):
        if k in eating_num:
            continue
        now_r, now_c = 0, 0
        for r in range(4):
            for c in range(4):
                if ground[r][c] == [-1, -1]: continue
                if ground[r][c][0] == k:
                    now_r, now_c = r, c
                    break
        now_direction = ground[now_r][now_c][1]
        while True:
            delta_r, delta_c = deltas[ground[now_r][now_c][1]]
            next_r, next_c = now_r + delta_r, now_c + delta_c
            if not is_field(next_r, next_c) or (shark_r == next_r and shark_c == next_c):
                ground[now_r][now_c][1] = (ground[now_r][now_c][1] + 1) % 8
                if ground[now_r][now_c][1] == now_direction:
                    break
            else:
                now_fish, next_fish = ground[now_r][now_c], ground[next_r][next_c]
                ground[now_r][now_c], ground[next_r][next_c] = next_fish, now_fish
                break


def move_shark(r, c, direction, total_num):
    global max_total_num, eating_num, ground
    max_total_num = max(total_num, max_total_num)
    temp_ground = copy.deepcopy(ground)
    move_fish(r, c)
    for k in range(1, 4):
        delta_r, delta_c = k * deltas[direction][0], k * deltas[direction][1]
        next_r, next_c = r + delta_r, c + delta_c
        if not is_field(next_r, next_c): break
        if ground[next_r][next_c] == [-1, -1]: continue
        fish_number, fish_direction = ground[next_r][next_c]
        eating_num.append(fish_number)
        ground[next_r][next_c] = [-1, -1]
        move_shark(next_r, next_c, fish_direction, total_num + fish_number)
        ground[next_r][next_c] = [fish_number, fish_direction]
        eating_num.pop()
    ground = copy.deepcopy(temp_ground)


ground = [[[0, 0] for _ in range(4)] for _ in range(4)]
max_total_num = 0
for r in range(4):
    line = list(map(int, input().split()))
    for c in range(0, 8, 2):
        ground[r][c // 2][0], ground[r][c // 2][1] = line[c], line[c+1]-1

start_total_num, start_direction = ground[0][0]
eating_num = [start_total_num]
ground[0][0] = [-1, -1]
move_shark(0, 0, start_direction, start_total_num)

print(max_total_num)
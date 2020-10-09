import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def move(move_info):
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                group_num = visited[r][c]
                countries[r][c] = move_info[group_num]


def open_boundary(r, c, group_num):
    visited[r][c] = group_num
    stack = [(r, c)]
    total_people = countries[r][c]
    countries_cnt = 1

    while stack:
        now_r, now_c = stack.pop()
        for delta_r, delta_c in deltas:
            next_r, next_c = now_r + delta_r, now_c + delta_c
            if not is_field(next_r, next_c): continue
            if visited[next_r][next_c]: continue
            if not (L <= abs(countries[now_r][now_c] - countries[next_r][next_c]) <= R): continue
            if (next_r, next_c) in stack: continue
            visited[next_r][next_c] = group_num
            stack.append((next_r, next_c))
            countries_cnt += 1
            total_people += countries[next_r][next_c]

    return total_people, countries_cnt



N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
move_cnt = 0

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    group_num = 1
    move_info = dict()
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                total_people, countries_cnt = open_boundary(r, c, group_num)
                # print(total_people, countries_cnt)
                move_info[group_num] = (total_people // countries_cnt)
                group_num += 1
    # pprint(visited)
    if group_num == N ** 2 + 1:
        break
    # print(is_move)
    # if not is_move:
    #     break
    move(move_info)
    move_cnt += 1

print(move_cnt)
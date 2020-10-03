import sys
sys.stdin = open('../input.txt', 'r')

import itertools

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < M


def spread(r, c):
    global visited
    stack = [(r, c)]
    visited[r][c] = True

    while stack:
        now_r, now_c = stack.pop()
        for delta_r, delta_c in deltas:
            next_r, next_c = now_r + delta_r, now_c + delta_c
            if not is_field(next_r, next_c): continue
            if visited[next_r][next_c]: continue
            if ground[next_r][next_c] != 0: continue
            stack.append((next_r, next_c))
            visited[next_r][next_c] = True



def set_wall(wall_cand):
    global visited, ground, max_safe_area

    safe_area = 0
    for r, c in wall_cand:
        ground[r][c] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if ground[r][c] == 2 and not visited[r][c]:
                spread(r, c)


    for r in range(N):
        for c in range(M):
            if ground[r][c] == 0 and not visited[r][c]:
                safe_area += 1

    max_safe_area = max(max_safe_area, safe_area)

    for r, c in wall_cand:
        ground[r][c] = 0


N, M = map(int, input().split())
ground = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
wall_cands = []
max_safe_area = 0

for r in range(N):
    line = list(map(int, input().split()))
    for c in range(M):
        ground[r][c] = line[c]
        if ground[r][c] == 0:
            wall_cands.append((r, c))

for wall_cand in itertools.combinations(wall_cands, 3):
    set_wall(wall_cand)

print(max_safe_area)
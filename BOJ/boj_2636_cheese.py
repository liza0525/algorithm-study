import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint
from collections import deque

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < M


def fill_air(r, c):
    queue = deque()
    queue.append((r, c))
    ground[r][c] = 2

    while queue:
        now_r, now_c = queue.popleft()
        for delta_r, delta_c in deltas:
            next_r, next_c = now_r + delta_r, now_c + delta_c
            if not is_field(next_r, next_c): continue
            if ground[next_r][next_c]: continue
            queue.append((next_r, next_c))
            ground[next_r][next_c] = 2


def melt_cheese():
    cand = set()
    for r in range(N):
        for c in range(M):
            if ground[r][c] == 1:
                for delta_r, delta_c in deltas:
                    next_r, next_c = r + delta_r, c + delta_c
                    if not is_field(next_r, next_c): continue
                    if ground[next_r][next_c] == 2: 
                        cand.add((r, c))
    return cand


def is_all_air():
    for r in range(N):
        for c in range(M):
            if ground[r][c] != 2:
                return False
    return True

N, M = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
hour = 0

fill_air(0, 0)
while not is_all_air():
    cand = melt_cheese()

    for r, c in cand:
        ground[r][c] = 2
        fill_air(r, c)

    hour += 1

print(hour)
print(len(cand))
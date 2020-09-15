import sys
from collections import deque
sys.stdin = open('../input.txt', 'r')

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Fish:
    def __init__(self, r, c, size):
        self.r = r
        self.c = c
        self.size = size


class Shark:
    def __init__(self, r, c, size, eat):
        self.r = r
        self.c = c
        self.size = size
        self.eat = eat


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]

for num in range(N*N):
    r, c = num // N, num % N
    if ground[r][c] == 9:
        shark = Shark(r, c, 2, 0)
        ground[r][c] = 0
        break

queue = deque([(shark.r, shark.c)])
total_dist = 0
dist = [[1e9 for _ in range(N)] for _ in range(N)]
dist[shark.r][shark.c] = 0

while queue:
    candidate = []
    temp = queue
    queue = deque()
    while temp:
        r, c = temp.popleft()
        for delta_r, delta_c in deltas:
            next_r, next_c = r+delta_r, c+delta_c
            if not (0 <= next_r < N and 0 <= next_c < N): continue
            if dist[next_r][next_c] <= dist[r][c] + 1: continue
            if ground[next_r][next_c] == 0 or ground[next_r][next_c] == shark.size:
                dist[next_r][next_c] = dist[r][c] + 1
                queue.append((next_r, next_c))
            elif ground[next_r][next_c] < shark.size:
                dist[next_r][next_c] = dist[r][c] + 1
                candidate.append(Fish(next_r, next_c, ground[next_r][next_c]))

    if candidate:
        fish = sorted(candidate, key=lambda x: (x.r, x.c))[0]
        shark.r, shark.c = fish.r, fish.c
        total_dist += dist[shark.r][shark.c]
        ground[shark.r][shark.c] = 0
        shark.eat += 1
        queue = deque([(shark.r, shark.c)])
        dist = [[1e9 for _ in range(N)] for _ in range(N)]
        dist[shark.r][shark.c] = 0

    if shark.size == shark.eat:
        shark.size += 1
        shark.eat = 0

print(total_dist)
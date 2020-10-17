import sys
sys.stdin = open('../input.txt', 'r')

import collections

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

tubes = [0,
         [0, 1, 2, 3], # 1번
         [0, 1], # 2번
         [2, 3], # 3번
         [0, 3], # 4번
         [1, 3], # 5번
         [1, 2], # 6번
         [0, 2]] # 7번


def is_field(r, c):
    return 0 <= r < N and 0 <= c < M


def is_go_to_next_tube(direction, next_r, next_c):
    next_tube = tubes[ground[next_r][next_c]]
    if direction == 0:
        opposite_dir = 1
    elif direction == 1:
        opposite_dir = 0
    elif direction == 2:
        opposite_dir = 3
    elif direction == 3:
        opposite_dir = 2

    return True if opposite_dir in next_tube else False


def go_jailbreak(r, c):
    queue = collections.deque()
    queue.append((r, c))
    visited[r][c] = 1

    while queue:
        now_r, now_c = queue.popleft()
        tube = tubes[ground[now_r][now_c]]
        for direction in tube:
            delta_r, delta_c = deltas[direction]
            next_r, next_c = now_r + delta_r, now_c + delta_c
            if visited[now_r][now_c] + 1 > L: continue
            if not is_field(next_r, next_c): continue
            if ground[next_r][next_c] == 0: continue
            if not is_go_to_next_tube(direction, next_r, next_c): continue
            if visited[next_r][next_c] != 0 and visited[next_r][next_c] <= visited[now_r][now_c] + 1: continue
            queue.append((next_r, next_c))
            visited[next_r][next_c] = visited[now_r][now_c] + 1


T = int(input())

for test_case in range(T):
    N, M, R, C, L = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    total_tube_cnt = 0

    go_jailbreak(R, C)

    for r in range(N):
        for c in range(M):
            if visited[r][c]:
                total_tube_cnt += 1

    print('#{} {}'.format(test_case+1, total_tube_cnt))
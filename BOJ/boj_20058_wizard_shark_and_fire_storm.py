import sys
sys.stdin = open('../input.txt', 'r')


deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def dfs(r, c):
    global visited, max_ice_size, total_ice
    stack = [(r, c)]
    visited[r][c] = 1
    ice_size = 1
    total_ice += ground[r][c]

    while stack:
        now_r, now_c = stack.pop()
        for delta_r, delta_c in deltas:
            next_r, next_c = now_r + delta_r, now_c + delta_c
            if not is_field(next_r, next_c): continue
            if ground[next_r][next_c] == 0: continue
            if visited[next_r][next_c]: continue
            stack.append((next_r, next_c))
            visited[next_r][next_c] = 1
            total_ice += ground[next_r][next_c]
            ice_size += 1

    max_ice_size = max(max_ice_size, ice_size)


def melt():
    cand = []
    for r in range(N):
        for c in range(N):
            if ground[r][c] == 0: continue
            neighbor_cnt = 0
            for delta_r, delta_c in deltas:
                next_r, next_c = r + delta_r, c + delta_c
                if not is_field(next_r, next_c): continue
                if ground[next_r][next_c] != 0:
                    neighbor_cnt += 1

            if neighbor_cnt < 3:
                cand.append((r, c))

    for r, c in cand:
        ground[r][c] -= 1


def rotate(level):
    global ground
    level_size = 2 ** level
    half_level_size = level_size // 2

    # ========================================================================
    # for start_r in range(0, N, level_size):
    #     for start_c in range(0, N, level_size):
    #         for rotate_r in range(start_r, start_r + half_level_size):
    #             for rotate_c in range(start_c, start_c + half_level_size):
    #                 ground[rotate_r][rotate_c], ground[rotate_r][rotate_c + half_level_size], \
    #                 ground[rotate_r + half_level_size][rotate_c + half_level_size], ground[rotate_r + half_level_size][rotate_c] = \
    #                     ground[rotate_r + half_level_size][rotate_c], ground[rotate_r][rotate_c], \
    #                     ground[rotate_r][rotate_c + half_level_size], ground[rotate_r + half_level_size][rotate_c + half_level_size]
    # ========================================================================

    for r in range(0, N, level_size):
        for c in range(0, N, level_size):
            for k in range(half_level_size):
                start_r, start_c = r + k, c + k
                last_r, last_c = r + level_size - k, c + level_size - k
                for idx in range(level_size - 2 * k -1):
                    ground[start_r][start_c + idx], ground[start_r + idx][last_c - 1], \
                    ground[last_r - 1][last_c - 1 - idx], ground[last_r - 1 - idx][start_c] = \
                        ground[last_r - 1 - idx][start_c], ground[start_r][start_c + idx], \
                        ground[start_r + idx][last_c - 1], ground[last_r - 1][last_c - 1 - idx]

    melt()


N, Q = map(int, input().split())
N = 2 ** N
ground = [list(map(int, input().split())) for _ in range(N)]
levels = list(map(int, input().split()))
visited = [[0 for _ in range(N)] for _ in range(N)]
total_ice, max_ice_size = 0, 0

for level in levels:
    rotate(level)

for r in range(N):
    for c in range(N):
        if ground[r][c] and not visited[r][c]:
            dfs(r, c)


print(total_ice)
print(max_ice_size)
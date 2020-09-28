import sys
sys.stdin = open('../input.txt', 'r')


import collections

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def move(r, c, delta_r, delta_c):
    dist = 0
    while g[r+delta_r][c+delta_c] != '#' and g[r][c] != 'O':
        r, c = r+delta_r, c+delta_c
        dist += 1
    return r, c, dist


def bfs(red_r, red_c, blue_r, blue_c, cnt):
    queue = [(red_r, red_c, blue_r, blue_c, cnt)]
    queue = collections.deque(queue)
    visited = [(red_r, red_c, blue_r, blue_c)]

    while queue:
        red_r, red_c, blue_r, blue_c, cnt = queue.popleft()

        if cnt >= 10:
            return -1

        for delta_r, delta_c in deltas:
            next_cnt = cnt + 1
            next_red_r, next_red_c, red_dist = move(red_r, red_c, delta_r, delta_c)
            next_blue_r, next_blue_c, blue_dist = move(blue_r, blue_c, delta_r, delta_c)

            # 파란 구슬이 O에 도달하지만 않으면 모든 로직을 수행한다.
            if g[next_blue_r][next_blue_c] != 'O':
                if g[next_red_r][next_red_c] == 'O':
                    return next_cnt

                # 구슬이 겹칠 수 없기 때문에 더 멀리서 온 구슬을 한칸 다시 뒤로 돌림
                if next_red_r == next_blue_r and next_red_c == next_blue_c:
                    if red_dist > blue_dist:
                        next_red_r -= delta_r
                        next_red_c -= delta_c
                    elif red_dist < blue_dist:
                        next_blue_r -= delta_r
                        next_blue_c -= delta_c

                if (next_red_r, next_red_c, next_blue_r, next_blue_c) not in visited:
                    queue.append((next_red_r, next_red_c, next_blue_r, next_blue_c, next_cnt))
                    visited.append((next_red_r, next_red_c, next_blue_r, next_blue_c))
    return -1


R, C = map(int, input().split())
g = [list(input()) for _ in range(R)]
visited = []
red_r, red_c, blue_r, blue_c = 0, 0, 0, 0
min_cnt = 1e9

for r in range(R):
    for c in range(C):
        if g[r][c] == 'R':
            red_r, red_c = r, c
        elif g[r][c] == 'B':
            blue_r, blue_c = r, c

print(bfs(red_r, red_c, blue_r, blue_c, 0))
import sys
sys.stdin = open('../input.txt', 'r')

deltas = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def tour(r, c, d):
    global max_desserts_cnt
    if d == 3 and r + deltas[d][0] == start_r and c + deltas[d][1] == start_c:
        max_desserts_cnt = max(max_desserts_cnt, len(desserts))
    else:
        next_r, next_c = r + deltas[d][0], c + deltas[d][1]
        if not is_field(next_r, next_c): return
        if ground[next_r][next_c] not in desserts:
            desserts.append(ground[next_r][next_c])
            tour(next_r, next_c, d)
            if d != 3:
                tour(next_r, next_c, d+1)
            desserts.pop()


T = int(input())
for test_case in range(T):
    max_desserts_cnt = -1
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]

    for start_r in range(N):
        for start_c in range(N):
            if start_r == N-1 or start_c == 0 or start_c == N-1: continue
            desserts = [ground[start_r][start_c]]
            tour(start_r, start_c, 0)

    print('#{} {}'.format(test_case+1, max_desserts_cnt))
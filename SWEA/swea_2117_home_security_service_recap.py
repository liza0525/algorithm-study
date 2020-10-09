import sys
sys.stdin = open('../input.txt', 'r')


def get_benefit(r, c):
    home_cnt = 0
    for house_r, house_c in houses:
        if abs(r - house_r) + abs(c - house_c) < k:
            home_cnt += 1
    return home_cnt * M, home_cnt


T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    houses = []
    ground = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if ground[r][c] == 1:
                houses.append((r, c))

    max_home_cnt = 1

    for k in range(1, 2 * N):
        cost = k * k + (k - 1) * (k - 1)
        for r in range(N):
            for c in range(N):
                benefit, home_cnt = get_benefit(r, c)
                if benefit >= cost and home_cnt > max_home_cnt:
                    max_home_cnt = home_cnt

    print('#{} {}'.format(test_case+1, max_home_cnt))
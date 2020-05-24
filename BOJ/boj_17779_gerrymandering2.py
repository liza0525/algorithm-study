import sys
sys.stdin = open('../input.txt', 'r')


ds = [(1, 1), (1, -1), (-1, -1), (-1, 1)] # 대각선


def is_field(i, j):
    return 0 <= i < N and 0 <= j < N


def gerrymandering(boundary, d1, d2):
    global min_diff
    city_num = [0] * 6
    # 1번 구역
    for r in range(si+d1):
        for c in range(sj+1):
            if (r, c) in boundary: break
            city_num[1] += A[r][c]

    # 2번 구역
    for r in range(si+d2+1):
        for c in range(N-1, sj, -1):
            if (r, c) in boundary: break
            city_num[2] += A[r][c]

    # 3번 구역
    for r in range(si+d1, N):
        for c in range(sj-d1+d2):
            if (r, c) in boundary: break
            city_num[3] += A[r][c]

    # 4번 구역
    for r in range(N-1, si+d2, -1):
        for c in range(N-1, sj-d1+d2-1, -1):
            if (r, c) in boundary: break
            city_num[4] += A[r][c]

    city_num[5] = total_num - sum(city_num)

    diff = max(city_num) - min(city_num[1:])

    if diff < min_diff:
        min_diff = diff


def set_boundary(i, j, direction, d1, d2):
    boundary.append((i, j))
    if direction == 3 and i + ds[3][0] == si and j + ds[3][1] == sj:
        gerrymandering(boundary, d1, d2)
    else:
        di, dj = ds[direction]
        ni, nj = i + di, j + dj
        if is_field(ni, nj):
            if direction == 1: d1 += 1
            if direction == 0: d2 += 1
            set_boundary(ni, nj, direction, d1, d2)
            if direction != 3: set_boundary(ni, nj, direction+1,  d1, d2)
    boundary.pop()


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
# city_num = [0] * 6 # 인구수
total_num = sum(sum(A, []))
boundary = [] # 경계선
min_diff = 1e9

for i in range(N):
    for j in range(N):
        si, sj = i, j
        set_boundary(i, j, 0, 0, 0)

print(min_diff)
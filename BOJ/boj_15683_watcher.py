import copy
import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')

camera_ds = [
    [],
    [[(0, -1)], [(0, 1)], [(-1, 0)], [(1, 0)]],
    [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]],
    [[(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]],
    [[(0, -1), (0, 1), (-1, 0)], [(0, -1), (0, 1), (1, 0)], [(0, -1), (-1, 0), (1, 0)], [(0, 1), (-1, 0), (1, 0)]],
    [[(0, -1), (0, 1), (-1, 0), (1, 0)]]
]


def is_field(i, j):
    return 0 <= i < N and 0 <= j < M


def solve(c_info):
    global min_blind
    temp_g = copy.deepcopy(g)
    for si, sj, ds in c_info:
        for di, dj in ds:
            i, j = si, sj
            while is_field(i+di, j+dj) and temp_g[i+di][j+dj] != 6:
                i += di
                j += dj
                temp_g[i][j] = '#'

    num_blind = sum(temp_g, []).count(0)
    if num_blind < min_blind:
        min_blind = num_blind

def set_cameras(d, c_info):
    if d == len(cameras):
        solve(c_info)
    else:
        i, j, c_num = cameras[d]
        for ds in camera_ds[c_num]:
            c_info.append((i, j, ds))
            set_cameras(d+1, c_info)
            c_info.pop()


N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
min_blind = 987654321
cameras = []
for i in range(N):
    for j in range(M):
        if g[i][j] and g[i][j] != 6:
            cameras.append((i, j, g[i][j]))

set_cameras(0, [])

print(min_blind)
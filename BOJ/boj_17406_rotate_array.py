import sys
sys.stdin = open('../input.txt', 'r')
import itertools
import copy


deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상


def rotate(res_ground, r, c, s):
    for ss in range(s, 0, -1):
        now_r, now_c = r-ss, c-ss
        temp_next_num = res_ground[r-ss][c-ss]
        for d in range(4):
            delta_r, delta_c = deltas[d]
            while True:
                if not (r-ss <= now_r + delta_r <= r+ss and c-ss <= now_c + delta_c <= c+ss):
                    break
                next_r, next_c = now_r + delta_r, now_c + delta_c
                temp_next_num, res_ground[next_r][next_c] = res_ground[next_r][next_c], temp_next_num
                now_r, now_c = next_r, next_c

    return res_ground


def play(idxs):
    global ground, answer, min_num
    res_ground = copy.deepcopy(ground)
    for idx in idxs:
        r, c, s = commands[idx]
        res_ground = rotate(res_ground, r, c, s)

    temp_min_num = min(list(map(lambda x: sum(x), res_ground)))
    if temp_min_num < min_num:
        min_num = temp_min_num


N, M, K = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
commands = []

for _ in range(K):
    r, c, s = map(int, input().split())
    commands.append((r-1, c-1, s))

min_num = 1e9

for idxs in itertools.permutations(range(K), K):
    play(idxs)

print(min_num)
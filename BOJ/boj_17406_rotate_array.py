import sys
sys.stdin = open('../input.txt', 'r')
import itertools
import copy

def rotate(ground, r, c, s):
    pass


def play(idxs):
    global ground, answer
    temp_ground = copy.deepcopy(ground)
    for idx in idxs:
        r, c, s = commands[idx]
        temp_ground = rotate(temp_ground, r, c, s)

    res_min = min(list(map(lambda x: sum(x), temp_ground)))
    if res_min < answer:
        answer = res_min


N, M, K = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
commands = []

for _ in range(K):
    r, c, s = map(int, input().split())
    commands.append((r-1, c-1, s))

origin_sum_list = list(map(lambda x: sum(x), ground))
answer = min(origin_sum_list)

for idxs in itertools.permutations(range(K), K):
    play(idxs)

print(answer)
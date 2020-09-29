import sys
sys.stdin = open('../input.txt', 'r')

import itertools

def power_diff(starts, links):
    global min_power_diff
    start_power, link_power = 0, 0
    for cand in itertools.combinations(starts, 2):
        first_p, second_p = cand
        start_power += (powers[first_p][second_p] + powers[second_p][first_p])

    for cand in itertools.combinations(links, 2):
        first_p, second_p = cand
        link_power += (powers[first_p][second_p] + powers[second_p][first_p])

    min_power_diff = min(min_power_diff, abs(start_power-link_power))


N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]
min_power_diff = 1e9

for i in range(1 << N):
    starts, links = [], []
    for j in range(N):
        if i & 1 << j:
            starts.append(j)
        else:
            links.append(j)
    if len(starts) == N // 2:
        power_diff(starts, links)
print(min_power_diff)
import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

import itertools


def get_chicken_dist(chicken_idxs):
    global min_chicken_dist
    total_chicken_dist = 0

    for house_r, house_c in houses:
        min_house_to_chicken = 1e9
        for idx in chicken_idxs:
            chicken_r, chicken_c = chickens[idx]
            house_to_chicken = abs(house_r - chicken_r) + abs(house_c - chicken_c)
            min_house_to_chicken = min(min_house_to_chicken, house_to_chicken)
        total_chicken_dist += min_house_to_chicken


    min_chicken_dist = min(min_chicken_dist, total_chicken_dist)

N, M = map(int, input().split())
chickens = []
houses = []

min_chicken_dist = 1e9
for r in range(N):
    line = list(map(int, input().split()))
    for c in range(N):
        if line[c] == 1:
            houses.append((r, c))
        elif line[c] == 2:
            chickens.append((r, c))


for chicken_idxs in itertools.combinations(range(len(chickens)), M):
    get_chicken_dist(chicken_idxs)

print(min_chicken_dist)
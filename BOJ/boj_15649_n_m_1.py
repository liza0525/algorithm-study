import sys
sys.stdin = open('../input.txt', 'r')

from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

for permu in permutations(range(1, N+1), M):
    print(' '.join(map(str, permu)))
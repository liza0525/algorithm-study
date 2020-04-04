import sys
sys.stdin = open('../input.txt', 'r')

N, M = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(M)]

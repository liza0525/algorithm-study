import sys
sys.stdin = open('../input.txt', 'r')

M, N, H = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
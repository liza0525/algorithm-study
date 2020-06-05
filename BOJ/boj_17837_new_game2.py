import sys
sys.stdin = open('../input.txt', 'r')

N, K = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(K)]
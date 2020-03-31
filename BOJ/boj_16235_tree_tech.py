import sys
sys.stdin = open('../input.txt', 'r')

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
tinfo = [list(map(int, input().split())) for _ in range(M)]
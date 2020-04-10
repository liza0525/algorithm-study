import sys
sys.stdin = open('../input.txt', 'r')

N, M, X = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
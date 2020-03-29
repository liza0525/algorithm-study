import sys
sys.stdin = open('../input.txt', 'r')

N, M, x, y, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
move_dir = list(map(int, input().split()))
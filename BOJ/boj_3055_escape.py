import sys
sys.stdin = open('../input.txt', 'r')

R, C = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(R)]
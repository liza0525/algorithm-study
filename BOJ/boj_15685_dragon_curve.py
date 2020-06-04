import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
g = [list(map(int, input())) for _ in range(N)]
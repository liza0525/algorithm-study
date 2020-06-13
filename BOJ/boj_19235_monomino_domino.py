import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
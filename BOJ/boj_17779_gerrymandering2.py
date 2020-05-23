import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
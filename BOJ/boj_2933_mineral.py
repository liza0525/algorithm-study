import sys
sys.stdin = open('../input.txt', 'r')

R, C = map(int, input().split())
g = [list(input()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))
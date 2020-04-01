import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())
M, N, K = map(int, input().split())

for test in range(T):
    X, Y = map(int, input().split())
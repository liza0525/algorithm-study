import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())
for test in range(T):
    L = int(input())
    si, sj = map(int, input().split())
    ti, tj = map(int, input().split())
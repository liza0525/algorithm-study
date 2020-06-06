import sys
sys.stdin = open('../input.txt', 'r')

while True:
    N = int(input())
    if N == 0:
        break
    g = [list(map(int, input().split())) for _ in range(N)]
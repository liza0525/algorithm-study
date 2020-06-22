import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    print(A+B)
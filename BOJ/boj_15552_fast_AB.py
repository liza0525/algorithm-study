import sys
sys.stdin = open('../input.txt', 'r')

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
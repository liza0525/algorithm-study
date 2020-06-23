import sys
sys.stdin = open('../input.txt', 'r')

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    print(A+B)
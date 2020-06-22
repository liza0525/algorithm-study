import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())

for case in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{case+1}: {A} + {B} = {A+B}')
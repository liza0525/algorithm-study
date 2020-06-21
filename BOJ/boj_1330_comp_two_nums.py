import sys
sys.stdin = open('../input.txt', 'r')

N, M = map(int, input().split())

if N < M :
    print('<')
elif N == M:
    print('==')
elif N > M:
    print('>')
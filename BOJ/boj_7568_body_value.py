import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())
res = []
for _ in range(T):
    x, y = map(int, input().split())

print(res, end=' ')
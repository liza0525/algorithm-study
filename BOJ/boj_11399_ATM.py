import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
wd = list(map(int, input().split()))
wd.sort()
res = 0
for i in range(N):
    res += wd[i] * (N-i)
print(res)
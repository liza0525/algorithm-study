import sys
sys.stdin = open('../input.txt', 'r')

N, X = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    if num < X:
        print(num, end=' ')
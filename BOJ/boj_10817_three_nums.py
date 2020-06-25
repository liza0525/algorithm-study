import sys
sys.stdin = open('../input.txt', 'r')

nums = list(map(int, input().split()))

print(sorted(nums)[1])
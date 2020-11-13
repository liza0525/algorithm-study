import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

min_num, max_num = 1000000, -1000000

for number in numbers:
    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number

print(min_num, max_num)
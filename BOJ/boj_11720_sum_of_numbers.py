import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())
numbers = input()
total_number = 0
for number in numbers:
    total_number += int(number)
print(total_number)
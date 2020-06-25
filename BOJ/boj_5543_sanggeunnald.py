import sys
sys.stdin = open('../input.txt', 'r')

burger, beverage = 2001, 2001

for _ in range(3):
    tmp = int(input())
    if tmp < burger:
        burger = tmp

for _ in range(2):
    tmp = int(input())
    if tmp < beverage:
        beverage = tmp

print(burger + beverage - 50)
import sys
sys.stdin = open('../input.txt', 'r')


def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num-1)

N = int(input())
print(factorial(N))
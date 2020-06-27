import sys
sys.stdin = open('../input.txt', 'r')


def fibonacci(d):
    if d == 0:
        return 0
    elif d == 1:
        return 1
    elif d == 2:
        return 1
    else:
        return fibonacci(d-1) + fibonacci(d-2)


N = int(input())
print(fibonacci(N))
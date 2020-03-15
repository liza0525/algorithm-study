import sys
sys.stdin = open('../input.txt', 'r')

for test in range(int(input())):
    P = int(input())
    factors = list(map(int, input().split()))
    factors.sort()
    fl = len(factors)
    if fl % 2 == 0:
        res = factors[0] * factors[-1]
    else:
        res = (factors[fl//2]) ** 2

    print('#{} {}'.format(test+1, res))
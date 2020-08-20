# SWEA 10505 소득불균형

import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())
for test_case in range(T):
    N = int(input())
    incomes = list(map(int, input().split()))
    answer = 0

    avg = sum(incomes) / N

    for income in incomes:
        if income <= avg:
            answer += 1

    print('#{} {}'.format(test_case+1, answer))
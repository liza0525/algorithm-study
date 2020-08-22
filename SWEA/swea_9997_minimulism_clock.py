# swea 9997 미니멀리즘 시계

import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())
for test_case in range(T):
    degree = int(input())

    hour = degree // 30
    minute = int((degree - (30 * hour)) / 0.5)

    print(hour, minute)
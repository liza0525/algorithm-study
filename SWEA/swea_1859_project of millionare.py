# swea 1859번 백만장자 프로젝트
import sys
sys.stdin = open('../input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    answer = 0

    while prices:
        max_price_idx = prices.index(max(prices))
        for i in range(max_price_idx):
            answer += prices[max_price_idx+1] - prices[i]

        prices = prices[max_price_idx+1:]



    print('#{} {}'.format(test_case, answer))
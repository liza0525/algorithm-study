import sys
sys.stdin = open('../input.txt', 'r')



# 재귀 이용(468ms)
def calculate(num, d):
    global min_cnt
    if num == 1:
        min_cnt = min(min_cnt, d)
    else:
        if d < min_cnt:
            if num % 3 == 0:
                calculate(num // 3, d+1)
            if num % 2 == 0:
                calculate(num // 2, d+1)
            calculate(num-1, d+1)


N = int(input())
min_cnt = 1e9

calculate(N, 0)

print(min_cnt)
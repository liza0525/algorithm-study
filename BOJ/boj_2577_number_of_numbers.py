import sys
sys.stdin = open('../input.txt', 'r')

A = int(input())
B = int(input())
C = int(input())

number_cnt = [0 for _ in range(10)]
result_num = str(A * B * C)

for number in result_num:
    number_cnt[int(number)] += 1

print('\n'.join(map(str, number_cnt)))
# 문제 제목 : 숫자 골라내기
import sys
sys.stdin = open('../input.txt', 'r')

inf = sys.stdin

T = int(inf.readline())

for test_case in range(T):
    answer = 0
    N = int(inf.readline())
    num_list = list(map(int, inf.readline().split()))
    num_dict = dict()

    for num in num_list:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    for k, v in num_dict.items():
        if v % 2 == 1:
            answer ^= k

    print('Case #{}'.format(test_case+1))
    print(answer)
inf.close()
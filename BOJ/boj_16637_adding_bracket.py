import sys
sys.stdin = open('../input.txt', 'r')

from itertools import combinations

N = int(input())
cal_cnt = 0
cnt = 0
max_res = -1e9
formula = []
for ch in input():
    if ch.isdigit():
        formula.append(int(ch))
    else:
        formula.append(ch)
        cal_cnt += 1

cnt = cal_cnt // 2 if cal_cnt % 2 == 0 else cal_cnt // 2 + 1

for i in range(cnt+1):
    for combi in combinations(range(cal_cnt), i):
        for j in range(len(combi)-1):
            if combi[j]+1 == combi[j+1]: # 연속되는 숫자가 있다면 이 조합은 선택하면 안됨
                break
        else:
            combi = list(map(lambda x: x * 2 + 1, combi))
            res_list = [formula[0]] # 괄호 안의 계산부터 먼저 한 결과를 담는 리스트

            k = 1
            while k < len(formula):
                calc = formula[k]
                second_num = formula[k+1]
                if k in combi:
                    first_num = res_list.pop()
                    if calc == '+':
                        res_list.append(first_num+second_num)
                    elif calc == '-':
                        res_list.append(first_num-second_num)
                    elif calc == '*':
                        res_list.append(first_num*second_num)
                else:
                    res_list.append(calc)
                    res_list.append(second_num)
                k += 2

            res = res_list[0]
            for k in range(1, len(res_list), 2):
                if res_list[k] == '+':
                    res += res_list[k+1]
                elif res_list[k] == '-':
                    res -= res_list[k+1]
                elif res_list[k] == '*':
                    res *= res_list[k+1]
            if res > max_res:
                max_res = res

print(max_res)



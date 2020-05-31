from pprint import pprint
import sys
sys.stdin = open('../input.txt', 'r')


def calc(A, rc_num):
    max_len, new_A = 0, []

    for i in range(rc_num):
        set_Ai = set(A[i])
        if 0 in set_Ai: set_Ai.remove(0)
        if len(set_Ai) * 2 > max_len:
            max_len = len(set_Ai) * 2

    for i in range(rc_num):
        max_num = max(A[i])
        num_dict = dict()
        for num in range(1, max_num+1):
            cnt = A[i].count(num)
            if cnt == 0: continue
            if cnt not in num_dict.keys():
                num_dict.update({cnt: [num]})
            else:
                num_dict[cnt].append(num)
        new_r = []
        for k in sorted(num_dict.keys()):
            for v in sorted(num_dict[k]):
                new_r += [v, k]

        if len(new_r) < max_len:
            new_r += [0] * (max_len - len(new_r))

        new_A.append(new_r[:100])

    return new_A, max_len


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
r_num, c_num = 3, 3
res = 0

while True:
    if r <= r_num and c <= c_num:
        if A[r-1][c-1] == k:
            break
    if r_num >= c_num:
        A, c_num = calc(A, r_num)
    else:
        A, r_num = calc(list(map(list, zip(*A))), c_num)
        A = list(map(list, zip(*A)))
    res += 1

    if res > 100:
        res = -1
        break

print(res)
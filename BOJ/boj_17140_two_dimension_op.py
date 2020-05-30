from pprint import pprint
import sys
sys.stdin = open('../input.txt', 'r')


def R(): # R 연산 -> 끝나고 열이 늘어남
    pass

def C(): # C 연산 -> 끝나고 행이 늘어감
    pass

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
r_num, c_num = 3, 3
res = 0

while A[r-1][c-1] != k:
    if r_num >= c_num:
        R()
    else:
        C()
    pprint(A)
    res += 1
    break

print(res)
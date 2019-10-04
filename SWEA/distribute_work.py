import sys
from pprint import pprint
sys.stdin = open('../inputdata/20190920.txt', 'r')


def dis_work(k):
    global res, max_res
    if res <= max_res:
        return
    if k == n:
        max_res = res
        return

    for i in range(n):
        if not visited[i]:
            if pij[k][i] == 0:
                continue
            else:
                res *= (pij[k][i]/100)
                visited[i] = 1
                dis_work(k+1)
                res /= (pij[k][i]/100)
                visited[i] = 0

for test in range(int(input())):
    n = int(input())
    pij = [list(map(int, input().split())) for _ in range(n)]
    res, max_res = 1, 0
    visited = [0] * n
    dis_work(0)

    print('#{} {}'.format(test+1, format(max_res*100, ".7f")))

import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')

# def isFeild(i, j):
#     return 0 <= i < N and 0 <= j < N

def moving(g):
    pass


N, L = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
res = 0

res += moving(g)
res += moving(list(map(list, zip(*g))))
print(res)
# pprint(list(map(list, zip(*g))))
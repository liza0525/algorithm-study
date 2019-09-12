import sys
sys.stdin = open('exam2.txt', 'r')
from pprint import pprint
#
# def coloring(x1, y1, x2, y2, c):
#     for i in range(x1, x2+1):
#         for j in range(y1, y2+1):
#             if c < g[i][j]:
#                 return 0
#     for i in range(x1, x2+1):
#         for j in range(y1, y2+1):
#             g[i][j] = c
#
# def cntc(g):
#     colorlist = [0] * 11
#     for i in range(n):
#         for j in range(m):
#             colorlist[g[i][j]] += 1
#     return colorlist
#
# for test in range(int(input())):
#     n, m, k = map(int, input().split())
#     g = [[0] * m for _ in range(n)]
#     info = [list(map(int,input().split())) for _ in range(k)] # x1 y1 x2 y2 c
#     for a in range(k):
#         coloring(*info[a])
#
#     print('#{} {}'.format(test+1, max(cntc(g))))

def isSorted(cards):
    for i in range(len(cards)-1):
        if cards[i] > cards[i+1]:
            print('not Sorted')
            return 0

def shuffle(cards):
    if

for test in range(int(input())):
    n = int(input())
    cards = list(map(int, input().split()))
    isSorted(cards)
    # print('#{}'.format(test+1))
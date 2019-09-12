import sys
from pprint import pprint
sys.stdin = open('magnetic.txt', 'r')

# for test in range(10):
#     n = int(input())
#     g = [list(map(int,input().split())) for _ in range(n)]

#     for j in range(n):
#         for i in range(n-1):
#             if g[i][j] == 1 and not g[i+1][j]:
#                 g[i+1][j], g[i][j] = g[i][j], 0 

#     cnt = 0
#     for j in range(n):
#         for i in range(n-1):
#             if g[i][j] == 1 and g[i+1][j] == 2:
#                 cnt += 1

#     print('#{} {}'.format(test+1, cnt))

# for x in range(1,11):N=int(input());m=[list(map(int,input().split())) for i in range(N)];m=[[m[i][j] for i in range(N) if m[i][j]] for j in range(N)];m=[[1 for i in range(1,len(j)) if j[i-1]==1 and j[i]==2] for j in m];print("#%d %d"%(x,sum(sum(m,[]))))
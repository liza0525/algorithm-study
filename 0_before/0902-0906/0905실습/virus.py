import sys
from pprint import pprint
sys.stdin = open('virus.txt', 'r')

n = int(input())
visit = [0] * (n+1)
g = [[0] * (n+1) for _ in range(n+1)]
e = int(input())

for _ in range(e):
    v1, v2 = map(int, input().split())
    g[v1][v2] , g[v2][v1] = 1, 1

stack = []
stack.append(1)

while stack:
    v = stack.pop()
    if not visit[v]:
        visit[v] = 1
        for i in range(n+1):
            if g[v][i] and not visit[i]:
                stack.append(i)

print(visit.count(1) - 1)
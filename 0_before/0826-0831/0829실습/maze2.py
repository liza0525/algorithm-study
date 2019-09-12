import sys
sys.stdin = open('maze2.txt','r')
from pprint import pprint

dx = [0, 0, -1, 1] # 상하좌우
dy = [-1, 1, 0, 0]

def dfsr(x,y):
    global cnt
    global found
    if not 0 <= x < n or not 0 <= y < n or found or maze[x][y] == '1': return
    if maze[x][y] == '3': found = 1; return cnt

    if maze[x][y] == '0':
        cnt += 1
    maze[x][y] = '1'
    dfsr(x,y+1)
    dfsr(x,y-1)
    dfsr(x+1,y)
    dfsr(x-1,y)

for test in range(int(input())):
    n = int(input())
    maze = []
    for i in range(n):
        row = input()
        maze.append([ch for ch in row])
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                stx, sty = i, j
    found = 0
    cnt = 0
    dfsr(stx,sty)
    pprint(maze)
    print(cnt)
    print(found)
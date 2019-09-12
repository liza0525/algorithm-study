import sys
sys.stdin = open('node.txt','r')



def bfs(start):
    for info in infos:
        global cnt
        if info[1] == end:
            break
        if info[0] == start:
            cnt += 1
            bfs(info[0])

for test in range(int(input())):
    v, e = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(e)]
    start, end = map(int, input().split())
    cnt = 0
    bfs(start)
    print('#{}'.format(test+1))
import sys
sys.stdin = open('input.txt', 'r')

d = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def isField(i, j):
    return 0 <= i < N and 0 <= j < N


def tour(i, j, num):
    global store, visited, max_res
    if num == 3 and i + d[3][0] == si and j + d[3][1] == sj:
        if len(visited) > max_res:
            max_res = len(visited)
    else:
        di, dj = d[num]
        if isField(i+di, j+dj) and g[i+di][j+dj] not in store and (i+di, j+dj) not in visited:
            store.append(g[i+di][j+dj])
            visited.append((i+di, j+dj))
            tour(i+di, j+dj, num)
            if num != 3:
                tour(i+di, j+dj, num+1)
            store.pop()
            visited.pop()


for test in range(int(input())):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    max_res = 0

    for i in range(N-1):
        for j in range(N-1):
            store = [(g[i][j])]
            visited = [(i, j)]
            si, sj = i, j
            tour(i, j, 0)
    if max_res == 0:
        max_res = -1
    print('#{} {}'.format(test+1, max_res))
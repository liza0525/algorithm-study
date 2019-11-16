import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solve(cell):
    global cell_set
    for di, dj in d:
        ni = cell[0] + di
        nj = cell[1] + dj
        if not visited[ni][nj]:
            cell_set[cell[2]].append([ni, nj, cell[2], cell[2], 0])
            visited[ni][nj] = 1


for test in range(int(input())):
    N, M, K = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]
    cell_set = [[] for _ in range(11)]
    visited = [[0] * 350 for _ in range(350)]

    for i in range(N):
        for j in range(M):
            if g[i][j] != 0:
                cell_set[g[i][j]].append([i+151, j+151, g[i][j], g[i][j], 0]) # 세포 i, 세포 j, 세포 생명력, 세포 시간, 비활성/활성/죽음
                visited[i+151][j+151] = 1
                # 세포 생명력, 세포 시간, 비활성/활성/소멸(0/1/2)

    while K:
        K -= 1
        for size in range(10, 0, -1):
            dead = []
            for i in range(len(cell_set[size])):
                cell = cell_set[size][i]

                # if cell[4] == 0:
                #     cell[3] -= 1
                #     if cell[3] == 0:
                #         cell[4] = 1
                #         cell[3] = cell[2]
                # elif cell[4] == 1:
                #     solve(cell)
                #     cell[3] -= 1
                #     if cell[3] == 0:
                #         cell[4] = 2
                #         dead.append(cell)
                # elif cell[4] == 2:
                #     continue

                if cell[4] == 2:
                    continue
                cell[3] -= 1
                if cell[4] == 1:
                    solve(cell)
                if cell[3] == 0: # 세포 시간이 0이 된 경우 상태 바꿔줘야 함
                    if cell[4] == 0:  # 상태가 비활성일 때
                        cell[3] = cell[2]
                        cell[4] = 1  # 활성으로
                    elif cell[4] == 1:  # 상태가 활성일 때
                        dead.append(cell)
                        cell[4] = 2  # 죽음

            for cell in dead:
                cell_set[size].remove(cell)
    res = len(sum(cell_set, []))

    print('#{} {}'.format(test+1, res))
import sys
sys.stdin = open("../inputdata/swea_5189.txt", "r")


def addEnergy(start, d, total):
    if d == n-1:
        total += energies[start][0]
        res_list.append(total)
    else:
        for i in range(1, n):
            if not visited[i]:
                total += energies[start][i]
                visited[i] = 1
                addEnergy(i, d+1, total)
                visited[i] = 0
                total -= energies[start][i]


for test in range(int(input())):
    n = int(input())
    energies = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    res_list = []

    addEnergy(0, 0, 0)

    print('#{} {}'.format(test+1, min(res_list)))
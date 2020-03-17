import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(i, j, di, dj):
    cnt = 0
    while g[i+di][j+dj] != '#' and g[i][j] != 'O':
        i, j = i+di, j+dj
        cnt += 1
    return i, j, cnt


def play(ri, rj, bi, bj, d):
    queue = [(ri, rj, bi, bj, d)]
    visited.append((ri, rj, bi, bj))

    while queue:
        sri, srj, sbi, sbj, sd = queue.pop(0)
        if sd > 10:
            return -1
        for di, dj in ds:
            nri, nrj, rcnt = move(sri, srj, di, dj)
            nbi, nbj, bcnt = move(sbi, sbj, di, dj)
            if g[nbi][nbj] != 'O':
                if g[nri][nrj] == 'O':
                    return sd
                if nri == nbi and nrj == nbj:
                    if rcnt > bcnt:
                        nri -= di
                        nrj -= dj
                    else:
                        nbi -= di
                        nbj -= dj
                if (nri, nrj, nbi, nbj) not in visited:
                    visited.append((nri, nrj, nbi, nbj))
                    queue.append((nri, nrj, nbi, nbj, sd+1))
    return -1


N, M = map(int, input().split())
g = [list(input()) for _ in range(N)]
visited = []

for i in range(N):
    for j in range(M):
        if g[i][j] == 'R':
            ri, rj = i, j
        if g[i][j] == 'B':
            bi, bj = i, j

res = play(ri, rj, bi, bj, 1)


print(res)
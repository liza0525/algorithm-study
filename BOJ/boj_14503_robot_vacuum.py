md = [(0, -1), (-1, 0), (0, 1), (1, 0)]
back = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def l_rotate(d):
    return 3 if d == 0 else d-1

N, M = map(int, input().split())
i, j, d = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
res = 0
toggle = False
while not toggle:
    if g[i][j] == 0:
        g[i][j] = 2
        res += 1

    for idx in range(d, d-4, -1):
        d = l_rotate(d)
        ni, nj = i + md[idx][0], j + md[idx][1]
        if g[ni][nj] == 0:
            i, j = ni, nj
            break
    else:
        ni, nj = i + back[d][0], j + back[d][1]
        if g[ni][nj] == 2:
            i, j = ni, nj
        else:
            toggle = True

print(res)
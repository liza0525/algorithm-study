def moving(g):
    bridge = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        j = 0
        while j < N-1:
            if g[i][j] == g[i][j+1]:
                j += 1
            elif g[i][j] + 1 == g[i][j+1]:
                if sum(bridge[i][j-L+1:j+1]) == 0 and g[i][j-L+1:j+1].count(g[i][j]) == L:
                    bridge[i][j-L+1:j+1] = [1] * L
                    j += 1
                else:
                    break
            elif g[i][j] - 1 == g[i][j+1]:
                if g[i][j+1:j+L+1].count(g[i][j+1]) == L:
                    bridge[i][j+1:j+L+1] = [1] * L
                    j += L
                else:
                    break
            else:
                break
        if j == N-1:
            cnt += 1
    return cnt

N, L = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
res = 0
res += moving(g)
res += moving(list(map(list, zip(*g))))
print(res)
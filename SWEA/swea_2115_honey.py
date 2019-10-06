def choose(pots):
    tmp_max_res = 0
    for x in range(1 << m):
        tmp = 0
        tmp_res = 0
        for y in range(m):
            if x & (1 << y) and tmp + pots[y] <= c:
                tmp += pots[y]
                tmp_res += (pots[y] ** 2)
                if tmp_res > tmp_max_res:
                    tmp_max_res = tmp_res
    return tmp_max_res

for test in range(int(input())):
    n, m, c = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    a, b = [], []
    answer = 0

    for i in range(n):
        visited = []
        for j in range(n-m+1):
            for k in range(m):
                visited.append((i, j+k))
            a = g[i][j:j+m]

            for p in range(n):
                for q in range(n-m+1):
                    for r in range(m):
                        if (p, q+r) in visited:
                            break
                    else:
                        b = g[p][q:q+m]
                        if choose(a)+choose(b) > answer:
                            answer = choose(a)+choose(b)

    print('#{} {}'.format(test+1, answer))
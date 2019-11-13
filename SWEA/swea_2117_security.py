for test in range(int(input())):
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    houses = []
    res_house = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                houses.append((i, j))

    for i in range(n):
        for j in range(n):
            k = 1
            while k < n + n:
                temp = 0
                cost = k ** 2 + (k - 1) ** 2
                for hi, hj in houses:
                    if abs(hi - i) + abs(hj - j) <= k - 1:
                        temp += 1
                if temp * m >= cost and temp > res_house:
                    res_house = temp
                k += 1
    
    print('#{} {}'.format(test+1, res_house))
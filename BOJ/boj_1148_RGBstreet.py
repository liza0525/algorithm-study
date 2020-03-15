N = int(input())
cp = [list(map(int, input().split())) for _ in range(N)] # 집 별 색깔 별 가격
price = [cp[0]] + [[0 ,0, 0] for _ in range(N-1)]

for i in range(1, N):
    for j in range(3):
        cand = []
        for k in range(3):
            if j != k:
                cand.append(price[i-1][k])
        price[i][j] = cp[i][j] + min(cand)

print(min(price[N-1]))
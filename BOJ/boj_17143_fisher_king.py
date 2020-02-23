def moving(r, c, s, d, z):
    if d == 1 or d == 2:
        division = 2*R
    elif d == 3 or d == 4:
        division = 2*C

    if d == 1: # 위
        r = (r-s) % division
        if r >= R and r < division:
            r = division - r
            d = 2
    elif d == 2: #아래
        r = (r+s) % division
        if r >= R and r < division:
            r = 2*R - r
            d = 1
    elif d == 3: #오른쪽
        c = (c+s) % division
        if c >= C and c < division:
            c = 2*C - c
            d = 4
    elif d == 4: #왼쪽
        c = (c-s) % division
        if c >= C and c < division:
            c = division - c
            d = 3
    return [r, c, s, d, z]

R, C, M = map(int, input().split()) # R : 깊이 C: 넓이
sharks = dict()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1, c-1)] = [s, d, z]
R, C = R-1, C-1
total = 0 # 잡은 상어의 크기의 합

for px in range(C+1):
    # 낚시
    for depth in range(R+1):
        if (depth, px) in sharks.keys():
            total += sharks[(depth, px)][2]
            del sharks[(depth, px)]
            break
    # 상어 이동 및 잡아먹기
    temp = dict()
    for shark in sharks:
        r, c = shark[0], shark[1]
        s, d, z = sharks[(r, c)]
        r2, c2, s2, d2, z2 = moving(r, c, s, d, z)
        if (r2, c2) not in temp.keys():
            temp[(r2, c2)] = [s2, d2, z2]
        else:
            if temp[(r2, c2)][2] < z2:
                temp[(r2, c2)] = [s2, d2, z2]
    sharks = temp

print(total)
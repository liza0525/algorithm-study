def blocklist(r1, c1, r2, c2):
    res = []
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            res.append([i,j])
    return res

t = int(input())
for tc in range(t):
    info = []
    red = []
    blue = []
    cnt = 0
    n = int(input())

    for i in range(n):
        info.append(list(map(int, input().split())))

    for i in range(n):
        if info[i][4] == 1:
            red += blocklist(info[i][0], info[i][1], info[i][2], info[i][3])
        else:
            blue += blocklist(info[i][0], info[i][1], info[i][2], info[i][3])

    for i in range(len(red)):
        if red[i] in blue:
            cnt += 1

    print('#{} {}'.format(tc+1,cnt))
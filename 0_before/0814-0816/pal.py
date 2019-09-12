def palidrome(chs):
    for row in chs:
        for fch in range(n-m+1):
            for i in range(int(m/2)):
                if row[fch+i] != row[fch+m-i-1]:
                    break
            else:
                return row[fch:fch+m]
    return []

for test in range(int(input())):
    n, m = map(int, input().split())
    chs = []
    count = 0
    for i in range(n):
        tmp = []
        for j in input():
            tmp.append(j)
        chs.append(tmp)
    if palidrome(chs):
        print('#{} {}'.format(test+1, ''.join(map(str, palidrome(chs)))))
    elif palidrome(list(zip(*chs))):
        print('#{} {}'.format(test+1, ''.join(map(str, palidrome(list(zip(*chs)))))))
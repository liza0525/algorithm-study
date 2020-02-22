def play1(g):
    for i in range(n):
        tmp = []
        for j in range(n):
            if g[i][j] != 0:
                tmp.append(g[i][j])
        j = 0
        while j < len(tmp) - 1:
            if tmp[j] == tmp[j + 1]:
                tmp[j] *= 2
                tmp.pop(j + 1)
            j += 1
        for j in range(len(tmp)):
            res[i][j] = tmp[j]


def play2(g):
    for i in range(n):
        tmp = []
        for j in range(n - 1, -1, -1):
            if g[i][j] != 0:
                tmp.append(g[i][j])
        j = 0
        while j < len(tmp) - 1:
            if tmp[j] == tmp[j + 1]:
                tmp[j] *= 2
                tmp.pop(j + 1)
            j += 1
        for j in range(len(tmp) - 1, -1, -1):
            res[i][j] = tmp[j]
    for i in range(n):
        res[i].reverse()


for test in range(int(input())):
    n, s = input().split()
    n = int(n)
    g = [list(map(int, input().split())) for _ in range(n)]
    res = [[0] * n for _ in range(n)]

    if s == 'left':
        play1(g)
    elif s == 'up':
        play1(list(map(list, zip(*g))))
        res = list(map(list, zip(*res)))
    if s == 'right':
        play2(g)
    elif s == 'down':
        play2(list(map(list, zip(*g))))
        res = list(map(list, zip(*res)))

    print('#{}'.format(test + 1))
    for i in range(n):
        print(' '.join(map(str, res[i])))
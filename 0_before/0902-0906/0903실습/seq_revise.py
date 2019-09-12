for test in range(int(input())):
    n, m, l = map(int, input().split())
    numlist = list(map(str, input().split()))
    infos = [list(map(str, input().split())) for _ in range(m)]

    for info in infos:
        if info[0] == 'I':
            numlist.insert(int(info[1]), info[2])
        elif info[0] == 'D':
            numlist.remove(numlist[int(info[1])])
        elif info[0] == 'C':
            numlist[int(info[1])] = info[2]

    if l > len(numlist)-1:
        print('#{} -1'.format(test+1))
    else:
        print('#{} {}'.format(test+1, numlist[l]))
for tc in range(10):
    tc_num = int(input())
    num_set = []
    sum_set = []
    for i in range(100):
        num_set.append(list(map(int,input().split())))
    
    for i in range(len(num_set)):
        sumnum = 0
        for j in range(len(num_set)):
            sumnum += num_set[i][j]
        sum_set.append(sumnum)
    
    for i in range(len(num_set)):
        sumnum = 0
        for j in range(len(num_set)):
            sumnum += num_set[j][i]
        sum_set.append(sumnum)

    sumnum = 0
    for i in range(len(num_set)):
        sumnum += num_set[i][i]
    sum_set.append(sumnum)

    sumnum = 0
    for i in range(len(num_set)):
        sumnum += num_set[i][len(num_set)-i-1]
    sum_set.append(sumnum)
    maxv = sum_set[0]

    for comp in sum_set:
        if comp > maxv:
            maxv = comp
    print('#{} {}'.format(tc+1, maxv))

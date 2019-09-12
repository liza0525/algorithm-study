for test in range(int(input())):
    n, m, l = map(int, input().split())
    numlist = list(map(int,input().split()))

    for i in range(m):
        a, b = map(int, input().split())
        numlist.insert(a, b)

    print('#{} {}'.format(test+1, numlist[l]))
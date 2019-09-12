def addnums(nums, n, m):
    adds = []
    for i in range(n-m+1):
        sumnum = 0
        for j in range(i, i+m):
            sumnum += nums[j]
        adds.append(sumnum)

    maxaddnum, minaddnum = adds[0], adds[0]
    
    for tmp in adds:
        if tmp > maxaddnum:
            maxaddnum = tmp
        if tmp < minaddnum:
            minaddnum = tmp
            
    return maxaddnum - minaddnum


for test in range(int(input())):
    n, m = list(map(int, input().split()))
    nums = list(map(int,input().split()))

        
    print('#{} {}'.format(test+1, addnums(nums, n, m)))

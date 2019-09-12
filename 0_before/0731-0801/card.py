for test in range(int(input())):
    cardnum = int(input())
    nums = input()
    cnt = [0 for i in range(10)]
    for ch in nums:
        cnt[int(ch)] += 1

    maxnum = 0
    maxnum_idx = 0

    for i in range(len(cnt), 0, -1):
        if cnt[i-1] > maxnum:
            maxnum = cnt[i-1]
            maxnum_idx = i-1
            
    print('#{} {} {} '.format(test+1, maxnum_idx,maxnum))

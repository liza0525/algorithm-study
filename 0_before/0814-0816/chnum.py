for test in range(int(input())):
    str1 = input()
    str2= input()
    chlist = []
    chnum = dict()
    for ch in str1:
        if ch not in chlist:
            chlist.append(ch)

    for ch in str2:
        if ch in chlist:
            if ch not in chnum.keys():
                chnum.update({ch:1})
            else:
                chnum[ch] += 1
    
    maxnum = chnum[chlist[0]]
    for i in chlist:
        if chnum[i] > maxnum:
            maxnum = chnum[i]

    print('#{} {}'.format(test+1, maxnum))
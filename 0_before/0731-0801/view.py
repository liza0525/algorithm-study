
for test in range(10):
    case_len = int(input())
    bd = list(map(int, input().split()))
    cnt = 0
    for i in range(2, len(bd)-2):
        maxbd = 0
        for n in [-2,-1,1,2]:
            if bd[i] <= bd[i+n]:
                break
            else:
                if bd[i+n] > maxbd:
                    maxbd = bd[i+n]
                if n == 2:
                    cnt += (bd[i]-maxbd)
    print('#{} {}'.format(test+1, cnt))
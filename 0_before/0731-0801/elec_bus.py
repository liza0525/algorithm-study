for test in range(int(input())):
    k, n, m = list(map(int, input().split()))
    stops = list(map(int, input().split()))
    charges = 0
    nowstop = 0
    idx = 0
    while idx < len(stops)-1:
        if nowstop >= n:
            break
        if stops[idx+1] - stops[idx] > k:
            charges = 0
            break
        else:
            for dis in range(k,0,-1):
                if nowstop+dis == n:
                    nowstop = n
                    break
                elif nowstop + dis in stops:
                    nowstop += dis
                    charges += 1
                    idx = stops.index(nowstop)
                    break

    print('#{} {}'.format(test+1, charges))

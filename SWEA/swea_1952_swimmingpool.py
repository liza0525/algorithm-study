for test in range(int(input())):
    fees = list(map(int, input().split()))
    days = list(map(int, input().split()))
    monthly_budgets = [0] * 12
    month3_fee = 0

    for i in range(12):
        if days[i]*fees[0] > fees[1]:
            monthly_budgets[i] = fees[1]
        else:
            monthly_budgets[i] = days[i]*fees[0]

    for i in range(0, 12, 3):
        if sum(monthly_budgets[i:i+3]) > fees[2]:
            month3_fee += fees[2]
            monthly_budgets[i:i+3] = [0, 0, 0]
        else:
            break

    while monthly_budgets:
        tmp = [0] * 12
        for i in range(12):
            tmp[i] = sum(monthly_budgets[i:i+3])

        if max(tmp) > fees[2]:
            month3_fee += fees[2]
            i = tmp.index(max(tmp))
            for k in range(3):
                if i+k < 12:
                    monthly_budgets[i+k] = 0
                else:
                    break
        else:
            break

    res = sum(monthly_budgets) + month3_fee
    if res > fees[3]:
        res = fees[3]
    print('#{} {}'.format(test+1, res))


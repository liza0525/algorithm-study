import sys
sys.stdin = open("../inputdata/swea_5203.txt", "r")

for test in range(int(input())):
    cards = list(map(int, input().split()))
    p1 = cards[::2]
    p2 = cards[1::2]
    res = 0
    for i in range(2, 6):
        toggle = 0
        tmp1 = p1[:i+1]
        tmp2 = p2[:i+1]
        for j in range(i+1):
            if tmp1.count(tmp1[j]) == 3:
                res = 1
                toggle = 1
                break
            if tmp2.count(tmp1[j]) == 3:
                res = 2
                toggle = 1
                break
            if (tmp1[j]+1) in tmp1 and (tmp1[j]+2) in tmp1:
                res = 1
                toggle = 1
                break
            if (tmp2[j]+1) in tmp2 and (tmp2[j]+2) in tmp2:
                res = 2
                toggle = 1
                break
        if toggle:
            break

    print('#{} {}'.format(test+1, res))
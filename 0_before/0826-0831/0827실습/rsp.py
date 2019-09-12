def win(x, y):
    if (cards[x-1] == 1 and cards[y-1] == 3) or (cards[x-1] == 1 and cards[y-1] == 1):
        return x
    elif (cards[x-1] == 2 and cards[y-1] == 1) or (cards[x-1] == 2 and cards[y-1] == 2):
        return x
    elif (cards[x-1] == 3 and cards[y-1] == 2) or (cards[x-1] == 3 and cards[y-1] == 3):
        return x
    return y

def match(start, end):
    if start == end:
        return start

    fv = match(start, (start+end)//2)
    sv = match((start+end)//2+1, end)
    return win(fv, sv)

for test in range(int(input())):
    n = int(input())
    cards = list(map(int, input().split()))
    start = 1
    end = n
    print('#{} {}'.format(test+1, match(start, end)))
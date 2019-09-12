def paper(n):
    i = int(n/10)
    if i == 1:
        return 1
    elif i == 2:
        return 3
    else:
        return paper(n-10)+paper(n-20) *2

for test in range(int(input())):
    n = int(input())
    print('#{} {}'.format(test+1, paper(n)))

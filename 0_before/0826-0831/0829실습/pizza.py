import sys
sys.stdin = open('pizza.txt','r')

for test in range(int(input())):
    n, m = map(int, input().split())
    pizzas = list(map(int, input().split()))
    idx = [i for i in range(m)]
    oven = []
    oven_i = []

    for i in range(n):
        oven.append(pizzas.pop(0))
        oven_i.append(idx.pop(0))

    while oven.count(0) != n-1:
        for i in range(n):
            oven[i] //= 2
            if oven[i] == 0 and pizzas:
                oven[i] = pizzas.pop(0)
                oven_i[i] = idx.pop(0)
            if oven.count(0) == n-1:
                break
    for i in range(n):
        if oven[i] != 0:
            print('#{} {}'.format(test+1, oven_i[i]+1))
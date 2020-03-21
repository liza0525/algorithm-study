for test in range(int(input())):
    N = int(input())
    jail = [0] * (N+1)
    for i in range(1, N+1):
        num = i
        while num < N+1:
            jail[num] = 1 if not jail[num] else 0
            num += i

    print(sum(jail))
def myCalc(y):
    global tmp, result

    if result < tmp:
        return

    if y == n:
        if tmp < result:
            result = tmp
        return

    for x in range(n):
        if not visited[x]:
            visited[x] = 1
            tmp += nums[y][x]
            myCalc(y+1)
            visited[x] = 0
            tmp -= nums[y][x]

for test in range(int(input())):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    tmp, result = 0, 987654321
    myCalc(0)

    print('#{} {}'.format(test+1, result))
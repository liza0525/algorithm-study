def operating(res, d):
    global max_num, min_num
    if d == len(numbers)-1:
        if res >= max_num:
            max_num = res
        if res <= min_num:
            min_num = res
    else:
        for i in range(len(num_op)):
            if num_op[i]:
                d += 1
                num_op[i] -= 1
                tmp = res
                if i == 0:
                    res += numbers[d]
                elif i == 1:
                    res -= numbers[d]
                elif i == 2:
                    res *= numbers[d]
                elif i == 3:
                    res = int(res / numbers[d])
                operating(res, d)
                d -= 1
                num_op[i] += 1
                res = tmp


for test in range(int(input())):
    n = int(input())
    num_op = list(map(int, input().split())) # 덧셈 뺄셈 곱셈 나눗셈 갯수
    numbers = list(map(int, input().split()))
    operators = []
    max_num = -987654321
    min_num = 987654321

    operating(numbers[0], 0)

    print('#{} {}'.format(test+1, max_num - min_num))
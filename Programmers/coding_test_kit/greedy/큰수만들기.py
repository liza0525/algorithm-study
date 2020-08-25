def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and number[i] > stack[-1] and k:
            stack.pop()
            k -= 1
        if k == 0:
            stack += list(number[i:])
            break
        stack.append(number[i])

    if len(stack) == len(number):
        stack = stack[:-k]
    return ''.join(stack)


# 부분집합 이용(시간초과)

def solution(number, k):
    answer = 0
    numbers = list(number)
    N = len(numbers)

    for i in range(1 << N):
        made_num = ''
        for j in range(N):
            if i & 1 << j:
                made_num += numbers[j]
        if len(made_num) == N - k and int(made_num) > answer:
            answer = int(made_num)

    return str(answer)
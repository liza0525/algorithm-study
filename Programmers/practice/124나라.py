def solution(number):
    from collections import deque
    remainders = deque()
    divider = 3

    while True:
        remainder = number % divider
        remainders.appendleft(remainder)
        number //= divider
        if number < divider:
            if number != 0:
                remainders.appendleft(number)
            break

    digit = 1
    answer = 0
    for i in range(len(remainders)-1, -1, -1):
        if i > 0:
            if remainders[i] == -1:
                remainders[i-1] -= 1
                remainders[i] = 2
            elif remainders[i] == 0:
                remainders[i-1] -= 1
                remainders[i] = 4
        answer += digit * remainders[i]
        digit *= 10

    return str(answer)

for n in range(1, 11):
    print(solution(n))
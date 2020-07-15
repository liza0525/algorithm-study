def solution(arrangement):
    answer = 0
    stack = []
    wood = 0
    isCut = False
    for bracket in arrangement:
        if bracket == ')':
            if isCut:
                wood -= 1
                answer += 1
                stack.pop()
            else:
                wood -= 1
                answer += wood
                stack.pop()
                isCut = True
        else:
            stack.append(bracket)
            wood += 1
            isCut = False
    return answer
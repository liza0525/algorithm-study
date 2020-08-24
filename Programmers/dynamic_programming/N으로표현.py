def solution(N, number):
    nums = [0] * (number+1)
    cals = [[] for _ in range(9)]
    for i in range(1, 9):
        nums[i] = nums[i-1] * 10 + N
        cals[i].append(nums[i])

    for i in range(2, 9):
        for j in range(1, i):
            for n1 in cals[j]:
                for n2 in cals[i-j]:
                    cals[i].append(n1 + n2)
                    cals[i].append(n1 - n2)
                    cals[i].append(n1 * n2)
                    if n2 != 0:
                        cals[i].append(n1 // n2)
        if number in cals[i]:
            return i
    return -1


print(solution(5, 12))
print(solution(2, 11))
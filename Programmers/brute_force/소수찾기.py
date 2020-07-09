from itertools import permutations
import math


def prime_num(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if not num % i:
            return False
    else:
        return True


def solution(numbers):
    answer = 0
    num_list = set()

    for i in range(1, len(numbers) + 1):
        for nums in set(permutations(numbers, i)):
            num_list.add(int(''.join(nums)))

    for num in list(num_list):
        if prime_num(num):
            answer += 1

    return answer
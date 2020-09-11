# 2019 KAKAO BLIND RECRUITMENT
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    foods = [[dish_num, amount] for dish_num, amount in enumerate(food_times)]
    foods = sorted(foods, key=lambda x: x[1])
    n = len(foods)

    pre_amount, i = 0, 0
    while True:
        amount = foods[i][1]
        reduce_amount = (amount - pre_amount) * (n - i)
        if reduce_amount >= k:
            break
        else:
            k -= reduce_amount
            pre_amount, i = amount, i+1
    foods = sorted(foods[i:])
    return foods[k % len(foods)][0] + 1


print(solution([3, 1, 2], 5))
print(solution([3, 2, 1, 2, 3], 10)) # 5
print(solution([1, 2, 3, 4, 5], 20)) # -1
print(solution([9, 1, 4, 2, 5], 16)) # 5
print(solution([1, 2, 3, 4, 5], 10)) # 4
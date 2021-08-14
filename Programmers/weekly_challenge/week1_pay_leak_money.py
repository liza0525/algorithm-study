def solution(price, money, count):
    expected_money = price * ((1 + count) * count) // 2
    return expected_money - money if expected_money - money > 0 else 0


print(solution(3, 20, 4))  # 10

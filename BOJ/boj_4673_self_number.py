is_self_number = [True] * 10001

for number in range(1, 10001):
    number_length = len(str(number))
    next_number = number
    for k in range(number_length, -1, -1):
        divider = 10 ** k
        next_number += number // divider
        number %= divider
    if next_number < 10001:
        is_self_number[next_number] = False


for number in range(1, 10001):
    if is_self_number[number]:
        print(number)
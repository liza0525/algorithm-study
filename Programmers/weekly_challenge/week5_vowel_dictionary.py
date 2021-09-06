def solution(word):
    def get_added_number(n, vowel):
        i = 0
        added_number = 1
        while i < 4 - n:
            added_number = added_number * 5 + 1
            i += 1
        added_number *= vowel_dict[vowel]
        return added_number

    answer = len(word)
    vowel_dict = {
        'E': 1, 'I': 2, 'O': 3, 'U': 4,
    }

    for i, vowel in enumerate(word):
        if vowel == 'A':
            continue
        answer += get_added_number(i, vowel)

    return answer


print(solution("AAAAE"))  # 6
print(solution("AAAE"))  # 10
print(solution("EIO"))  # 1189
print(solution("I"))  # 1563

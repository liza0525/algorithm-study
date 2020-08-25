def solution(answers):
    answer = []
    patterns = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    right_answer = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):
        if answers[i] == patterns[0][i % 5]:
            right_answer[1] += 1
        if answers[i] == patterns[1][i % 8]:
            right_answer[2] += 1
        if answers[i] == patterns[2][i % 10]:
            right_answer[3] += 1

    right_answer = sorted(right_answer.items(), key=lambda x: -x[1])
    person, max_num = right_answer[0]
    answer.append(person)
    for i in range(1, len(right_answer)):
        person, num = right_answer[i]
        if num != max_num:
            break
        answer.append(person)
    return answer
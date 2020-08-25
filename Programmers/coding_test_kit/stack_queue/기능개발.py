import math


def solution(progresses, speeds):
    answer = []
    max_days, works = math.ceil((100 - progresses[0]) / speeds[0]), 1
    for i in range(1, len(progresses)):
        days = math.ceil((100 - progresses[i]) / speeds[i])
        if days <= max_days:
            works += 1
        else:
            answer.append(works)
            max_days = days
            works = 1
    else:
        answer.append(works)

    return answer
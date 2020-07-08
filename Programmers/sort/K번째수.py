# 나중에 정렬 별로 공부할 것(Java, JS, C 대비)

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sliced = array[i-1:j]
        answer.append(sorted(sliced)[k-1])
    return answer
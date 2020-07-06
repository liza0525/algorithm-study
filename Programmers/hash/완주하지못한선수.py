def solution(participant, completion):
    answer = ''
    names = dict()
    for name in participant:
        if name not in names.keys():
            names.update({name: 1})
        else:
            names[name] += 1
    for name in completion:
        names[name] -= 1

    for k, v in names.items():
        if v == 1:
            answer = k
            break

    return answer
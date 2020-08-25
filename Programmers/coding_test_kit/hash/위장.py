def solution(clothes):
    cth_dict = dict()
    for itm, variety in clothes:
        if variety not in cth_dict.keys():
            cth_dict.update({variety: [itm]})
        else:
            cth_dict[variety].append(itm)
    answer = 1
    for k, v in cth_dict.items():
        answer *= (len(v) + 1)

    return answer - 1
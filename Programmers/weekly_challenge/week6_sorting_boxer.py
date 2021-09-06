def solution(weights, head2head):
    def get_win_rate(boxer):
        win_lose = win_lose_list[boxer]
        win_count, lose_count = win_lose.count('W'), win_lose.count('L')
        return win_count / (win_count + lose_count) if win_count + lose_count != 0 else 0

    def get_win_heavier_people_count(boxer):
        boxer_weight = weights[boxer]
        win_lose = win_lose_list[boxer]
        return sum([
            1
            for i, win_char in enumerate(win_lose)
            if win_char == 'W' and boxer_weight < weights[i]
        ])

    win_lose_list = list(map(lambda x: list(x), head2head))
    boxer_cnt = len(weights)

    boxers = [i for i in range(boxer_cnt)]
    boxers = sorted(boxers, key=lambda x: (
        -get_win_rate(x),
        -get_win_heavier_people_count(x),
        -weights[x],
        x
    ))
    return list(map(lambda x: x+1, boxers))


# [3,4,1,2]
print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
# [2,3,1]
print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))
# [2,1,3]
print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))

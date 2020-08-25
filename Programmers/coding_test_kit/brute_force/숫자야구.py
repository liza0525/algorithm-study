# 백준 2503번 문제와 동일

def is_target(tfn, tsn, ttn, baseball):
    for predict_num, strike, ball in baseball:
        predict_strike, predict_ball = 0, 0
        pfn, psn, ptn = str(predict_num)
        if pfn == tfn:
            predict_strike += 1
        if psn == tsn:
            predict_strike += 1
        if ptn == ttn:
            predict_strike += 1

        if pfn == tsn or pfn == ttn:
            predict_ball += 1
        if psn == tfn or psn == ttn:
            predict_ball += 1
        if ptn == tfn or ptn == tsn:
            predict_ball += 1

        if predict_strike != strike or predict_ball != ball:
            return False
    return True


def solution(baseball):
    answer = 0

    for target_num in range(123, 988):
        fn, sn, tn = str(target_num)
        if fn == '0' or sn == '0' or tn == '0':
            continue
        if fn == sn or fn == tn or sn == tn:
            continue
        if not is_target(fn, sn, tn, baseball):
            continue
        else:
            answer += 1

    return answer
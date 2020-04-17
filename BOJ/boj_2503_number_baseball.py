import sys
sys.stdin = open('../input.txt', 'r')


def is_target_num(fn, sn, tn):
    if fn == '0' or sn == '0' or tn == '0':
        return False
    if fn == sn or fn == tn or sn == tn:
        return False

    for i_num, i_strike, i_ball in info:
        strike, ball = 0, 0
        i_fn, i_sn, i_tn = list(str(i_num))

        if fn == i_fn: strike += 1
        if sn == i_sn: strike += 1
        if tn == i_tn: strike += 1

        if fn == i_sn: ball += 1
        if fn == i_tn: ball += 1
        if sn == i_fn: ball += 1
        if sn == i_tn: ball += 1
        if tn == i_fn: ball += 1
        if tn == i_sn: ball += 1

        if strike != i_strike or ball != i_ball:
            return False
    return True


N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
answers = []

for target in range(123, 988):
    fn, sn, tn = list(str(target))

    if not is_target_num(fn, sn, tn):
        continue
    else:
        answers.append(target)

print(len(answers))
import sys
sys.stdin = open('../input.txt', 'r')


def get_time(group, stair):
    dists = []
    stair_r, stair_c, stair_length = stair
    for person_r, person_c in group:
        dists.append(abs(stair_r - person_r) + abs(stair_c - person_c))
    dists.sort()
    if len(dists) <= 3:
        total_time = dists[-1] + stair_length + 1
    else:
        idx = 0
        for idx in range(len(dists)-3):
            if dists[idx + 3] > dists[idx] + stair_length + 1:
                total_time = dists[idx + 3]
                idx += 3
            else:
                total_time = dists[idx + 3] + stair_length - (dists[idx + 3] - dists[idx])
                idx += 3

        total_time = max(total_time + stair_length + 1, dists[-1] + stair_length + 1)

    return total_time


T = int(input())
for test_case in range(T):
    N = int(input())
    people = []
    stairs = []
    ground = [[0 for _ in range(N)] for _ in range(N)]
    min_time = 10001

    for r in range(N):
        line = list(map(int, input().split()))
        for c in range(N):
            ground[r][c] = line[c]
            if line[c] == 1:
                people.append((r, c))
            elif line[c] > 1:
                stairs.append((r, c, line[c]))

    P = len(people)

    for i in range(1 << P):
        a_group, b_group = [], []
        a_group_time, b_group_time = 0, 0
        for j in range(P):
            if i & 1 << j:
                a_group.append(people[j])
            else:
                b_group.append(people[j])

        if a_group:
            a_group_time = get_time(a_group, stairs[0])

        if b_group:
            b_group_time = get_time(b_group, stairs[1])

        batch_max_time = max(a_group_time, b_group_time)
        min_time = min(batch_max_time, min_time)

    print('#{} {}'.format(test_case+1, min_time))
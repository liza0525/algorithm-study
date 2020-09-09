# 2019 KAKAO BLIND RECRUITMENT
def solution(N, stages):
    fail_probs = []

    for now_stage in range(1, N+1):
        arrival = 0 # 스테이지에 들린 사람 수
        stop = 0 # 현재 스테이지에 멈춘 사람 수
        for stage in stages:
            if stage >= now_stage:
                arrival += 1
                if stage == now_stage:
                    stop += 1
        fail_prob = stop / arrival if arrival != 0 else 0
        fail_probs.append([now_stage, fail_prob])

    return list(list(zip(*sorted(fail_probs, key=lambda x:(-x[1], x[0]))))[0])


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))

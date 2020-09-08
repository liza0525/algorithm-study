# 2020 KAKAO BLIND RECRUITMENT
from itertools import permutations

def solution(n, weak, dist):
    rotate_weaks = [weak]

    for _ in range(len(weak)-1): # 시계 방향으로 계속 돈다고 했을 때, 출발점에 따른 변화하는 도착지점 모음
        rotate_weaks.append(rotate_weaks[-1][1:] + [rotate_weaks[-1][0] + n])

    def isPossible(people):
        for rotate_weak in rotate_weaks:
            s_idx = 0 # 현재 사람의 시작 위치
            for person in people:
                for n_idx in range(s_idx+1, len(rotate_weak)):
                    if rotate_weak[n_idx] - rotate_weak[s_idx] > person:
                        s_idx = n_idx
                        break
                else:
                    return True
        return False

    for people_num in range(1, len(dist)+1): # 1~n명까지의 순열을 뽑아본다.
        for people in map(list, permutations(reversed(dist), people_num)): # 순열
            if isPossible(people):
                return people_num
    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print(solution(12, [1, 8, 10], [1, 2, 3]))
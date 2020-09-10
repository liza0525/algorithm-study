# 2019 KAKAO BLIND RECRUITMENT
from itertools import combinations


def solution(relation):
    N = len(relation[0])
    attributes = list(zip(*relation))
    key_idx_set = [] # attributions의 조합으로 이뤄진 키들의 집합(idx)
    answer = 0

    # attribute의 조합이 후보키인지 판별하는 함수
    def is_candidate(key_idxes):
        combi_key = []
        for key_idx in key_idxes:
            combi_key.append(attributes[key_idx])
        combi_key = list(zip(*combi_key))

        return True if len(combi_key) == len(set(combi_key)) else False

    # 해당 attribute을 부분집합으로 하는 모든 set 삭제하기
    def remove_set(first_key_idx):
        a = set(first_key_idx)
        remove_list = []
        for second_key_idx in key_idx_set:
            b = set(second_key_idx)
            if a != b and a.issubset(b):
                remove_list.append(second_key_idx)

        for el in remove_list:
            key_idx_set.remove(el)

    for i in range(1, N+1):
        for combi in combinations(range(0, N), i):
            key_idx_set.append(combi)
    for key_idx in key_idx_set:
        if is_candidate(key_idx):
            answer += 1
            remove_set(key_idx)

    return answer

# 답 2
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

# 답 4
print(solution([[1, 2, 8, 4, 5],
                [1, 3, 5, 7, 10],
                [2, 4, 7, 7, 19],
                [5, 5, 3, 10, 8]]))

# 답 4
print(solution([[1, 1, 1, 1, 1],
                [2, 4, 2, 2, 2],
                [2, 3, 3, 3, 3],
                [4, 4, 4, 4, 4]]))

# 답 1
print(solution([['a', 'aa'],
                ['aa', 'a'],
                ['a', 'a']]))
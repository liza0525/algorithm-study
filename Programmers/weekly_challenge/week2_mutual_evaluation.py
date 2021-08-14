def solution(scores_list):
    def get_score(evaluated_scores):
        total_scores = sum(evaluated_scores) / len(evaluated_scores)
        if total_scores >= 90:
            return 'A'
        elif total_scores >= 80:
            return 'B'
        elif total_scores >= 70:
            return 'C'
        elif total_scores >= 50:
            return 'D'
        else:
            return 'F'

    answer = ''
    student_num = len(scores_list)
    self_evaluate_dict = {}
    for idx in range(student_num):
        self_evaluate_dict[idx] = scores_list[idx][idx]

    scores_list = list(map(list, zip(*scores_list)))

    for idx in range(student_num):
        scores = scores_list[idx]
        self_evaluate = self_evaluate_dict[idx]
        min_score = min(scores)
        max_score = max(scores)
        if scores.count(self_evaluate) == 1:
            if self_evaluate in (min_score, max_score):
                scores.pop(idx)
        answer += get_score(scores)

    return answer


print(solution([
    [100, 90, 98, 88, 65],
    [50, 45, 99, 85, 77],
    [47, 88, 95, 80, 67],
    [61, 57, 100, 80, 65],
    [24, 90, 94, 75, 65]
]))  # FBABD
print(solution([[50, 90], [50, 87]]))  # DA
print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))  # CFD

def solution(budgets, M):
    answer = 0
    left, right = 0, max(budgets)
    while left <= right:
        mid = (left + right) // 2
        total = 0  # 상한액 이하의 예산
        for budget in budgets:
            if budget > mid:
                total += mid
            else:
                total += budget
        if total <= M:
            answer = mid
            left = mid + 1
        elif total > M:
            right = mid - 1

    return answer
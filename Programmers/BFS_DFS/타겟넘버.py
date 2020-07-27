answer = 0
def solution(numbers, target):
    def dfs(idx, res):
        global answer
        if idx == len(numbers):
            if res == target:
                answer +=1
        else:
            dfs(idx+1, res+numbers[idx])
            dfs(idx+1, res-numbers[idx])
    dfs(0, 0)
    return answer
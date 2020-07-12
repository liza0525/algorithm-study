def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    def dfs(start):
        stack = [start]
        visited[start] = 1
        while stack:
            v = stack.pop()
            for next_v in range(n):
                if computers[next_v][v] and not visited[next_v]:
                    stack.append(next_v)
                    visited[next_v] = 1
        return 1

    for i in range(n):
        for j in range(n):
            if computers[i][j] and not visited[i]:
                answer += dfs(i)

    return answer
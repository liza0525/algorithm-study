def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[-1] = triangle[-1]
    for i in range(N-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = max(triangle[i][j] + dp[i+1][j], triangle[i][j] + dp[i+1][j+1])
    return dp[0][0]
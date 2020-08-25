def solution(m, n, puddles):
    paths = [[0 for _ in range(m+1)] for _ in range(n+1)]
    paths[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: continue
            if [j, i] in puddles: continue
            if 0 <= i-1 < n:
                paths[i][j] += paths[i-1][j]
            if 0 <= j-1 < m:
                paths[i][j] += paths[i][j-1]
    print(paths)
    return paths[n][m] % 1000000007

print(solution(5, 5, [[2, 4], [3, 2], [5, 4]]))
def erase(s):
    memo = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if s[i][j] and s[i][j] == s[i][j-1]:
                if s[i][j] not in memo:
                    memo.append((i, j))
                if s[i][j-1] not in memo:
                    memo.append((i, j-1))
            if i < N-1 and s[i][j] and s[i][j] == s[i+1][j]:
                if s[i][j] not in memo:
                    memo.append((i, j))
                if s[i+1][j] not in memo:
                    memo.append((i+1, j))
    if memo:
        for i, j in memo:
            s[i][j] = 0
    else:
        t = N * M - sum(s, []).count(0)
        avg = sum(sum(s, [])) / t if t else 0

        for i in range(N):
            for j in range(M):
                if s[i][j]:
                    if s[i][j] < avg:
                        s[i][j] += 1
                    elif s[i][j] > avg:
                        s[i][j] -= 1


N, M, T = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(N)]
r = [list(map(int, input().split())) for _ in range(T)]

for t in range(T):
    for i in range(N):
        if not (i+1) % r[t][0]:
            if not r[t][1]:
                s[i] = s[i][M-r[t][2]:] + s[i][:M-r[t][2]]
            else:
                s[i] = s[i][r[t][2]:] + s[i][:r[t][2]]
    erase(s)
print(sum(sum(s, [])))
def solution(N):
    sq = [0] * N
    sq[0], sq[1] = 4, 6

    for i in range(2, N):
        sq[i] = sq[i - 1] + sq[i - 2]

    return sq[N - 1]
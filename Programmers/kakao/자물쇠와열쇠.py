# 2020 KAKAO BLIND RECRUITMENT
def solution(key, lock):
    M, N = len(key), len(lock)
    G = 2 * (M - 1) + N
    ground = [[0 for _ in range(G)] for _ in range(G)]
    hole_location = []
    for i in range(N):
        for j in range(N):
            ground[M+i-1][M+j-1] = lock[i][j]
            if not lock[i][j]:
                hole_location.append((M+i-1, M+j-1))


    def rotate(key):
        rotate_key = [[0 for _ in range(M)] for _ in range(M)]
        for i in range(M):
            for j in range(M):
                rotate_key[j][M-i-1] = key[i][j]
        return rotate_key


    def is_fit(sti, stj):
        hole_cnt = 0
        for i in range(M):
            for j in range(M):
                if ground[sti+i][stj+j] * key[i][j]:
                    return False
                elif not ground[sti+i][stj+j] and key[i][j]:
                    if (sti+i, stj+j) in hole_location:
                        hole_cnt += 1
        if hole_cnt == len(hole_location):
            return True
        else:
            return False

    cnt = 0
    while cnt < 4:
        for sti in range(G-M+1):
            for stj in range(G-M+1):
                if is_fit(sti, stj):
                    return True
        cnt += 1
        key = rotate(key)
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
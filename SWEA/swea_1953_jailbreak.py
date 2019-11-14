def isField(i, j):
    return 0 <= i < N and 0 <= j < M


def isNext(si, sj, di, dj):
    if (di, dj) == (-1, 0):
        if g[si+di][sj+dj] in [3, 4, 7]:
            return False
    elif (di, dj) == (1, 0):
        if g[si+di][sj+dj] in [3, 5, 6]:
            return False
    elif (di, dj) == (0, -1):
        if g[si+di][sj+dj] in [2, 6, 7]:
            return False
    elif (di, dj) == (0, 1):
        if g[si+di][sj+dj] in [2, 4, 5]:
            return False
    return True


def tube_direction(num):
    if num == 1:
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    elif num == 2:
        return [(-1, 0), (1, 0)] # 상하
    elif num == 3:
        return [(0, -1), (0, 1)]  # 좌우
    elif num == 4:
        return [(-1, 0), (0, 1)]  # 상우
    elif num == 5:
        return [(1, 0), (0, 1)]  # 하우
    elif num == 6:
        return [(1, 0), (0, -1)]  # 하좌
    elif num == 7:
        return [(-1, 0), (0, -1)]  # 상좌

def bfs(i, j, h):
    visited = [(i, j)]
    queue = [(i, j)]
    h -= 1

    while queue and h:
        temp = queue[:]
        queue = []
        while temp:
            si, sj = temp.pop(0)
            d = tube_direction(g[si][sj])
            for di, dj in d:
                if isField(si+di, sj+dj) and g[si+di][sj+dj] and (si+di, sj+dj) not in visited and isNext(si, sj, di, dj):
                    queue.append((si+di, sj+dj))
                    visited.append((si+di, sj+dj))
        h -= 1

    return len(visited)


for test in range(int(input())):
    N, M, R, C, L = map(int, input().split()) # 터널 세로, 터널 가로, 맨홀 위치(세로), 맨홀 위치(가로), 탈출 후 시간
    g = [list(map(int, input().split())) for _ in range(N)]

    res = bfs(R, C, L)
    print('#{} {}'.format(test+1, res))
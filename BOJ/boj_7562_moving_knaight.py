import sys
sys.stdin = open('../input.txt', 'r')


ds = [(-2, 1), (-1, 2), (1, 2), (2, 1),
      (2, -1), (1, -2), (-1, -2), (-2, -1)
      ] # 나이트 이동 방향


def moving(si, sj):
    queue = [(si, sj)]
    visited = [[0] * L for _ in range(L)]
    visited[si][sj] = 1
    cnt = 0

    if si == ti and sj == tj:
        return cnt

    while queue:
        temp = queue
        queue = []
        while temp:
            i, j = temp.pop()
            for di, dj in ds:
                ni, nj = i+di, j+dj
                if 0 <= ni < L and 0 <= nj < L:
                    if ni == ti and nj == tj:
                        cnt += 1
                        return cnt
                    if not visited[ni][nj]:
                        queue.append((ni, nj))
                        visited[ni][nj] = 1
        cnt += 1


T = int(input())
for test in range(T):
    L = int(input())
    si, sj = map(int, input().split())
    ti, tj = map(int, input().split())
    res = 987654321
    visited = [[0] * L for _ in range(L)]
    res = moving(si, sj)
    print(res)
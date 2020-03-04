import copy
import sys
sys.stdin = open('../input.txt', 'r')


ds = [(1, 0), (0, 1), (0, -1), (-1, 0)] # 화우좌상

def is_field(i, j):
    return 0 <= i < H and 0 <= j < W


def break_block(arr, i):
    visited = []
    stack = []
    for j in range(W-1, -1, -1):
        if arr[i][j]:
            visited.append((i, j))
            stack.append((i, j))
            break

    while stack:
        si, sj = stack.pop()
        for di, dj in ds:
            ks = arr[si][sj]
            for k in range(1, ks):
                ni, nj = si + di * k, sj + dj * k
                if is_field(ni, nj) and (ni, nj) not in visited:
                    stack.append((ni, nj))
                    visited.append((ni, nj))

    visited = list(reversed(sorted(visited)))
    for i, j in visited:
        del arr[i][j]
        arr[i].append(0)

def repeat_combi(arr, d):
    global min_res
    if d == N:
        res = W * H - sum(arr, []).count(0)
        if res < min_res:
            min_res = res
    else:
        for i in range(H):
            temp_g = copy.deepcopy(arr)
            break_block(arr, i)
            repeat_combi(arr, d+1)
            arr = copy.deepcopy(temp_g)


for test in range(int(input())):
    N, W, H = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(H)]
    g = list(map(list, (map(reversed, zip(*g))))) # 2차원 리스트 시계 방향 돌리기
    W, H = H, W
    min_res = W * H + 1

    repeat_combi(g, 0)

    print('#{} {}'.format(test+1, min_res))
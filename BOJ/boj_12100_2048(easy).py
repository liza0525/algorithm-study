import sys
sys.stdin = open('../input.txt', 'r')
import copy


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def play(g, direction):
    isChange = [[0 for _ in range(N)] for _ in range(N)]
    if direction == 'left' or direction == 'right':
        g = list(map(list, zip(*g)))
    if direction == 'down' or direction == 'right':
        g = g[::-1]

    delta_r = -1
    for num in range(N*N):
        r, c = num // N, num % N
        if g[r][c] == 0: continue
        if not 0 <= r + delta_r < N: continue
        dist = 1
        while True:
            next_r = r + delta_r * dist
            if g[next_r][c] == g[r][c] and not isChange[next_r][c]:
                g[next_r][c] += g[r][c]
                isChange[next_r][c] = 1
                g[r][c] = 0
                break
            else:
                if g[next_r][c] == 0:
                    if next_r == 0 or next_r == N-1:
                        g[next_r][c] = g[r][c]
                        g[r][c] = 0
                        break
                else:
                    if dist != 1:
                        g[r + delta_r * (dist-1)][c] = g[r][c]
                        g[r][c] = 0
                    break
            dist += 1
    if direction == 'down' or direction == 'right':
        g = g[::-1]
    if direction == 'left' or direction == 'right':
        g = list(map(list, zip(*g)))
    return g


def dfs(g, d):
    global max_num
    if d == 5:
        num = max(sum(g, []))
        if num > max_num:
            max_num = num
    else:
        for direction in ['up', 'down', 'left', 'right']:
            g_temp = copy.deepcopy(g)
            dfs(play(g, direction), d+1)
            g = copy.deepcopy(g_temp)


N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
dfs(g, 0)

print(max_num)
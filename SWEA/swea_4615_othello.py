dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def isField(x, y):
    return 0 <= x < n and 0 <= y < n


def isEdge(x, y):
    return x == 0 or x == n - 1 or y == 0 or y == m - 1


def play(x, y, c):
    g[x][y] = c
    for i in range(8):
        stack = []
        tmp = 1
        nx = x + dx[i] * tmp
        ny = y + dy[i] * tmp
        while isField(nx, ny):
            if g[nx][ny] == c:
                for a, b in stack:
                    g[a][b] = c
                break
            elif g[nx][ny] == 0:
                stack = []
                break
            else:
                stack.append((nx, ny))
                tmp += 1
                nx = x + dx[i] * tmp
                ny = y + dy[i] * tmp


for test in range(int(input())):
    n, m = map(int, input().split())
    g = [[0] * n for _ in range(n)]
    hp = n // 2 - 1
    g[hp][hp], g[hp + 1][hp + 1], g[hp + 1][hp], g[hp][hp + 1] = 2, 2, 1, 1

    for _ in range(m):
        x, y, c = map(int, input().split())
        play(x - 1, y - 1, c)
    black, white = 0, 0
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 1:
                white += 1
            elif g[i][j] == 2:
                black += 1
    print('#{} {} {}'.format(test + 1, white, black))

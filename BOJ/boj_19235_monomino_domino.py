from pprint import pprint
import sys
sys.stdin = open('../input.txt', 'r')


def play(g, t, j):
    global score
    if g == green_g:
        if t == 1:
            g[0][j] = 1
        elif t == 2:
            g[0][j], g[0][j+1] = 1, 1
        elif t == 3:
            g[0][j], g[1][j] = 1, 1
    elif g == blue_g:
        if t == 1:
            g[0][j] = 1
        elif t == 2:
            g[0][j], g[1][j] = 1, 1
        elif t == 3:
            g[0][j], g[0][j-1] = 1, 1

    row = 0
    while row < 6:
        pass
    # for row in range(5, -1, -1):
    #     if t == 1:
    #         if not g[row][j]:
    #             g[row][j] = 1
    #             break
    #     elif t == 2:
    #         if g == green_g:
    #             if not g[row][j] and not g[row][j+1]:
    #                 g[row][j], g[row][j+1] = 1, 1
    #                 break
    #         if g == blue_g:
    #             if not g[row][j] and not g[row-1][j]:
    #                 g[row][j], g[row-1][j] = 1, 1
    #                 break
    #     elif t == 3:
    #         if g == green_g:
    #             if not g[row][j] and not g[row-1][j]:
    #                 g[row][j], g[row-1][j] = 1, 1
    #                 break
    #         if g == blue_g:
    #             if not g[row][j] and not g[row][j-1]:
    #                 g[row][j], g[row][j-1] = 1, 1
    #                 break
    cand = []
    for row in range(5, 1, -1):
        if sum(g[row]) == 4:
            score += 1
            cand.append(row)

    for row in cand:
        pass


green_g = [[0] * 4 for _ in range(6)]
blue_g = [[0] * 4 for _ in range(6)]
score = 0
N = int(input())
for _ in range(N):
    t, i, j = map(int, input().split())
    play(green_g, t, j)
    play(blue_g, t, 3-i)

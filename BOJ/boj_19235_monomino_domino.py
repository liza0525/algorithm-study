from pprint import pprint
import sys
sys.stdin = open('../input.txt', 'r')


def play(g, t, j):
    global green_g, blue_g
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



green_g = [[0] * 4 for _ in range(6)]
blue_g = [[0] * 4 for _ in range(6)]
N = int(input())
for _ in range(N):
    t, i, j = map(int, input().split())
    play(green_g, t, j)
    play(blue_g, t, 3-i)

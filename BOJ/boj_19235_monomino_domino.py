import sys
sys.stdin = open('../input.txt', 'r')


def play():
    pass


N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

green_g = [[0] * 4 for _ in range(6)]
blue_g = [[0] * 4 for _ in range(6)]
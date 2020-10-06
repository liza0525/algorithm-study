import sys
sys.stdin = open('../input.txt', 'r')


def tiling_fibo(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        tiles = [0] * (N+1)
        tiles[1], tiles[2] = 1, 2

        for num in range(3, N+1):
            tiles[num] = tiles[num-1] + tiles[num-2]

        return tiles[N] % 10007


N = int(input())
print(tiling_fibo(N))
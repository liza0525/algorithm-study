import sys
sys.stdin = open('../input.txt', 'r')

import collections

deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상 좌 하 우


class Snake:
    class Head:
        def __init__(self, r, c):
            self.r = r
            self.c = c

    def __init__(self, direction, r, c):
        self.direction = direction
        self.body = collections.deque()
        self.body.append((r, c))
        self.head = self.Head(r, c)

    def grow(self, r, c):
        self.body.appendleft((r, c))
        self.head = self.Head(r, c)

    def move(self, r, c):
        self.body.appendleft((r, c))
        self.body.pop()
        self.head = self.Head(r, c)


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def rotate(letter, idx):
    if letter == 'D':
        return idx - 1 if idx != 0 else 3
    elif letter == 'L':
        return idx + 1 if idx != 3 else 0


def play():
    play_time = 0
    time, letter = key_presses.pop(0)
    while True:
        if time == play_time:
            snake.direction = rotate(letter, snake.direction)
            if key_presses:
                time, letter = key_presses.pop(0)
        delta_r, delta_c = deltas[snake.direction]
        next_r, next_c = snake.head.r + delta_r, snake.head.c + delta_c

        if not is_field(next_r, next_c) or (next_r, next_c) in snake.body: # 벽이나 자기 몸에 부딪히면 끝
            return play_time + 1
        else:
            if (next_r, next_c) in apples:
                apples.remove((next_r, next_c))
                snake.grow(next_r, next_c)
            else:
                snake.move(next_r, next_c)
        play_time += 1

    return play_time


N = int(input())
K = int(input())
apples = []
for _ in range(K):
    r, c = map(int, input().split())
    apples.append((r-1, c-1))
L = int(input())
key_presses = []
for _ in range(L):
    time, letter = input().split()
    key_presses.append((int(time), letter))

snake = Snake(3, 0, 0)
print(play())
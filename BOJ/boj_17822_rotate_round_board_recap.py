import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint


def rotate(b_line, d, k):
    if d == 0:
        b_line = b_line[M - k:] + b_line[:M - k]
    else:
        b_line = b_line[k:] + b_line[:k]
    return b_line


def set_num():
    total_num = sum(sum(board, []))

    avg = total_num / remain_num
    for r in range(N):
        for c in range(M):
            if board[r][c] != 0:
                if board[r][c] > avg:
                    board[r][c] -= 1
                elif board[r][c] < avg:
                    board[r][c] += 1


def erase_num():
    global board, remain_num
    cand = set()
    for r in range(N):
        for c in range(M):
            if board[r][c] != 0:
                if r < N - 1 and board[r][c] == board[r + 1][c]:
                    cand.add((r, c))
                    cand.add((r + 1, c))
                if c < M - 1 and board[r][c] == board[r][c+1]:
                    cand.add((r, c))
                    cand.add((r, c+1))
                elif c == M - 1 and board[r][c] == board[r][0]:
                    cand.add((r, c))
                    cand.add((r, 0))

    if cand:
        for r, c in cand:
            board[r][c] = 0
        remain_num -= len(cand)
    else:
        if remain_num != 0:
            set_num()


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rotate_info = [list(map(int, input().split())) for _ in range(T)]
remain_num = N * M

for t, d, k in rotate_info:
    for r in range(N):
        if (r + 1) % t == 0:
            board[r] = rotate(board[r], d, k)
    erase_num()

print(sum(sum(board, [])))
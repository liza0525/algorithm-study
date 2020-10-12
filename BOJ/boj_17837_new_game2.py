import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

deltas = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


N, K = map(int, input().split())
colors = [list(map(int, input().split())) for _ in range(N)]
field = [[[] for _ in range(N)] for _ in range(N)] # 말 번호를 저장
pieces = [] # 말의 정보 저장(인덱스가 곧 말 번호)
playtime = 0


for numbering in range(K):
    r, c, direction = map(int, input().split())
    pieces.append([r-1, c-1, direction])
    field[r-1][c-1].append(numbering)

while True:
    toggle = False
    for numbering in range(K):
        now_r, now_c, now_direction = pieces[numbering]
        delta_r, delta_c = deltas[now_direction]
        next_r, next_c = now_r + delta_r, now_c + delta_c
        next_direction = now_direction
        now_height = field[now_r][now_c].index(numbering)

        move_pieces = field[now_r][now_c][now_height:]

        field[now_r][now_c] = field[now_r][now_c][:now_height]

        if not is_field(next_r, next_c) or colors[next_r][next_c] == 2:
            if next_direction == 1:
                next_direction = 2
            elif next_direction == 2:
                next_direction = 1
            elif next_direction == 3:
                next_direction = 4
            elif next_direction == 4:
                next_direction = 3

            delta_r, delta_c = deltas[next_direction]
            pieces[numbering][2] = next_direction
            next_r, next_c = now_r + delta_r, now_c + delta_c

            if not is_field(next_r, next_c) or colors[next_r][next_c] == 2:
                next_r, next_c = now_r, now_c

            elif colors[next_r][next_c] == 1:
                move_pieces.reverse()

        elif colors[next_r][next_c] == 1:
            move_pieces.reverse()

        for move_piece in move_pieces:
            pieces[move_piece][0], pieces[move_piece][1] = next_r, next_c

        field[next_r][next_c] += move_pieces

        if len(field[next_r][next_c]) >= 4:
            toggle = True
            break

    playtime += 1

    if toggle:
        break

    if playtime > 1000:
        playtime = -1
        break

print(playtime)
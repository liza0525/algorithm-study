import sys
sys.stdin = open('../input.txt', 'r')

deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북 동 남 서


def is_field(r, c):
    return 0 <= r < N and 0 <= c < M


def rotate(direction):
    return direction - 1 if direction != 0 else 3


N, M = map(int, input().split())
r, c, direction = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
cleans = [[False for _ in range(M)] for _ in range(N)]
clean_cnt = 0
toggle = False

while not toggle:
    if not cleans[r][c]:
        cleans[r][c] = True # 청소하기
        clean_cnt += 1
    for _ in range(4):
        direction = rotate(direction)
        delta_r, delta_c = deltas[direction]
        next_r, next_c = r + delta_r, c + delta_c
        if is_field(next_r, next_c) and g[next_r][next_c] == 0 and not cleans[next_r][next_c]:
            r, c = next_r, next_c
            break
    else:
        back_delta_r, back_delta_c = deltas[direction-2]
        back_r, back_c = r+back_delta_r, c+back_delta_c
        if is_field(back_r, back_c):
            if g[back_r][back_c] == 1:
                toggle = True
            else:
                r, c = back_r, back_c
        else:
            toggle = True

print(clean_cnt)
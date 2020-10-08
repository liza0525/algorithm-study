import sys
sys.stdin = open('../input.txt', 'r')

tetrominos = [
    [[(0, 1), (1, 0), (0, -1)]], # 정사각 모양
    [[(0, 1), (0, 1), (0, 1)], [(1, 0), (1, 0), (1, 0)]], # 막대 모양
    [[(1, 0), (0, 1), (1, 0)], [(1, 0), (0, -1), (1, 0)]], # 계단 모양1
    [[(0, 1), (1, 0), (0, 1)], [(0, -1), (1, 0), (0, -1)]], # 계단 모양2
    [[(1, 0), (1, 0), (0, 1)], [(1, 0), (1, 0), (0, -1)], [(0, 1), (1, 0), (1, 0)], [(0, -1), (1, 0), (1, 0)]], # 니은 모양1
    [[(0, 1), (0, 1), (-1, 0)], [(0, 1), (0, 1), (1, 0)], [(-1, 0), (0, 1), (0, 1)], [(1, 0), (0, 1), (0, 1)]], # 니은 모양2
    [[(0, 1), (0, 1), (-1, -1)], [(1, 0), (0, 1), (1, -1)], [(1, 0), (0, -1), (1, 1)], [(0, 1), (1, 0), (-1, 1)]], # 철 모양
]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < M


def set_tetro(r, c):
    global max_score
    for tetromino in tetrominos:
        for deltas in tetromino:
            now_r, now_c = r, c
            score = scores[now_r][now_c]
            for delta_r, delta_c in deltas:
                next_r, next_c = now_r + delta_r, now_c + delta_c
                if not is_field(next_r, next_c):
                    break
                score += scores[next_r][next_c]
                now_r, now_c = next_r, next_c
            else:
                max_score = max(max_score, score)


N, M = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(N)]

max_score = 0

for r in range(N):
    for c in range(M):
        set_tetro(r, c)

print(max_score)
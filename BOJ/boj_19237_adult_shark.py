import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')

deltas = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def reduce_scent():
    for r in range(N):
        for c in range(N):
            if visited[r][c][0]:
                visited[r][c][1] -= 1
                if visited[r][c][1] == 0:
                    visited[r][c][0] = 0


def move():
    global sharks, time
    while time <= 1000 and len(sharks) > 1:
        temp_sharks = dict()
        for (r, c), shark_num in sorted(sharks.items(), key=lambda x: -x[1]):
            next_r, next_c = 0, 0
            now_dir = now_shark_dirs[shark_num]
            for next_dir in shark_dir_priors[shark_num][now_dir]:
                delta_r, delta_c = deltas[next_dir]
                next_r, next_c = r + delta_r, c + delta_c
                if not is_field(next_r, next_c): continue
                if visited[next_r][next_c] == [0, 0]:
                    now_shark_dirs[shark_num] = next_dir
                    break
            else:
                for next_dir in shark_dir_priors[shark_num][now_dir]:
                    delta_r, delta_c = deltas[next_dir]
                    next_r, next_c = r + delta_r, c + delta_c
                    if not is_field(next_r, next_c): continue
                    if visited[next_r][next_c][0] == shark_num:
                        now_shark_dirs[shark_num] = next_dir
                        break

            if is_field(next_r, next_c):
                temp_sharks[(next_r, next_c)] = shark_num

        sharks = temp_sharks
        reduce_scent()
        for (r, c), shark_num in sharks.items():
            visited[r][c] = [shark_num, K]

        time += 1


N, M, K = map(int, input().split()) # ground 길이, 상어의 마릿수, 냄새 보존 시간
sharks = dict()
visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
time = 0

for r in range(N):
    line = list(map(int, input().split()))
    for c in range(N):
        if line[c]:
            sharks[(r, c)] = line[c]
            visited[r][c] = [line[c], K]

now_shark_dirs = [0] + list(map(int, input().split())) # 현재 상어의 방향
shark_dir_priors = [0]
for _ in range(M):
    shark_dir_prior = [0]
    for _ in range(4):
        shark_dir_prior.append(list(map(int, input().split())))
    shark_dir_priors.append(shark_dir_prior)

move()

print(time if time <= 1000 else -1)
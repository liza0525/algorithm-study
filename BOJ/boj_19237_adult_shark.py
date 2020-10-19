import sys
from pprint import pprint
sys.stdin = open('../input.txt', 'r')


import copy

deltas = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]

def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def scent():
    for r in range(N):
        for c in range(N):
            if visited[r][c][0] != 0:
                if visited[r][c][1] != 0:
                    visited[r][c][1] -= 1
                    if visited[r][c][1] == 0:
                        visited[r][c][0] = 0


def move():
    global ground, visited, time_ans, shark_cnt
    while time_ans < 5 and shark_cnt > 1:
        print('time_ans', time_ans)
        pprint(ground)
        pprint(visited)
        scent()
        temp_ground = [[0 for _ in range(N)] for _ in range(N)]
        for now_r in range(N):
            for now_c in range(N): # 모든 칸 돌기
                if ground[now_r][now_c] == 0: continue # 상어 없으면 빠이
                shark_num = ground[now_r][now_c]
                # while True:
                    # delta_r, delta_c = deltas[shark_dirs[shark_num]] # 상어가 있다면 상어의 현재 방향
                    # next_r, next_c = now_r + delta_r, now_c + delta_c # 해당 상어가 다음으로 갈 칸
                    # if is_field(next_r, next_c) and (visited[next_r][next_c] == [0, 0] or visited[next_r][next_c][0] == shark_num):
                    #     if ground[next_r][next_c] == 0:
                    #         temp_ground[next_r][next_c] = shark_num
                    #         visited[next_r][next_c] = [shark_num, K]
                    #     else:
                    #         peek_shark = min(shark_num, temp_ground[next_r][next_c])
                    #         temp_ground[next_r][next_c] = peek_shark
                    #         visited[next_r][next_c] = [peek_shark, K]
                    #     break
                    # else:
                now_dir = shark_dirs[shark_num]
                for direction in shark_infos[shark_num][now_dir]:
                    delta_r, delta_c = deltas[direction]
                    next_r, next_c = now_r + delta_r, now_c + delta_c
                    if not is_field(next_r, next_c): continue
                    if not(ground[next_r][next_c] == 0 or visited[next_r][next_c][0] == 0 or visited[next_r][next_c][0] == shark_num): continue
                    shark_dirs[shark_num] = direction
                    break

                delta_r, delta_c = deltas[shark_dirs[shark_num]] # 상어가 있다면 상어의 현재 방향
                next_r, next_c = now_r + delta_r, now_c + delta_c # 해당 상어가 다음으로 갈 칸

                if temp_ground[next_r][next_c] == 0:
                    temp_ground[next_r][next_c] = shark_num
                    visited[next_r][next_c] = [shark_num, K]
                else:
                    peek_shark = min(shark_num, temp_ground[next_r][next_c])
                    shark_cnt -= 1
                    temp_ground[next_r][next_c] = peek_shark
                    visited[next_r][next_c] = [peek_shark, K]


        ground = copy.deepcopy(temp_ground)
        print('shark_cnt', shark_cnt)
        print('=' * 30)
        time_ans += 1


N, M, K = map(int, input().split())
ground = [[0 for _ in range(N)] for _ in range(N)]
visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
shark_cnt = M
for r in range(N):
    line = list(map(int, input().split()))
    for c in range(N):
        if line[c] != 0:
            ground[r][c] = line[c]
            visited[r][c] = [line[c], K] # 상어 번호, 냄새 존재 시간

shark_dirs = [0] + list(map(int, input().split()))
shark_infos = [0] # 상어들의 방향 우선순위
time_ans = 0

for _ in range(M):
    shark_info = []
    for _ in range(4):
        dir_prior = list(map(int, input().split()))
        shark_info.append(dir_prior)
    shark_infos.append([0] + shark_info)

move()

print(time_ans if time_ans < 1000 else -1)
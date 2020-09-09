# 2020 KAKAO BLIND RECRUITMENT
from collections import deque


def solution(board):
    N = len(board)
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 드론의 하우상좌 이동
    queue = deque()
    visited = {}

    def is_field(i, j):
        return 0 <= i < N and 0 <= j < N

    def add_drone(i1, j1, i2, j2, pre_dist):
        if is_field(i1, j1) and is_field(i2, j2) and ((i1, j1), (i2, j2)) not in visited.keys():
            visited[((i1, j1), (i2, j2))] = pre_dist + 1
            queue.append(((i1, j1), (i2, j2)))

    def bfs(drone): # block은 2차 list
        queue.append(drone)
        visited.update({drone: 0}) # 현재 드론에 대한 이동 횟수

        while queue:
            (i1, j1), (i2, j2) = queue.popleft()
            pre_dist = visited[((i1, j1), (i2, j2))]
            # 방향 이동
            for di, dj in ds:
                ni1, nj1, ni2, nj2 = i1+di, j1+dj, i2+di, j2+dj
                if not is_field(ni1, nj2) or not is_field(ni2, nj2): continue
                if board[ni1][nj1] or board[ni2][nj2]: continue
                # 이동 가능
                add_drone(ni1, nj1, ni2, nj2, pre_dist)

            # 회전
            if i1 == i2: # 좌우로 놓인 상황
                # 드론 기준 위가 비었을 때
                if is_field(i2-1, j2) and not board[i2-1][j2] and is_field(i1-1, j1) and not board[i1-1][j1]:
                    add_drone(i2-1, j2-1, i1, j1, pre_dist)
                    add_drone(i1-1, j1+1, i2, j2, pre_dist)
                # 드론 기준 아래가 비었을 때
                if is_field(i2+1, j2) and not board[i2+1][j2] and is_field(i1+1, j1) and not board[i1+1][j1]:
                    add_drone(i1, j1, i2+1, j2-1, pre_dist)
                    add_drone(i2, j2, i1+1, j1+1, pre_dist)

            elif j1 == j2: # 상하로 놓인 상황
                # 드론 기준 왼쪽이 비었을 때
                if is_field(i2, j2-1) and not board[i2][j2-1] and is_field(i1, j1-1) and not board[i1][j1-1]:
                    add_drone(i1+1, j1-1, i2, j2, pre_dist)
                    add_drone(i2-1, j2-1, i1, j1, pre_dist)
                # 드론 기준 오른쪽이 비었을 때
                if is_field(i2, j2+1) and not board[i2][j2+1] and is_field(i1, j1+1) and not board[i1][j1+1]:
                    add_drone(i1, j1, i2-1, j2+1, pre_dist)
                    add_drone(i2, j2, i1+1, j1+1, pre_dist)

        if ((N-2, N-1), (N-1, N-1)) in visited.keys() and ((N-1, N-2), (N-1, N-1)) in visited.keys():
            return min(visited[((N-2, N-1), (N-1, N-1))], visited[((N-1, N-2), (N-1, N-1))])
        elif ((N-2, N-1), (N-1, N-1)) in visited.keys():
            return visited[((N-2, N-1), (N-1, N-1))]
        else:
            return visited[((N-1, N-2), (N-1, N-1))]

    return bfs(((0, 0), (0, 1)))


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
# 7
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
# 21
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
# 11
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
# 33
print(solution([[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# 10
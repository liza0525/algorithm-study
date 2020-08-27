# 2020 KAKAO BLIND RECRUITMENT
from pprint import pprint

def solution(n, build_frame):
    answer = []
    wall = [[[0, 0, 0, 0] for _ in range(n+1)] for _ in range(n+1)]
    # 각 위치에서 상하좌우가 연결이 되었는지 아닌지
    up, down, left, right = 0, 1, 2, 3

    for i, j, a, b in build_frame: # a : 기둥 or 보 , b : 삭제 or 설치
        if a == 0: # 기둥인 경우
            if b == 0: # 기둥 삭제
                if not wall[i][j+1][right] or wall[i][j][up] or wall[i][j][down]:
                    wall[i][j][right], wall[i][j+1][left] = 0, 0
                elif not wall[i][j+1][up] or (wall[i-1][j+1][left] or (wall[i-1][j+1][up] and wall[i][j+1][down])):
                    wall[i][j][right], wall[i][j+1][left] = 0, 0
                elif not wall[i][j+1][down] or (wall[i+1][j+1][left] or (wall[i][j+1][up] and wall[i+1][j+1][down])):
                    wall[i][j][right], wall[i][j+1][left] = 0, 0
            elif b == 1: # 기둥 추가
                if j == 0 or wall[i][j][left] or wall[i][j][up] or wall[i][j][down]:
                    wall[i][j][right], wall[i][j+1][left] = 1, 1
        elif a == 1: # 보인 경우
            if b == 0: # 보 삭제
                # if wall[i][j][left] or wall[i+1][j][left] or (not wall[i][j][up] and not wall[i+1][j][down]):
                if (not wall[i][j][up] and not wall[i+1][j][down]):
                    wall[i][j][down], wall[i+1][j][up] = 0, 0
                elif (wall[i][j][up] and (wall[i][j][left] or wall[i-1][j][left])):
                    if (wall[i][j][down] and (wall[i][j][left] or wall[i+1][j][left])):
                        wall[i][j][down], wall[i+1][j][up] = 0, 0
            elif b == 1: # 보 추가
                if wall[i][j][left] or wall[i+1][j][left] or (wall[i][j][up] and wall[i+1][j][down]):
                    wall[i][j][down], wall[i+1][j][up] = 1, 1
        # pprint(wall)

    for i in range(n+1):
        for j in range(n+1):
            if wall[i][j][right]: # 기둥이 연결 된 경우
                answer.append([i, j, 0])
            if wall[i][j][down]: # 보가 연결 된 경우
                answer.append([i, j, 1])
    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# 답 [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
# 답 [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
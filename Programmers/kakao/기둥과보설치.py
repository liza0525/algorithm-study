# 2020 KAKAO BLIND RECRUITMENT
from pprint import pprint

def solution(n, build_frame):
    materials = set()

    for x, y, a, b in build_frame:
        if b == 0: # 삭제
            materials.remove((x, y, a))
        elif b == 1: # 추가
            materials.add((x, y, a))

        for (xx, yy, aa) in materials:
            if aa == 0: # 기둥인 경우
                if yy == 0 or (xx, yy-1, 0) in materials or (xx, yy, 1) in materials or (xx-1, yy, 1) in materials:
                    continue
                else:
                    if b == 0: # 삭제 한 거 다시 추가
                        materials.add((x, y, a))
                    elif b == 1: # 추가 한 거 다시 삭제
                        materials.remove((x, y, a))
                    break
            elif aa == 1: # 보인 경우
                if (xx, yy-1, 0) in materials or (xx+1, yy-1, 0) in materials or ((xx-1, yy, 1) in materials and (xx+1, yy, 1) in materials):
                    continue
                else:
                    if b == 0: # 삭제 한 거 다시 추가
                        materials.add((x, y, a))
                    elif b == 1: # 추가 한 거 다시 삭제
                        materials.remove((x, y, a))
                    break
                    
    return sorted(map(list, materials), key=lambda x: (x[0], x[1], x[2]))

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# 답 [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
# 답 [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
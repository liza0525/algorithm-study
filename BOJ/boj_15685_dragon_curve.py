import sys
sys.stdin = open('../input.txt', 'r')


deltas = [(1, 0), (0, -1), (-1, 0), (0, 1)] # x증가, y감소, x감소, y증가


N = int(input())
points = set()
num_square = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())
    delta_x, delta_y = deltas[d]
    
    # 0세대 만들기
    points.add((x, y))
    x += delta_x
    y += delta_y
    points.add((x, y))
    dir_set = [d]
    
    # 0세대 이상 만들기
    for gg in range(1, g+1):
        D = len(dir_set)
        for dd in range(D-1, -1, -1):
            d = (dir_set[dd] + 1) % 4
            delta_x, delta_y = deltas[d]
            x += delta_x
            y += delta_y
            points.add((x, y))
            dir_set.append(d)

# 윤영쓰 화이팅!!
# 사각형 찾기
for xx in range(100):
    for yy in range(100):
        if (xx, yy) in points and (xx+1, yy) in points and (xx, yy+1) in points and (xx+1, yy+1) in points:
            num_square += 1

print(num_square)
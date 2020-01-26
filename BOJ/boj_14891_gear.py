def rotate(num, d):
    global gears
    if d == 1: # 시계 방향
        gears[num] = gears[num][7:] + gears[num][:7]
    elif d == -1: # 반시계 방향
        gears[num] = gears[num][1:] + gears[num][:1]

gears = [0]
for _ in range(4):
    gears.append(list(map(int, input())))

n = int(input())
for _ in range(n):
    gear_r = [0] * 5
    num, d = map(int, input().split())
    gear_r[num] = d
    for i in range(num, 1, -1):
        if gears[i-1][2] != gears[i][6]:
            gear_r[i-1] = gear_r[i] * -1
    for i in range(num, 4):
        if gears[i][2] != gears[i+1][6]:
            gear_r[i+1] = gear_r[i] * -1
    for i in range(1, 5):
        if gear_r[i] != 0:
            rotate(i, gear_r[i])

res = 0
for i in range(1, 5):
    if gears[i][0] == 1:
        res += 2**(i-1)
print(res)
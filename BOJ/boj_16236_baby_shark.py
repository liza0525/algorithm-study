import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
shark_size = 2
fishes = 0
road_length = 0
time = 0
f_info = []
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def isField(x, y):
    return 0 <= x < n and 0 <= y < n

toggle = True
for j in range(n):
    for i in range(n):
        if g[i][j] == 9:
            shark_x, shark_y = i, j
            g[i][j] = 0
            toggle = False
            break
    if not toggle:
        break

queue = []
visited = []
queue.append((shark_x, shark_y))
visited.append((shark_x, shark_y))

while queue:
    temp = queue[:]
    queue = []
    candidate = []
    while temp:
        x, y = temp.pop(0)
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if isField(nx, ny) and (nx, ny) not in visited:
                if g[nx][ny] == 0 or g[nx][ny] == shark_size:
                    queue.append((nx, ny))
                    visited.append((nx, ny))
                elif g[nx][ny] < shark_size and (nx, ny) not in candidate:
                    candidate.append((nx, ny))
    road_length += 1

    if candidate:
        queue = []
        visited = []
        mx, my = candidate[0]
        if len(candidate) == 1:
            pass
        else:
            for x, y in candidate:
                if x < mx:
                    mx, my = x, y
                elif x == mx:
                    if y < my:
                        mx, my = x, y
        g[mx][my] = 0
        queue.append((mx, my))
        fishes += 1
        time += road_length
        road_length = 0

    if fishes == shark_size:
        shark_size += 1
        fishes = 0

print(time)
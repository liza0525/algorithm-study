import sys
sys.stdin = open('../input.txt', 'r')


class Fish:
    def __init__(self, s, d, z):
        self.speed = s
        self.direction = d
        self.size = z


def move(r, c, direction, speed):
    if direction == 1 or direction == 2:
        divider = 2 * (R-1)
    elif direction == 3 or direction == 4:
        divider = 2 * (C-1)

    if direction == 1:
        r = (r-speed) % divider
        if r >= R:
            direction = 2
            r = divider - r
    elif direction == 2:
        r = (r+speed) % divider
        if r >= R:
            direction = 1
            r = divider - r
    elif direction == 3:
        c = (c+speed) % divider
        if c >= C:
            direction = 4
            c = divider - c
    elif direction == 4:
        c = (c-speed) % divider
        if c >= C:
            direction = 3
            c = divider - c

    return r, c, direction


R, C, M = map(int, input().split())
total_size = 0
fishes = dict()

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    fish = Fish(s, d, z)
    fishes[(r-1, c-1)] = fish


for person_c in range(C):
    # 물고기 잡기
    for r in range(R):
        if (r, person_c) in fishes.keys():
            fish = fishes[(r, person_c)]
            total_size += fish.size
            del fishes[(r, person_c)]
            break

    # 물고기 이동
    temp = dict()
    for fish_r in range(R):
        for fish_c in range(C):
            if (fish_r,fish_c) in fishes.keys():
                fish = fishes[(fish_r, fish_c)]
                next_r, next_c, direction = move(fish_r, fish_c, fish.direction, fish.speed)
                fish.direction = direction
                if (next_r, next_c) not in temp.keys() or temp[(next_r, next_c)].size < fish.size:
                    temp[(next_r, next_c)] = fish
    fishes = temp


print(total_size)
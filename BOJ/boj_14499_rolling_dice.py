import sys
sys.stdin = open('../input.txt', 'r')


deltas = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # (), 동, 서, 북, 남

class Dice:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.up = 0
        self.down = 0
        self.east = 0
        self.west = 0
        self.south = 0
        self.north = 0

    def roll_east(self):
        self.up, self.down, self.east, self.west = self.west, self.east, self.up, self.down

    def roll_west(self):
        self.up, self.down, self.east, self.west = self.east, self.west, self.down, self.up

    def roll_south(self):
        self.up, self.down, self.south, self.north = self.north, self.south, self.up, self.down

    def roll_north(self):
        self.up, self.down, self.south, self.north = self.south, self.north, self.down, self.up


def is_field(r, c):
    return 0 <= r < R and 0 <= c < C


R, C, r, c, K = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(R)]
commands = list(map(int, input().split()))

dice = Dice(r, c)

for command in commands:
    delta_r, delta_c = deltas[command]
    next_r, next_c = dice.r + delta_r, dice.c + delta_c

    if not is_field(next_r, next_c):
        continue

    if command == 1: # 동
        dice.roll_east()
    elif command == 2: # 서
        dice.roll_west()
    elif command == 3: # 북
        dice.roll_north()
    elif command == 4: # 남
        dice.roll_south()

    dice.r, dice.c = next_r, next_c

    if ground[dice.r][dice.c] == 0:
        ground[dice.r][dice.c] = dice.down
    else:
        dice.down, ground[dice.r][dice.c] = ground[dice.r][dice.c], 0

    print(dice.up)
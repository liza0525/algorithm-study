import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

class Cube:
    def __init__(self):
        self.up = [['w' for _ in range(3)] for _ in range(3)] # 윗면 흰색
        self.down = [['y' for _ in range(3)] for _ in range(3)] # 아랫면 노란색
        self.front = [['r' for _ in range(3)] for _ in range(3)] # 앞면 빨간색
        self.back = [['o' for _ in range(3)] for _ in range(3)] # 뒷면 주황색
        self.left = [['g' for _ in range(3)] for _ in range(3)] # 왼쪽면 초록색
        self.right = [['b' for _ in range(3)] for _ in range(3)] # 오른쪽면 파란색


    def side_clock(self, side):
        side[0][0], side[2][0], side[2][2], side[0][2] = side[2][0], side[2][2], side[0][2], side[0][0]
        side[0][1], side[1][0], side[2][1], side[1][2] = side[1][0], side[2][1], side[1][2], side[0][1]

    def side_anticlock(self, side):
        side[0][0], side[2][0], side[2][2], side[0][2] = side[0][2], side[0][0], side[2][0], side[2][2]
        side[0][1], side[1][0], side[2][1], side[1][2] = side[1][2], side[0][1], side[1][0], side[2][1]


    def up_clock(self):
        for i in range(3):
            self.back[2][i], self.right[i][0], self.front[0][2-i], self.left[2-i][2] = self.left[2-i][2], self.back[2][i], self.right[i][0], self.front[0][2-i]
        self.side_clock(self.up)

    def up_anticlock(self):
        for i in range(3):
            self.back[2][i], self.right[i][0], self.front[0][2-i], self.left[2-i][2] = self.right[i][0], self.front[0][2-i], self.left[2-i][2], self.back[2][i]
        self.side_anticlock(self.up)

    def down_clock(self):
        for i in range(3):
            self.back[0][i], self.right[i][2], self.front[2][2-i], self.left[2-i][0] = self.right[i][2], self.front[2][2-i], self.left[2-i][0], self.back[0][i]
        self.side_clock(self.down)

    def down_anticlock(self):
        for i in range(3):
            self.back[0][i], self.right[i][2], self.front[2][2-i], self.left[2-i][0] = self.left[2-i][0], self.back[0][i], self.right[i][2], self.front[2][2-i]
        self.side_anticlock(self.down)

    def front_clock(self):
        for i in range(3):
            self.down[0][2-i], self.left[2][i], self.up[2][i], self.right[2][i] = self.right[2][i], self.down[0][2-i], self.left[2][i], self.up[2][i]
        self.side_clock(self.front)

    def front_anticlock(self):
        for i in range(3):
            self.down[0][2-i], self.left[2][i], self.up[2][i], self.right[2][i] = self.left[2][i], self.up[2][i], self.right[2][i], self.down[0][2-i]
        self.side_anticlock(self.front)

    def back_clock(self):
        for i in range(3):
            self.down[2][2-i], self.left[0][i], self.up[0][i], self.right[0][i] = self.left[0][i], self.up[0][i], self.right[0][i], self.down[2][2-i]
        self.side_clock(self.back)

    def back_anticlock(self):
        for i in range(3):
            self.down[2][2-i], self.left[0][i], self.up[0][i], self.right[0][i] = self.right[0][i], self.down[2][2-i], self.left[0][i], self.up[0][i]
        self.side_anticlock(self.back)

    def left_clock(self):
        for i in range(3):
            self.back[i][0], self.up[i][0], self.front[i][0], self.down[i][0] = self.down[i][0], self.back[i][0], self.up[i][0], self.front[i][0]
        self.side_clock(self.left)

    def left_anticlock(self):
        for i in range(3):
            self.back[i][0], self.up[i][0], self.front[i][0], self.down[i][0] = self.up[i][0], self.front[i][0], self.down[i][0], self.back[i][0]
        self.side_anticlock(self.left)

    def right_clock(self):
        for i in range(3):
            self.back[i][2], self.up[i][2], self.front[i][2], self.down[i][2] = self.up[i][2], self.front[i][2], self.down[i][2], self.back[i][2]
        self.side_clock(self.right)

    def right_anticlock(self):
        for i in range(3):
            self.back[i][2], self.up[i][2], self.front[i][2], self.down[i][2] = self.down[i][2], self.back[i][2], self.up[i][2], self.front[i][2]
        self.side_anticlock(self.right)


TC = int(input())

for test in range(TC):
    N = int(input())
    cube = Cube()
    turn_infos = input().split()
    for turn_info in turn_infos:
        if turn_info == 'U+':
            cube.up_clock()
        elif turn_info == 'U-':
            cube.up_anticlock()
        elif turn_info == 'D+':
            cube.down_clock()
        elif turn_info == 'D-':
            cube.down_anticlock()
        elif turn_info == 'F+':
            cube.front_clock()
        elif turn_info == 'F-':
            cube.front_anticlock()
        elif turn_info == 'B+':
            cube.back_clock()
        elif turn_info == 'B-':
            cube.back_anticlock()
        elif turn_info == 'L+':
            cube.left_clock()
        elif turn_info == 'L-':
            cube.left_anticlock()
        elif turn_info == 'R+':
            cube.right_clock()
        elif turn_info == 'R-':
            cube.right_anticlock()

    for line in range(3):
        print(''.join(cube.up[line]))
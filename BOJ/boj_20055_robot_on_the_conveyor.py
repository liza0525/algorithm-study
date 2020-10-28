import sys
sys.stdin = open('../input.txt', 'r')


class Conveyor:
    def __init__(self):
        self.strengths = []
        self.robots = [] # 로봇이 존재하는 위치 index
        self.zero_cnt = 0

    def rotate(self):
        self.strengths = [self.strengths[-1]] + self.strengths[:-1]
        for idx in range(len(self.robots)):
            self.robots[idx] += 1
        self.remove_robot()
    
    def add_robot(self):
        if not self.robots or (self.robots[0] != 0 and self.strengths[0] != 0):
            self.robots.append(0)
            self.strengths[0] -= 1
            if self.strengths[0] == 0:
                self.zero_cnt += 1

    def move_robot(self):
        for idx in range(len(self.robots)):
            if idx != 0 and self.robots[idx] + 1 == self.robots[idx - 1]:
                continue
            if self.robots[idx] < N-1 and self.strengths[self.robots[idx] + 1] != 0:
                self.robots[idx] += 1
                self.strengths[self.robots[idx]] -= 1
                if self.strengths[self.robots[idx]] == 0:
                    self.zero_cnt += 1
        self.remove_robot()

    def remove_robot(self):
        if self.robots and self.robots[0] == N-1:
            self.robots = self.robots[1:]


N, K = map(int, input().split())
conveyor = Conveyor()
for strength in list(map(int, input().split())):
    conveyor.strengths.append(strength)

level = 0
while conveyor.zero_cnt < K:
    level += 1
    conveyor.rotate()
    conveyor.move_robot()
    conveyor.add_robot()

print(level)


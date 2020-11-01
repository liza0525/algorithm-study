import sys
sys.stdin = open('../input.txt', 'r')
from pprint import pprint

deltas = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


class Fireball:
    def __init__(self, m, s, d): # m 질량, s 속력, d 방향
        self.m = m
        self.s = s
        self.d = d


class Ground:
    def __init__(self):
        self.fireballs = dict()

    def move(self):
        temp_fireballs = dict()

        for (r, c), fireball_list in self.fireballs.items():
            for fireball in fireball_list:
                delta_r, delta_c = deltas[fireball.d]
                next_r, next_c = (r + fireball.s * delta_r) % N, (c + fireball.s * delta_c) % N
                if (next_r, next_c) not in temp_fireballs:
                    temp_fireballs[(next_r, next_c)] = [fireball]
                else:
                    temp_fireballs[(next_r, next_c)].append(fireball)

        self.fireballs = self.split(temp_fireballs)

    def split(self, fireballs):
        temp_fireballs = dict()
        for (r, c), fireball_list in fireballs.items():
            if len(fireball_list) > 1:
                n = len(fireball_list)
                total_m, total_s, is_same_d = 0, 0, True
                is_odd_d = fireball_list[0].d % 2
                while fireball_list:
                    fireball = fireball_list.pop()
                    total_m += fireball.m
                    total_s += fireball.s
                    if fireball.d % 2 != is_odd_d:
                        is_same_d = False
                new_m = total_m // 5
                if new_m != 0:
                    new_s = total_s // n
                    new_d = [0, 2, 4, 6] if is_same_d else [1, 3, 5, 7]
                    temp_fireballs[(r, c)] = [Fireball(new_m, new_s, new_d[0])]
                    for i in range(1, 4):
                        temp_fireballs[(r, c)].append(Fireball(new_m, new_s, new_d[i]))
            else:
                temp_fireballs[(r, c)] = fireball_list

        return temp_fireballs


N, M, K = map(int, input().split())
ground = Ground()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    ground.fireballs[(r-1, c-1)] = [Fireball(m, s, d)]

while K > 0:
    ground.move()
    K -= 1

total_m = 0

for fireball_list in ground.fireballs.values():
    for fireball in fireball_list:
        total_m += fireball.m

print(total_m)
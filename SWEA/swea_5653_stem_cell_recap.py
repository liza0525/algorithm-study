import sys
sys.stdin = open('../input.txt', 'r')

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Cell:
    def __init__(self, life, time, state):
        self.life = life
        self.time = time
        self.state = state


class Field:
    def __init__(self):
        self.cells = dict()

    def add(self, r, c, life, cell_dict):
        cell = Cell(life, 0, 'non-activate')
        cell_dict[(r, c)] = cell

    def flow_time(self):
        for cell in self.cells.values():
            if cell.state != 'dead':
                cell.time += 1

    def change_state(self):
        for cell in self.cells.values():
            if cell.time == cell.life:
                if cell.state == 'non-activate':
                    cell.state = 'activate'
                elif cell.state == 'activate':
                    cell.state = 'dead'
                cell.time = 0

    def spread(self):
        cand = dict()
        for (r, c), cell in self.cells.items():
            if cell.state == 'activate' and cell.time == 1:
                for delta_r, delta_c in deltas:
                    next_r, next_c = r + delta_r, c + delta_c
                    if (next_r, next_c) not in self.cells:
                        if (next_r, next_c) not in cand:
                            self.add(next_r, next_c, cell.life, cand)
                        else:
                            next_cell = cand[(next_r, next_c)]
                            if next_cell.state == 'non-activate' and next_cell.time == 0 and cell.life > next_cell.life:
                                cand[(next_r, next_c)].life = cell.life

        for (r, c), cell in cand.items():
            self.add(r, c, cell.life, self.cells)

    def get_remain_cell_cnt(self):
        remain_cell_cnt = 0
        for (r, c), cell in self.cells.items():

            if cell.state != 'dead':
                remain_cell_cnt += 1
        return remain_cell_cnt


T = int(input())

for test_case in range(T):
    N, M, K = map(int, input().split())
    field = Field()

    for r in range(N):
        line = list(map(int, input().split()))
        for c in range(M):
            if line[c] != 0:
                field.add(r, c, line[c], field.cells)

    for k in range(K):
        field.flow_time()
        field.spread()
        field.change_state()

    print('#{} {}'.format(test_case + 1, field.get_remain_cell_cnt()))
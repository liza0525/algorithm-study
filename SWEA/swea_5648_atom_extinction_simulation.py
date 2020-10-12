import sys
sys.stdin = open('../input.txt', 'r')

deltas = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]


class Atom:
    def __init__(self, x, y, direction, energy):
        self.x = x
        self.y = y
        self.direction = direction
        self.energy = energy


class Field:
    def __init__(self):
        self.atoms = dict()
        self.total_energy = 0

    def add(self, atom):
        self.atoms.update({(atom.x, atom.y): [atom]})

    def move_atoms(self):
        new_atoms = dict()
        for (x, y), atom_list in self.atoms.items():
            for atom in atom_list:
                delta_x, delta_y = deltas[atom.direction]
                next_x, next_y = x + delta_x, y + delta_y
                if not (-1000 <= next_x <= 1000 and -1000 <= next_y <= 1000): continue
                if (next_x, next_y) not in new_atoms:
                    new_atoms.update({(next_x, next_y): [atom]})
                else:
                    new_atoms[(next_x, next_y)].append(atom)
        self.atoms = new_atoms

    def get_energy(self):
        del_cand = []
        for (x, y), atom_list in self.atoms.items():
            if len(atom_list) == 1: continue
            for atom in atom_list:
                self.total_energy += atom.energy
            del_cand.append((x, y))

        for (x, y) in del_cand:
            del self.atoms[(x, y)]


T = int(input())
for test_case in range(T):
    N = int(input())
    field = Field()
    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        atom = Atom(x, y, direction, energy)
        field.add(atom)

    while field.atoms:
        field.move_atoms()
        field.get_energy()

    print('#{} {}'.format(test_case+1, field.total_energy))
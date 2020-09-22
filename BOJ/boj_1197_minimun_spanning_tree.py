import sys
sys.stdin = open('../input.txt', 'r')


class Tree:
    def __init__(self, V):
        self.parent = dict()
        self.rank = dict()
        for i in range(1, V + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find_root(self, v):
        parent_vertex = self.parent[v]
        if parent_vertex != v:
            self.parent[v] = self.find_root(parent_vertex)
        return self.parent[v]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


def kruskal(V, stack):
    min_weight = 0
    tree = Tree(V)

    while stack:
        weight, vertex1, vertex2 = stack.pop()
        root1 = tree.find_root(vertex1)
        root2 = tree.find_root(vertex2)

        if root1 != root2:
            tree.union(root1, root2)
            min_weight += weight
    return min_weight


V, E = map(int, input().split())
stack = []
for _ in range(E):
    vertex1, vertex2, weight = map(int, input().split())
    stack.append([weight, vertex1, vertex2])

stack.sort(key=lambda x: -x[0])

print(kruskal(V, stack))
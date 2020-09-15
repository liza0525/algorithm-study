import sys
import heapq
sys.stdin = open('../input.txt', 'r')


deltas = [(-1, -1), (-1, 0), (-1, 1),
          (0, -1), (0, 1),
          (1, -1), (1, 0), (1, 1)]


def is_field(r, c):
    return 0 <= r < N and 0 <= c < N


def spring_summer():
    for num in range(N*N):
        r, c = num // N, num % N
        if trees[r][c]:
            dead_trees = []
            for i in range(len(trees[r][c])):
                if trees[r][c][i] <= ground[r][c]:
                    ground[r][c] -= trees[r][c][i]
                    trees[r][c][i] += 1
                else:
                    dead_trees = trees[r][c][i:]
                    trees[r][c] = trees[r][c][:i]
                    break
            for tree in dead_trees:
                ground[r][c] += tree // 2


def autumn():
    for num in range(N*N):
        r, c = num // N, num % N
        if trees[r][c]:
            for tree in trees[r][c]:
                if tree % 5 == 0:
                    for delta_r, delta_c in deltas:
                        if is_field(r+delta_r, c+delta_c):
                            trees[r+delta_r][c+delta_c].insert(0, 1)
                            # heapq.heappush(trees[r+delta_r][c+delta_c], 1)


def winter():
    for num in range(N*N):
        r, c = num // N, num % N
        ground[r][c] += A[r][c]


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ground = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, age = map(int, input().split())
    heapq.heappush(trees[r-1][c-1], age)


for _ in range(K):
    spring_summer()
    autumn()
    winter()

print(len(sum(sum(trees, []), [])))
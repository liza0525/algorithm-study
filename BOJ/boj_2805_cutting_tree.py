import sys
sys.stdin = open('../input.txt', 'r')

N, M = map(int, input().split())
trees = list(map(int, input().split()))
min_height, max_height = 1, max(trees)

while min_height <= max_height:
    total_tree = 0
    cutting_height = (max_height + min_height) // 2

    for tree in trees:
        if tree > cutting_height:
            total_tree += tree - cutting_height

    if total_tree >= M:
        min_height = cutting_height + 1
    elif total_tree < M:
        max_height = cutting_height - 1

print(max_height)
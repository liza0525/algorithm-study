import sys
sys.stdin = open('../input.txt', 'r')

from collections import deque

N = int(input())
tree = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]


for _ in range(N - 1):
    first_node, second_node = map(int, input().split())
    tree[first_node].append(second_node)
    tree[second_node].append(first_node)

queue = deque()
queue.append(1)

while queue:
    now_node = queue.popleft()
    for next_node in tree[now_node]:
        if next_node != 1 and parents[next_node] == 0:
            parents[next_node] = now_node
            queue.append(next_node)

for node in parents[2:]:
    print(node)
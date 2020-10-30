import sys
sys.stdin = open('../input.txt', 'r')
from collections import deque


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dist = [0 for _ in range(N+1)]

queue = deque([1])
dist[1] = 1
while queue:
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if graph[next_node]:
            if not dist[next_node] or dist[next_node] > dist[now_node] + 1:
                queue.append(next_node)
                dist[next_node] = dist[now_node] + 1


max_dist = max(dist)
max_dist_cnt = dist.count(max_dist)
for idx in range(1, N+1):
    if dist[idx] == max_dist:
        break
print(idx, max_dist-1, max_dist_cnt)